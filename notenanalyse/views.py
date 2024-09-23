from operator import truediv

from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout, user_login_failed
from django.urls import reverse
from .forms import UserSubjectForm, SymbolForm
from .models import Subject, Symbol, User_Subject


def user_is_logged_in_and_valid(request):
    if request.user and request.user.is_authenticated:
        return True
    else:
        return False


# Create your views here.

def index(request):
    return render(request, 'notenanalyse/index.html')

def login_user(request):
    L_Form = AuthenticationForm()

    if request.method == 'POST':
        L_Form = AuthenticationForm(data=request.POST)

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect(reverse('dashboard'))

    return render(request, 'notenanalyse/login.html', {'L_Form': L_Form})

def logout_user(request):
    logout(request)
    return redirect('index')

def register_user(request):
    R_Form = UserCreationForm()

    if request.method == 'POST':
        # print(request.POST)

        R_Form = UserCreationForm(request.POST)
        if R_Form.is_valid():
            R_Form.save()

            name = R_Form.cleaned_data['username']
            password = R_Form.cleaned_data['password1']
            user = authenticate(request, username=name, password=password)
            if user:
                login(request, user)
                return redirect(reverse('notenanalyse:dashboard'))

    return render(request, 'notenanalyse/register.html', {'R_Form': R_Form})

def dashboard(request):
    if user_is_logged_in_and_valid(request): return render(request, './notenanalyse/dashboard.html', {'user': request.user})
    else: return redirect('login')

def subjects(request):
    if user_is_logged_in_and_valid(request):
        subjects_list = Subject.objects.all()
        return render(request, './notenanalyse/subjects/index.html', {'subjects': subjects_list})
    else: return redirect('login')

def show_subject(request):
    if user_is_logged_in_and_valid(request):
        subject_id = request.GET.get('id')
        user_subject = User_Subject.objects.get(pk=subject_id)
        if user_subject:
            return render(request, './notenanalyse/subjects/show.html', {'subject': user_subject})

def delete_subjects(request):
    if user_is_logged_in_and_valid(request):
        subject_id = request.GET.get('id')
        if subject_id:
            user_subject = User_Subject.objects.filter(id=subject_id).get()
            if user_subject.user_id == request.user.id:
                user_subject.delete()
                User_Subject.save()
        return redirect('subjects')


def create_subject(request):
    if request.user:
        subject_form = UserSubjectForm()
        if request.user.is_authenticated: return render(request, './notenanalyse/subjects/create.html', {'form': subject_form})
        else: return redirect('login')
    return redirect('login')

def symbols(request):
    if request.user:
        symbol_list = Symbol.objects.all()
        if request.user.is_authenticated: return render(request, './notenanalyse/icons/index.html', {'symbols': symbol_list})
        else: return redirect('login')
    return redirect('login')

def create_symbol(request):
    if request.user and request.user.is_authenticated:

        symbol_form = SymbolForm()

        if request.method == 'POST':
            symbol_form = SymbolForm(request.POST)
            if symbol_form.is_valid():
                symbol_form.save()
                return render(request, './notenanalyse/icons/index.html', {'form': symbol_form})
        else:
            return render(request, './notenanalyse/icons/create.html', {'form': symbol_form})
    return redirect('login')
