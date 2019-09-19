from django.shortcuts import render, HttpResponseRedirect, reverse, get_object_or_404
from .models import Profile
from .forms import RegisterForm, LoginForm, UpdateForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User


def homepage(request):
    return render(request, 'homepage.html')

def user_register(request):
    if not request.user.is_active:
        form = RegisterForm(data=request.POST or None)
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            faculty = form.cleaned_data.get('faculty')
            phone_number = form.cleaned_data.get('phone_number')

            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)
            user.save()

            Profile.objects.create(user=user)

            if user:
                if user.is_active:
                    login(request, user)
                    request.user.profile.faculty = faculty
                    request.user.profile.phone_number = phone_number
                    request.user.profile.save()
                    print(request.user.profile.faculty)
                    messages.success(request,
                                     '<b>Registiration has finished successfully. Welcome!</b>',
                                     extra_tags="success")
                    return HttpResponseRedirect(reverse('list-notes'))
    else:
        return HttpResponseRedirect(reverse('list-notes'))
    return render(request, 'users/register.html', context={'form': form})

def user_login(request):
    if not request.user.is_active:
        form = LoginForm(request.POST or None)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user:
                if user.is_active:
                    login(request, user)
                return HttpResponseRedirect(reverse('list-notes'))
    else:
        return HttpResponseRedirect(reverse('list-notes'))
    return render(request, 'users/login.html', context={'form': form})

def user_logout(request):
    logout(request)
    msg = "<b>You logged out. See you again, good bye!</b>"
    messages.success(request, msg, extra_tags="danger")

    return HttpResponseRedirect(reverse('list-notes'))

def who_we_are(request):
    return render(request, 'who-we-are/who-we-are.html')

def update_information(request, username):
    if request.user.is_active:
        user = get_object_or_404(User, username=username)
        form = UpdateForm(instance=user.profile, data=request.POST or None)

        if form.is_valid():
            phone_number = form.cleaned_data.get('phone_number', None)
            faculty = form.cleaned_data.get('faculty', None)

            user.profile.faculty = faculty
            user.profile.phone_number = phone_number
            user.profile.save()
            form.save()
            msg = "<b>Your information has updated successfully.</b>"
            messages.success(request, msg, extra_tags="success")
            return HttpResponseRedirect(reverse('user-settings', kwargs={'username':request.user.username}))
    else:
        return HttpResponseRedirect(reverse('list-notes'))
    return render(request, 'users/profile/settings.html', context={'user': user, 'form': form})
