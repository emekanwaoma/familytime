# Django Resume Summarization API

## Overview
This project is a Django-based API for summarizing resumes using OpenAI's GPT model. Applicants can upload their resumes, and HR users can retrieve AI-generated summaries.

## Features
- **Applicant Endpoints**:
  - Upload resumes (PDF only).
- **HR Endpoints**:
  - User authentication (sign up, login).
  - View resume summaries.
  
## Technologies Used
- Django
- Django REST Framework
- OpenAI API
- Python-Decouple
- PostgreSQL (or SQLite for development)

## Getting Started

### Prerequisites
- Python 3.8 or higher
- pip
- PostgreSQL (optional, for production)

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/emekanwaoma/familytime
   cd your-repo
   ```
2. **Create A virtual environment**
   ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. **Install Dependencies**
   ```bash
    pip install -r requirements.txt
   ```

4. **Create a .env file: In the root of the project, create a file named .env and add your environment variables from .env.sample:**
   ```bash
    SECRET_KEY=your-secret-key
    DEBUG=True
    OPENAI_API_KEY=your-openai-key
    ```
5. **Apply Migrations and Run Server**
    ```bash
    python manage.py migrate
    python manage.py runserver
    ```

