# Mechanical Assignment Portal

A Flask web application designed for mechanical engineering students to submit assignment answers for manufacturing processes questionnaire.

## 📋 Project Overview

The Mechanical Assignment Portal is a web-based platform that allows students to:
- Register with their Student Registration Number (SRN)
- Login to access the assignment questionnaire
- Submit answers to 7 manufacturing process questions
- Ensure unique answers across all students (no duplicate answers allowed)

## 🎯 Features

### Student Management
- **User Registration**: Students register using their SRN and name
- **Secure Login**: Authentication based on SRN and password
- **Profile Management**: User data stored securely in database

### Assignment System
- **7-Question Format**: Covers key manufacturing processes:
  1. Rolling process Example
  2. Drop Forging Example
  3. Press Forging Example
  4. Upset Forging Example
  5. Extrusion process Example
  6. Wire Drawing Example
  7. Sheet Metal Operations Example

### Data Integrity
- **Unique Answer Validation**: Each answer must be unique across all students
- **Real-time Error Handling**: Immediate feedback for duplicate answers
- **Database Constraints**: PostgreSQL constraints ensure data integrity

## 🛠️ Technology Stack

### Backend
- **Flask 2.2.5**: Python web framework
- **SQLAlchemy 2.0.27**: Database ORM
- **Flask-WTF 1.2.1**: Form handling and validation
- **PostgreSQL**: Production database (with SQLite fallback for development)

### Frontend
- **HTML5/CSS3**: Modern responsive design
- **Bootstrap**: UI components and styling
- **JavaScript**: Client-side interactions and form validation

### Deployment
- **Gunicorn**: WSGI HTTP Server
- **Docker**: Containerization support
- **Cloud-Ready**: Configured for Google Cloud Platform deployment

## 📁 Project Structure

```
mechanical-assignment/
├── app.py                 # Flask application entry point
├── config.py             # Configuration settings
├── models.py             # Database models (User, Answer)
├── routes.py             # Application routes and views
├── forms.py              # WTForms for form validation
├── requirements.txt      # Python dependencies
├── Dockerfile           # Docker configuration
├── deploy-*.sh          # Deployment scripts
├── templates/           # HTML templates
│   ├── layout.html      # Base template
│   ├── index.html       # Landing page
│   ├── register.html    # Registration form
│   ├── login.html       # Login form
│   ├── main.html        # Assignment questionnaire
│   └── congrats.html    # Success page
├── static/              # Static assets
│   ├── style.css        # Custom styles
│   └── script.js        # JavaScript functionality
└── instance/            # Instance-specific files
    └── site.db          # SQLite database (development)
```

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- PostgreSQL (for production) or SQLite (for development)
- Git

### Local Development Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd mechanical-assignment
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Create a `.env` file:
   ```env
   SECRET_KEY=your-secret-key-here
   DATABASE_URL=sqlite:///site.db  # For development
   # DATABASE_URL=postgresql://user:pass@host:port/dbname  # For production
   ```

5. **Initialize the database**
   ```bash
   flask init-db
   ```

6. **Run the application**
   ```bash
   python app.py
   ```

   The application will be available at `http://localhost:5000`

## 🌐 Deployment Options

### Google Cloud Platform

#### Option 1: Cloud Run (Serverless)
```bash
./deploy-cloudrun.sh
```

#### Option 2: App Engine
```bash
./deploy-appengine.sh
```

### Other Platforms
- **Render**: Configured with `render.yaml`
- **Heroku**: Ready with `Procfile`
- **Docker**: Use included `Dockerfile`

## 🗄️ Database Schema

### User Table
- `srn` (Primary Key): Student Registration Number
- `name`: Student's full name
- `password`: Hashed password

### Answer Table
- `user_srn` (Primary Key, Foreign Key): References User.srn
- `answer1` to `answer7`: Text fields for each question response
- Unique constraints on each answer field to prevent duplicates

## 🔒 Security Features

- **Password Protection**: User authentication required
- **CSRF Protection**: Flask-WTF CSRF tokens
- **Data Validation**: Server-side form validation
- **Unique Constraints**: Database-level uniqueness enforcement
- **Error Handling**: Graceful error messages and recovery

## 📱 User Experience

### Registration Flow
1. Student enters SRN, name, and password
2. System validates SRN uniqueness
3. Account created successfully

### Assignment Flow
1. Student logs in with SRN and password
2. Accesses personalized questionnaire
3. Submits answers for all 7 questions
4. System validates answer uniqueness
5. Success confirmation displayed

### Error Handling
- Duplicate answer detection with specific field highlighting
- Clear error messages for user guidance
- Form state preservation during validation errors

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request


---

**Built with ❤️ for Mechanical Engineering Education**
