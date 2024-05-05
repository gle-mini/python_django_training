import os
from django.conf import settings
from django.shortcuts import render, redirect
from django.utils import timezone
from .forms import InputForm

def get_history():
    try:
        with open(settings.LOG_FILE_PATH, 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        return []

def append_to_history(text):
    with open(settings.LOG_FILE_PATH, 'a') as file:
        timestamp = timezone.now().strftime('%Y-%m-%d %H:%M:%S')
        file.write(f"{timestamp} - {text}\n")

def index(request):
    form = InputForm()
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            input_text = form.cleaned_data['text_input']
            append_to_history(input_text)
            return redirect('index_ex02')

    history = get_history()
    return render(request, 'ex02/index.html', {'form': form, 'history': history})

