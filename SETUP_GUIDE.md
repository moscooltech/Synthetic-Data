# Quick Setup Guide

## First Time Setup

1. **Create and activate virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment:**
   ```bash
   cp .env.example .env
   # Edit .env with your settings
   ```

4. **Initialize database:**
   ```bash
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   ```

5. **Run the application:**
   ```bash
   python run.py
   ```

6. **Access the application:**
   Open your browser and navigate to `http://localhost:5000`

## Project Components

### Blueprints
- **main**: Home page and dashboard (`/`, `/dashboard`)
- **auth**: Authentication routes (`/auth/login`, `/auth/register`, `/auth/logout`)
- **generator**: Generator functionality (`/generator/`)

### Templates
All templates extend `base.html` which includes:
- Bootstrap 5 navigation
- Flash message support
- Custom CSS and JavaScript
- Responsive design

### Static Assets
- **CSS**: `app/static/css/style.css`
- **JavaScript**: `app/static/js/main.js`
- **Images**: `app/static/images/`

### Configuration
- **Development**: Uses SQLite database, debug mode enabled
- **Production**: Requires DATABASE_URL, debug mode disabled

## Common Commands

```bash
# Run development server
python run.py

# Create database migration
flask db migrate -m "Description"

# Apply migrations
flask db upgrade

# Rollback migration
flask db downgrade

# Open Flask shell
flask shell
```

## Troubleshooting

### Module not found errors
Make sure your virtual environment is activated and dependencies are installed:
```bash
source venv/bin/activate
pip install -r requirements.txt
```

### Database errors
Initialize the database if you haven't:
```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

### Port already in use
Change the port in `run.py` or kill the process using port 5000:
```bash
# Linux/Mac
lsof -ti:5000 | xargs kill -9

# Or run on different port
python run.py --port 8000
```
