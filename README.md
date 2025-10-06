# Zoi teckh Python Machine test 

Simple Django API for managing users and expenses.

## Setup

1. Clone the repository:
```bash
git clone https://github.com/hisham1665/zoi_test.git
cd zoi_test
```

2. Create and activate virtual environment:
```bash
python -m venv .venv
.venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Start server:
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