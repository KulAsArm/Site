from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import AnonymousUser
from django.template import loader
from django.http import HttpResponse, Http404
from .forms import UserRegisterForm, LoginForm, UserProfileForm, User
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
        user_form = UserRegisterForm(request.POST, instance=request.user)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request, 'users/registration_done.html', {'new_user': new_user})
    else:
        user_form = UserRegisterForm(instance=request.user)
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


def user_profile(request):
    if request.method == 'POST':
        student = UserProfileForm(request.POST, instance=request.user.student)
        if student.is_valid():
            idx = student.id(request)
            user_change_profile = User.objects.get(id=idx)
            user_change_profile.student.FIO = student.FIO
            user_change_profile.student.email = student.email
            user_change_profile.student.group = student.group
            user_change_profile.student.phone = student.phone
            user_change_profile.save()
            return redirect('profile')
        else:
            error = "формат заполнения полей неверный"
            template = loader.get_template("users/profile.html")
            context = {'student': student, 'error': error}
            return HttpResponse(template.render(context, request))
    else:
        student = UserProfileForm()
    template = loader.get_template("users/profile.html")
    context = {'student': student}
    return HttpResponse(template.render(context, request))
    # return redirect('index/')


def user_profile_student(request):
    student = Student.objects.all()
    template = loader.get_template("users/student_profile.html")
    context = {'student': student}
    return HttpResponse(template.render(context, request))


def user_login(request):
    if request.method == 'POST':
        log_form = LoginForm(request.POST)
        if log_form.is_valid():
            cd = log_form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    log = loader.get_template('holidays/index.html')
                    return HttpResponse(log.render({}, request))
                else:
                    return HttpResponse('Disabled account')
            else:
                err = loader.get_template('users/login.html')
                context = {'user': user}
                return HttpResponse(err.render(context, request))
    else:
        log_form = LoginForm()
    template = loader.get_template('users/login.html')
    context = {'log_form': log_form}
    return HttpResponse(template.render(context, request))


def user_logout(request):
    logout(request)
    template = loader.get_template('users/logout.html')
    context = {}
    return HttpResponse(template.render(context, request))