from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .serializers import RegisterSerializer

def register(request):
    if request.method == 'POST':
        serializer = RegisterSerializer(data=request.POST)
        if serializer.is_valid():
            user = serializer.save()
            # Return JSON response with user details (excluding password)
            return JsonResponse({
                'success': True,
                'message': 'User registered successfully!',
                'user': {
                    'id': user.id,
                    'username': user.username,
                    'email': user.email,
                    'date_joined': user.date_joined.isoformat(),
                    'is_active': user.is_active
                }
            })
        else:
            return JsonResponse({
                'success': False,
                'errors': serializer.errors
            }, status=400)
    return render(request, 'register.html')

def get_users(request):
    users = User.objects.all()
    if request.headers.get('Accept') == 'application/json' or request.GET.get('format') == 'json':
        users_data = []
        for user in users:
            users_data.append({
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'date_joined': user.date_joined.isoformat(),
                'is_active': user.is_active
            })
        return JsonResponse({'users': users_data})
    if not users:
        messages.info(request, "No users found.")
    return render(request, 'user_dashboard.html', {'users': users})

#get user by id
def get_user_detail(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.headers.get('Accept') == 'application/json' or request.GET.get('format') == 'json':
        return JsonResponse({
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'date_joined': user.date_joined.isoformat(),
            'is_active': user.is_active
        })
    return render(request, 'user_detail.html', {'user': user})

@csrf_exempt
@require_http_methods(["DELETE"])

def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    username = user.username
    user.delete()
    
    return JsonResponse({
        'message': f'User {username} (ID: {user_id}) deleted successfully',
        'deleted_user_id': user_id
    }, status=200)