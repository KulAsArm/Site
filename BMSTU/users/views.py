from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate, logout
from django.template import loader
from django.http import HttpResponse
from .forms import UserRegisterForm, LoginForm, UserProfileForm, User
from django.db import transaction
from .models import Booking, Destinations


def user_dest(request):
    st_id = request.user.student.id
    books = Booking.objects.filter(student_id=st_id)
    dests_list = []
    for book in books:
        dests_list.append(book.destination_id)
    print(dests_list)
    info = []
    for dest_id in dests_list:
        dest = Destinations.objects.get(id=dest_id)
        info.append(f'{dest.name}: {dest.date}')
    return info

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
    return HttpResponse(template.render(context, request))


@transaction.atomic
def user_profile(request):
    if request.method == 'POST':
        student = UserProfileForm(request.POST, instance=request.user.student)
        if student.is_valid():
            print(request.path)
            idx = request.user.id
            email = request.user.email
            print(email)
            cd = student.cleaned_data
            cd['email'] = email
            user_change_profile = User.objects.get(id=idx)
            user_change_profile.student.FIO = cd['FIO']
            user_change_profile.student.email = cd['email']
            user_change_profile.student.group = cd['group']
            user_change_profile.student.phone = cd['phone']
            user_change_profile.student.names_of_priority = cd['names_of_priority']
            user_change_profile.student.telegram = cd['telegram']
            user_change_profile.save()
            return redirect('complited_profile')
        else:
            error = "Формат заполнения полей неверный"
            template = loader.get_template("users/profile.html")
            context = {'student': student, 'error': error}
            return HttpResponse(template.render(context, request))
    else:
        student = UserProfileForm()
    template = loader.get_template("users/profile.html")
    context = {'student': student}
    return HttpResponse(template.render(context, request))


@transaction.atomic
def user_complited_profile(request):
    temp_user = request.user.student
    dests = user_dest(request)
    cd = temp_user
    context = {'cd': cd, 'dests': dests}
    template = loader.get_template("users/complited_profile.html")
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
                error = 'Введен неправильный логин или пароль'
                err = loader.get_template('users/login.html')
                context = {'user': user, "err": error}
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


def user_delete(request):
    if request.method == 'POST':
        id = request.user.id
        user = User.objects.get(id=id)
        user.delete()
        return redirect('delete_done')
    else:
        template = loader.get_template("users/delete.html")
        context = {}
        return HttpResponse(template.render(context, request))


def user_delete_done(request):
    context = {}
    template = loader.get_template("users/delete_done.html")
    return HttpResponse(template.render(context, request))

