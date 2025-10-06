# Zoi techk Python Machine test 

Simple Django API for managing users and expenses.

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

3. Start server:
```bash
python manage.py runserver
```

## API Endpoints

### Users

**GET /users/?format=json** - List all users
```json
{"users": [{"id": 1, "username": "john", "email": "john@example.com"}]}
```

**GET /users/1/?format=json** - Get user by ID
```json
{"id": 1, "username": "john", "email": "john@example.com", "is_active": true}
```

**DELETE /users/1/delete/** - Delete user
```json
{"message": "User john (ID: 1) deleted successfully"}
```

### Expenses

**GET /expenses/summary/** - Expense totals by category
```json
{"Food": 1200.00, "Travel": 3000.00, "Entertainment": 800.00}
```

## Web Forms

- `/register/` - User registration
- `/categories/add/` - Add expense categories  
- `/expenses/add/` - Add expenses