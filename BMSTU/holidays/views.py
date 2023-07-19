from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.template import loader
from .models import Destinations
from users.models import Booking


def booking_create(request, dests):
    booking = Booking()
    booking.student_id = request.user.student.id
    booking.destination_id = dests.id
    booking.save()


def dest_update(date, name):
    dest = Destinations.objects.get(name=name, date=date[0])
    dest.occ_seats = dest.occ_seats + 1
    dest.save()
    return dest


def occ_part(dest):
    #функция считает процент занятых мест от общего количества
    occ = dest.occ_seats
    total = dest.tot_seats
    return int(100 * occ / total)


# def for_many_date(date, request, dest_name):
#     for i in date:
#         dest = dest_update(date, name=dest_name)
#
#         booking_create(request=request, dests=dest)
#
#     template = loader.get_template("holidays/booking2.html")
#     res = occ_part(dest)
#     context = {'seat_num': res}
#     return HttpResponse(template.render(context, request))

def index(request):
    template = loader.get_template("holidays/index.html")
    context = {'title': 'ГЛАВНАЯ СТРАНИЦА НАШЕГО САЙТА '}
    return HttpResponse(template.render(context, request))


def booking2(request):
    dest_name = 'СОЛ "Бауманец"'
    dest_date = ['2023-06-10', '2023-07-01', '2023-07-20']
    if request.method == 'POST':
        date = request.POST.getlist('date')
        if (date[0] in dest_date) and (len(date) == 1):
            dest = dest_update(date, name=dest_name)

            booking_create(request=request, dests=dest)

            template = loader.get_template("holidays/booking2.html")
            res = occ_part(dest)
            context = {'seat_num': res}
            return HttpResponse(template.render(context, request))
        # else:
        #     for_many_date(date=date, request=request, dest_date=dest_name)
        #
    else:
        template = loader.get_template("holidays/booking2.html")
        context = {}
        return HttpResponse(template.render(context, request))


def booking3(request):
    dest_name = 'СОЛ "КИТ"'
    dest_date = ['2023-06-16', '2023-07-01']
    if request.method == 'POST':
        date = request.POST.getlist('date')
        if (date[0] in dest_date) and (len(date) == 1):
            dest = dest_update(date, name=dest_name)

            booking_create(request=request, dests=dest)

            template = loader.get_template("holidays/booking3.html")
            res = occ_part(dest)
            context = {'seat_num': res}
            return HttpResponse(template.render(context, request))
    else:
        template = loader.get_template("holidays/booking3.html")
        context = {}
        return HttpResponse(template.render(context, request))


def booking4(request):
    dest_name = 'Пансионат "Сердоликовая бухта"'
    dest_date = ['2023-06-10', '2023-07-01']
    if request.method == 'POST':
        date = request.POST.getlist('date')
        if (date[0] in dest_date) and (len(date) == 1):
            dest = dest_update(date, name=dest_name)

            booking_create(request=request, dests=dest)

            template = loader.get_template("holidays/booking4.html")
            res = occ_part(dest)
            context = {'seat_num': res}
            return HttpResponse(template.render(context, request))
    else:
        template = loader.get_template("holidays/booking4.html")
        context = {}
        return HttpResponse(template.render(context, request))


def booking5(request):
    dest_name = 'Пансионат "Смена"'
    dest_date = ['2023-06-20', '2023-07-10']
    if request.method == 'POST':
        date = request.POST.getlist('date')
        if (date[0] in dest_date) and (len(date) == 1):
            dest = dest_update(date, name=dest_name)

            booking_create(request=request, dests=dest)

            template = loader.get_template("holidays/booking5.html")
            res = occ_part(dest)
            context = {'seat_num': res}
            return HttpResponse(template.render(context, request))
    else:
        template = loader.get_template("holidays/booking5.html")
        context = {}
        return HttpResponse(template.render(context, request))


def booking6(request):
    dest_name = 'СОЛ "Алушта"'
    dest_date = ['2023-07-01', '2023-07-20']
    if request.method == 'POST':
        date = request.POST.getlist('date')
        if (date[0] in dest_date) and (len(date) == 1):
            dest = dest_update(date, name=dest_name)

            booking_create(request=request, dests=dest)

            template = loader.get_template("holidays/booking6.html")
            res = occ_part(dest)
            context = {'seat_num': res}
            return HttpResponse(template.render(context, request))
    else:
        template = loader.get_template("holidays/booking6.html")
        context = {}
        return HttpResponse(template.render(context, request))


def booking7(request):
    dest_name = 'База отдыха "Охта"'
    dest_date = ['2023-06-10', '2023-07-01', '2023-08-20']
    if request.method == 'POST':
        date = request.POST.getlist('date')
        if (date[0] in dest_date) and (len(date) == 1):
            dest = dest_update(date, name=dest_name)

            booking_create(request=request, dests=dest)

            template = loader.get_template("holidays/booking7.html")
            res = occ_part(dest)
            context = {'seat_num': res}
            return HttpResponse(template.render(context, request))
    else:
        template = loader.get_template("holidays/booking7.html")
        context = {}
        return HttpResponse(template.render(context, request))


def booking8(request):
    dest_name = 'Кумысная поляна'
    dest_date = ['2023-08-10', '2023-08-20']
    if request.method == 'POST':
        date = request.POST.getlist('date')
        if (date[0] in dest_date) and (len(date) == 1):
            dest = dest_update(date, name=dest_name)

            booking_create(request=request, dests=dest)

            template = loader.get_template("holidays/booking8.html")
            res = occ_part(dest)
            context = {'seat_num': res}
            return HttpResponse(template.render(context, request))
    else:
        template = loader.get_template("holidays/booking8.html")
        context = {}
        return HttpResponse(template.render(context, request))


def booking(request):
    dest_name = 'Альплагерь Джан-Туган'
    dest_date = ['2023-07-15', '2023-08-01']
    if request.method == 'POST':
        date = request.POST.getlist('date')
        if (date[0] in dest_date) and (len(date) == 1):
            dest = dest_update(date, name=dest_name)

            booking_create(request=request, dests=dest)

            template = loader.get_template("holidays/booking.html")
            res = occ_part(dest)
            context = {'seat_num': res}
            return HttpResponse(template.render(context, request))
    else:
        template = loader.get_template("holidays/booking.html")
        context = {}
        return HttpResponse(template.render(context, request))


def aboutus(request):
    template = loader.get_template("holidays/abus.html")
    context = {}
    return HttpResponse(template.render(context, request))


def dest(request):
    template = loader.get_template("holidays/dest.html")
    context = {}
    return HttpResponse(template.render(context, request))

