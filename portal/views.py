from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ReminderForm, feedbackForm, RegisterForm
from .models import tasks, Reminder

def home(request):
    return render(request, 'home.html')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})


@login_required
def dashboard(request):
    return render(request, 'dashboard.html')


@login_required
def tasks(request):
    data = tasks.objects.all()
    return render(request, 'tasks.html', {'tasks': data})


@login_required
def solution(request):
    return render(request, 'solution.html')


@login_required
def reminders(request):
    reminders = Reminder.objects.all()

    if request.method == 'POST':
        form = ReminderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reminders')
    else:
        form = ReminderForm()

    return render(request, 'reminders.html', {
        'form': form,
        'reminders': reminders
    })


@login_required
def feedback(request):
    if request.method == 'POST':
        form = feedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('feedback')
    else:
        form = feedbackForm()

    return render(request, 'feedback.html', {'form': form})