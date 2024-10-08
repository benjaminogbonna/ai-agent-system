# AI/Agent System

## Overview
The **AI/Agent System** is a web application that enables users to upload documents (in `.txt`, `.json`, `.pdf`, or `.doc` formats) and engage in a chat-based interaction with the document content. This system leverages Django for the backend and integrates Bootstrap for a polished UI.

Users can ask questions related to the uploaded document, and the system will provide responses based on the document’s content.

## Features
- **Document Upload**: Users can upload documents in `.txt`, `.json`, `.pdf`, and `.doc` formats.
- **Chat-to-Document Interaction**: Users can interact with the document via a chat interface.
- **Responsive Design**: The UI is built using Bootstrap for a clean and responsive user experience.
- **AI-Powered Responses**: The system processes the user's queries and returns relevant information from the uploaded document.

## Technology Stack
- **Backend**: Django (Python)
- **Frontend**: Bootstrap 4, JavaScript
- **Templates**: Django templating engine
- **Database**: SQLite (since it's a simple project)

## Setup Instructions

### Prerequisites
- Python 3.10
- Django 4.2
- google-generativeai

### 1. Clone the Repository
```bash
git clone https://github.com/benjaminogbonna/ai-agent-system.git
cd ai-agent-system
```

### 2. Install Dependencies
Create a virtual environment and install the necessary dependencies:

```bash
python3 -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Set Up Django
Run the following commands to set up the Django project:

```bash
python manage.py migrate
```

### 4. Run the Server
Start the Django development server:

```bash
python manage.py runserver
```

The app will be accessible at `http://127.0.0.1:8000/`.

### 5. Upload and Interact with Documents

- Navigate to the **Upload Document** page via the navbar and upload a document.
- After uploading, you will be redirected to the chat interface, where you can start interacting with the document by asking questions.


## Future Improvements
- **User authentication**: Allow users to sign up and manage their document history.


## Contributing
Pull requests are welcome! To contribute:
1. Fork the repository.
2. Create a new feature branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Open a pull request.


## Contact Information
[Linkedin](https://linkedin.com/in/benjamin-ogbonna)


## License
[MIT](https://choosealicense.com/licenses/mit/)