from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.db.models import Sum
from django.contrib import messages
from .models import Category, Expense

# Create your views here.

def expenses_summary(request):
    
    summary = Category.objects.annotate(
        total_amount=Sum('expenses__amount')
    ).values('name', 'total_amount')
    result = {}
    for category in summary:
        if category['total_amount'] is not None:
            result[category['name']] = float(category['total_amount'])
        else:
            result[category['name']] = 0
    
    return JsonResponse(result)

# below functions are used to add expenses and categories via HTML forms not mentioned in the task

def add_expenses(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        amount = request.POST.get('amount')
        category_id = request.POST.get('category_id')
        date = request.POST.get('date')
        
        try:
            category = Category.objects.get(id=category_id)
            expense = Expense.objects.create(
                title=title,
                amount=amount,
                category=category,
                date=date
            )
            return JsonResponse({'message': 'Expense added successfully', 'expense_id': expense.id})
        except Category.DoesNotExist:
            return JsonResponse({'error': 'Category does not exist'}, status=400)
    if request.method == 'GET':
        categories = Expense.objects.all().values('id', 'title' , 'amount', 'category__name', 'date')
        return JsonResponse({'expenses': list(categories)})
    return JsonResponse({'error': 'Invalid request method'}, status=405)

def add_category(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            category, created = Category.objects.get_or_create(name=name)
            if created:
                messages.success(request, f'Category "{name}" added successfully!')
            else:
                messages.warning(request, f'Category "{name}" already exists!')
        else:
            messages.error(request, 'Category name is required!')
        return redirect('add_category')
    
    categories = Category.objects.all()
    return render(request, 'add_category.html', {'categories': categories})

def add_expense_form(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        amount = request.POST.get('amount')
        category_id = request.POST.get('category_id')
        date = request.POST.get('date')
        
        if all([title, amount, category_id, date]):
            try:
                category = Category.objects.get(id=category_id)
                expense = Expense.objects.create(
                    title=title,
                    amount=amount,
                    category=category,
                    date=date
                )
                messages.success(request, f'Expense "{title}" added successfully!')
            except Category.DoesNotExist:
                messages.error(request, 'Selected category does not exist!')
            except Exception as e:
                messages.error(request, f'Error adding expense: {str(e)}')
        else:
            messages.error(request, 'All fields are required!')
        return redirect('add_expense_form')
    categories = Category.objects.all()
    expenses = Expense.objects.all().order_by('-date')
    return render(request, 'add_expense.html', {'categories': categories, 'expenses': expenses})