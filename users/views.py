from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST) # changed this with django's default UserCreationForm since I also want to add email on registration
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
        # else:
        #     messages.error(request, 'pass again.')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required    # FBV decorator making sure user is logged in to get access to /profile/, make sure to add LOGIN_URL = 'login' in the settings.py too. Otherwise the default is accounts/login
def profile(request):
    u_form = UserUpdateForm()
    p_form = ProfileUpdateForm()

    context = {
        "u_form": u_form,
        "p_form": p_form,
    }

    return render(request, 'users/profile.html', context)
