# Flask Application

A modern Flask web application with SQLAlchemy, Flask-Migrate, and Bootstrap frontend.

## Features

- **Application Factory Pattern**: Modular Flask application structure
- **Blueprint Architecture**: Organized code with separate blueprints for different features
- **Database Support**: SQLAlchemy ORM with Flask-Migrate for database migrations
- **Configuration Management**: Environment-based configuration (development/production)
- **Bootstrap UI**: Responsive frontend using Bootstrap 5
- **Multiple Pages**: Home, Dashboard, Login, Register, and Generator pages

## Project Structure

```
.
├── app/
│   ├── __init__.py                 # Application factory
│   ├── blueprints/                 # Application blueprints
│   │   ├── __init__.py
│   │   ├── auth/                   # Authentication blueprint
│   │   │   ├── __init__.py
│   │   │   └── routes.py
│   │   ├── generator/              # Generator blueprint
│   │   │   ├── __init__.py
│   │   │   └── routes.py
│   │   └── main/                   # Main blueprint
│   │       ├── __init__.py
│   │       └── routes.py
│   ├── static/                     # Static files
│   │   ├── css/
│   │   │   └── style.css
│   │   ├── js/
│   │   │   └── main.js
│   │   └── images/
│   └── templates/                  # HTML templates
│       ├── base.html
│       ├── index.html
│       ├── login.html
│       ├── register.html
│       ├── dashboard.html
│       └── generator.html
├── config/
│   ├── __init__.py
│   └── config.py                   # Configuration classes
├── .env.example                    # Example environment variables
├── requirements.txt                # Python dependencies
├── run.py                          # Application entry point
└── README.md                       # This file
```

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- virtualenv (recommended)

## Installation

1. **Clone the repository** (if applicable):
   ```bash
   git clone <repository-url>
   cd <project-directory>
   ```

2. **Create a virtual environment**:
   ```bash
   python3 -m venv venv
   ```

3. **Activate the virtual environment**:
   - On Linux/Mac:
     ```bash
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Set up environment variables**:
   ```bash
   cp .env.example .env
   ```
   
   Edit the `.env` file and configure your settings:
   ```
   FLASK_ENV=development
   SECRET_KEY=your-secret-key-here-change-in-production
   DATABASE_URL=sqlite:///app.db
   ```

6. **Initialize the database**:
   ```bash
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   ```

## Running the Application

### Development Mode

Run the application using the run script:

```bash
python run.py
```

Or use Flask's built-in development server:

```bash
export FLASK_APP=run.py
export FLASK_ENV=development
flask run
```

The application will be available at `http://localhost:5000`

### Production Mode

For production deployment, use a WSGI server like Gunicorn:

1. Install Gunicorn:
   ```bash
   pip install gunicorn
   ```

2. Run with Gunicorn:
   ```bash
   gunicorn -w 4 -b 0.0.0.0:8000 run:app
   ```

Make sure to set `FLASK_ENV=production` in your `.env` file.

## Database Migrations

When you make changes to your database models:

1. **Create a migration**:
   ```bash
   flask db migrate -m "Description of changes"
   ```

2. **Apply the migration**:
   ```bash
   flask db upgrade
   ```

3. **Rollback if needed**:
   ```bash
   flask db downgrade
   ```

## Configuration

The application supports different configurations based on the environment:

- **Development**: Debug mode enabled, SQLite database
- **Production**: Debug mode disabled, requires production database URL

Set the environment using the `FLASK_ENV` variable in your `.env` file.

## Available Routes

- `/` - Home page
- `/dashboard` - Dashboard page
- `/auth/login` - Login page
- `/auth/register` - Registration page
- `/auth/logout` - Logout endpoint
- `/generator/` - Generator page

## Development

### Adding a New Blueprint

1. Create a new directory in `app/blueprints/`
2. Add `__init__.py` with blueprint initialization
3. Add `routes.py` with your routes
4. Register the blueprint in `app/__init__.py`

### Adding Static Assets

- CSS files: `app/static/css/`
- JavaScript files: `app/static/js/`
- Images: `app/static/images/`

### Creating Templates

Templates should extend `base.html` and use Jinja2 template syntax.

## Testing

To run tests (when implemented):

```bash
python -m pytest
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License.

## Support

For issues and questions, please open an issue in the repository.
