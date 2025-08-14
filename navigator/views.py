# navigator/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from .forms import RegisterForm
from .utils import shortest_path, GRAPH  # Keep your imports


# --------------------------
# User Registration
# --------------------------
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('map')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = RegisterForm()

    return render(request, 'navigator/register.html', {'form': form})


# --------------------------
# Map View
# --------------------------
@login_required
def map_view(request):
    """Render the map page with available blocks."""
    return render(request, 'navigator/map.html', {"blocks": list(GRAPH.keys())})


# --------------------------
# Shortest Path API
# --------------------------
@csrf_exempt
def find_path(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Invalid request'}, status=400)

    try:
        data = json.loads(request.body)
        start = data.get('start')
        end = data.get('end')
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)

    # Use actual BFS shortest_path from utils.py
    path = shortest_path(start, end)
    if not path:
        return JsonResponse({'error': 'No path found'}, status=404)

    # For now, simple distance = number_of_edges * 100 meters
    distance = (len(path) - 1) * 100

    return JsonResponse({
        'path': path,
        'distance': distance
    })


# --------------------------
# Login View
# --------------------------
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect

def loginView(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/map/')  # redirect to map after login
        else:
            return render(request, 'navigator/login.html', {'error': 'Invalid credentials'})
    return render(request, 'navigator/login.html')
# --------------------------
# Logout View
# --------------------------
@login_required
def logoutView(request):
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect('login')