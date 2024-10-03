from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.conf import settings
from django.utils.safestring import mark_safe
from .forms import DocumentUploadForm
from .models import UploadedDocument
import fitz
import docx
import json
import os

import google.generativeai as genai
genai.configure(api_key=settings.GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-pro')
# model = genai.GenerativeModel('gemini-1.5-flash-latest', generation_config={"response_mime_type": "application/json"})

ai_chat = model.start_chat(history=[])

# Helper functions to parse different file formats
def parse_pdf(file_path):
    doc = fitz.open(file_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text


def parse_docx(file_path):
    doc = docx.Document(file_path)
    return '\n'.join([para.text for para in doc.paragraphs])


def parse_txt(file_path):
    with open(file_path, 'r') as file:
        return file.read()


def parse_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return json.dumps(data, indent=4)


# View to handle file upload
def upload_document(request):
    if request.method == 'POST':
        form = DocumentUploadForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save()
            file_path = document.file.path

            # Parse the document based on file extension
            if file_path.endswith('.pdf'):
                content = parse_pdf(file_path)
            elif file_path.endswith('.docx'):
                content = parse_docx(file_path)
            elif file_path.endswith('.txt'):
                content = parse_txt(file_path)
            elif file_path.endswith('.json'):
                content = parse_json(file_path)
            else:
                return JsonResponse({"error": "Unsupported file format"}, status=400)

            # Save the document content into the session
            request.session['document_content'] = content
            # I added this in case you want to delete the document after processing it.
            # if os.path.exists(file_path):
            #     os.remove(file_path)
            return redirect('chat')
    else:
        form = DocumentUploadForm()

    return render(request, 'upload.html', {'form': form})


# Chat view to interact with the document
def chat(request):
    document_content = request.session.get('document_content', '')

    if request.method == 'POST':
        user_query = json.loads(request.body).get('user_query')
        ai_response = ai_chat.send_message(f'{user_query} \n Document: {document_content}')
        return JsonResponse({"response": mark_safe(ai_response.text)})

    return render(request, 'chat.html', {})

