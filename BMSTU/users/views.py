from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import AnonymousUser
from django.template import loader
from django.http import HttpResponse, Http404
from .forms import UserRegisterForm, LoginForm
from django.contrib import messages


# def registration(request):
#     if request.method == 'POST':
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request, f"Аккаунт {username} создан, пожалуйста, посетите личный кабинет на сайте.")
#             return redirect('login')
#     else:
#         form = UserRegisterForm()
#     template = loader.get_template('users/registration.html')
#     context = {'form': form}
#     # return render(request, 'users/regr.html', {'form': form})
#     return HttpResponse(template.render(context, request))


def registration(request):
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request, 'users/registration_done.html', {'new_user': new_user})
    else:
        user_form = UserRegisterForm()
    template = loader.get_template('users/registration.html')
    context = {'user_form': user_form}
    #     # return render(request, 'users/regr.html', {'form': form})
    return HttpResponse(template.render(context, request))
    # return render(request, 'users/registration.html', {'user_form': user_form})

# def registration(request):
#     if request.method == 'GET':
#         user_form = UserRegisterForm()
#         return render(request, 'users/registration.html', {'form': user_form})
#     if request.method == "POST":
#         user_form = UserRegisterForm(request.POST)
#         if user_form.is_valid():
#             user = user_form.save(commit=False)
#             user.username = user.username.lower()
#             user.save()
#             messages.success(request, "Вы успешно зарегистрировались. Разрегистрируйтесь живо.")
#             login(request, user)
#             return redirect('posts')
#         else:
#             return render(request, 'users/registration.html', {'user_form': user_form})


def user_profile(req):
    # if AnonymousUser.is_anonymous:
    #     log = loader.get_template("users/login.html")
    #     context = {}
    #     return HttpResponse(log.render(context, req))
    # else:
    template = loader.get_template("users/profile.html")
    context = {}
    return HttpResponse(template.render(context, req))


def user_login(req):
    if req.method == 'POST':
        log_form = LoginForm(req.POST)
        if log_form.is_valid():
            cd = log_form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(req, user)
                    log = loader.get_template('users/profile.html')
                    return HttpResponse(log.render({}, req))
                else:
                    return HttpResponse('Disabled account')
            else:
                err = loader.get_template('users/login.html')
                context = {'user': user}
                return HttpResponse(err.render(context, req))
    else:
        log_form = LoginForm()
    template = loader.get_template('users/login.html')
    context = {'log_form': log_form}
    return HttpResponse(template.render(context, req))


def user_logout(req):
    logout(req)
    template = loader.get_template('users/logout.html')
    context = {}
    return HttpResponse(template.render(context, req))