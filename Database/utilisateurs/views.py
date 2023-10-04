from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import CustomUserCreationForm
from .forms import CustomAuthenticationForm
from .models import UserProfile  # Import your UserProfile model
from django.contrib.auth import logout

from django.shortcuts import render
from .models import UserProfile

def profile_view(request):
    if request.user.is_authenticated:
        user = request.user
        user_profile = UserProfile.objects.filter(user=user).first()
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
            return redirect('homes')
    else:
        form = CustomUserCreationForm()
    return render(request, 'utilisateurs/connexion.html', {'form': form})



def connexion(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            
            password = form.cleaned_data.get('password')
            username = form.cleaned_data.get('username')
            user = authenticate(request, password=password, username=username)
            if user is not None:
                login(request, user)
                
                # Vérifiez si un UserProfile existe pour l'utilisateur, et créez-en un s'il n'existe pas
                user_profile, created = UserProfile.objects.get_or_create(user=user)
                
                return redirect('homes')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'utilisateurs/connexion.html', {'form': form})

def custom_logout(request):
    logout(request)
    return redirect('accueil')


def custom_404(request, exception):
    return render(request, 'Database/404.html', status=404)


