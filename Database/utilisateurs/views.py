from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import CustomUserCreationForm
from .forms import CustomAuthenticationForm
from .models import UserProfile  # Import your UserProfile model
from django.contrib.auth import logout

def profile_view(request):
    if request.user.is_authenticated:
        user = request.user
        user_profile = UserProfile.objects.get(user=user)
        context = {
            'user_profile': user_profile,
        }
        return render(request, 'utilisateurs/profil.html', context)
    else:
        # Handle the case when the user is not logged in
        return render(request, 'not_logged_in.html')



from .models import UserProfile  # Importez votre modèle UserProfile

def inscription(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            # Créez un UserProfile pour le nouvel utilisateur inscrit
            UserProfile.objects.create(user=user)
            
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'utilisateurs/inscription.html', {'form': form})



def connexion(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            username = form.cleaned_data.get('username')
            user = authenticate(request, email=email, password=password, username=username)
            if user is not None:
                login(request, user)
                
                # Vérifiez si un UserProfile existe pour l'utilisateur, et créez-en un s'il n'existe pas
                user_profile, created = UserProfile.objects.get_or_create(user=user)
                
                return redirect('home')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'utilisateurs/connexion.html', {'form': form})

def custom_logout(request):
    logout(request)
    return redirect('accueil')




