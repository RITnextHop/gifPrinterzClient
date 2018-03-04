from .models import *
from django.shortcuts import render, redirect
from .forms import *

def Index(request):
    if request.method == 'POST':
        form = gifForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    data = { 'form': gifForm(), 'uploads': Upload.objects.all() }
    return render(request, 'index.html', data)
