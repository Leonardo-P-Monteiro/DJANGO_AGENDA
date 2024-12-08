from django.shortcuts import render, redirect
from contact.forms import RegisterForm, RegisterUpdateForm
from django.contrib import messages, auth
from django.contrib.auth.forms import AuthenticationForm

def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'User create with success.')
            return redirect('contact:login')
    
    return render(
        request,
        'contact/user_update.html',
        {'form': form}
    )

def user_update(request):
    form = RegisterUpdateForm(instance= request.user)

    if request.method != "POST":
        return render(
            request,
            'contact/user_update.html',
            {'form': form}
        )
    
    form = RegisterUpdateForm(instance= request.user, data=request.POST)

    if not form.is_valid():
        return render(
            request,
            'contact/user_update.html',
            {'form': form}
        )

    form.save()
    messages.success(request, 'Update Success.')
    return redirect('contact:user_update')


def login_view(request):
    form = AuthenticationForm(request)

    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)

        if form.is_valid():
            messages.success(request, 'Log in success.')
            user = form.get_user()
            auth.login(request, user)
            return redirect('contact:index')

        messages.error(request, 'Log in error')

    return render(
        request,
        'contact/login.html',
        {'form': form}
    )

def logout_view(request):

    auth.logout(request)

    return redirect('contact:login')