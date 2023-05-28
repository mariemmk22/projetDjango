from multiprocessing import AuthenticationError
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from .models import *
from django.contrib import messages
from .forms import  UserRegistrationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login
from .forms import ProjectRequestForm, UserRegistrationForm



def accueil_view(request):
    portfolios = Portfolio.objects.all()
    services = Service.objects.all()
    equipes = equipe.objects.all()

    # Ajouter la vue 'view_personnel' pour chaque équipe dans le contexte
    context = {'portfolios': portfolios, 'services': services, 'equipes': equipes}

    for equipe_instance in equipes:
        context['personnel_' + str(equipe_instance.id)] = equipe_instance.Personnel.all()

    return render(request, 'ProfilArty/accueil.html', context)

# def services_view(request):
   
#     context = {'services': services}
#     return render(request, 'ProfilArty/services.html', context)

# def equipes_view(request):
   
#     context = {'equipes': equipes}
#     return render(request, 'ProfilArty/equipe.html', context)


def register(request):
    if request.method == 'POST' :
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request,user)
            messages.success(request, f'Coucou {username}, Votre compte a été créé avec succès !')
            return redirect('/login')
    else :
        form = UserCreationForm()
    return render(request,'account/register.html',{'form' : form})




def login(request):
    if request.method == "POST":
        form = AuthenticationError(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("../Protfolio")
            else:
                messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"login_form": form})


def logout(request):
    messages.info(request, "You have successfully logged out.") 
    return redirect("login")





def profil_view(request):
    if request.method == 'POST':
        form = ProjectRequestForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            start_date = form.cleaned_data['start_date']
            budget = form.cleaned_data['budget']
            new_project = Project(title=title, description=description, start_date=start_date, budget=budget)
            new_project.save()
            return render(request,'ProfilArty/success.html')
    else:
        form = ProjectRequestForm()
    
 
    projects = Project.objects.filter(status='achevé')
    projectsInPro = Project.objects.filter(status='en_cours')
    
    return render(request, 'ProfilArty/Profil.html', {'form': form, 'projects': projects,'projectsInPro': projectsInPro})
