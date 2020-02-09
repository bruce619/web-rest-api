from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import AccountAuthenticationForm, UserRegisterForm, UserUpdateForm
from django.contrib.auth import login, authenticate, logout
import sweetify
import urllib.parse


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            account = authenticate(username=username, password=password)
            login(request, account)
            # Success message after submission
            sweetify.success(request, title='Account Created',
                             text=f'Your account has been created for {username}', icon='success',
                             button='Ok', timer=3000)
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')


def login_view(request):
    redirect_to = urllib.parse.unquote(request.GET.get('next', 'home'))
    form = AccountAuthenticationForm
    # Check if the form is a get method
    if request.method == "GET":
        context = {'form': form}
        return render(request, 'registration/login.html', context)
    user = request.user
    if user.is_authenticated:
        return redirect("home")

    if request.method == 'POST':
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                return redirect(redirect_to)

        else:
            form = AccountAuthenticationForm()

    return render(request, "registration/login.html", {'form': form})


@login_required(login_url='/login/')
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)

        if u_form.is_valid:
            u_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)

    context = {
            'u_form': u_form,
    }

    return render(request, 'profile.html', context)



