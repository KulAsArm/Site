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


def views_occ(date, dest_name):
    # функция считает процент занятых мест от общего количества
    dest = Destinations.objects.get(name=dest_name, date=date)
    occ = dest.occ_seats
    total = dest.tot_seats
    per = f'{occ} / {total}'
    return (int(100 * occ / total), per)


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
            res = views_occ(date=dest_date[0], dest_name=dest_name)
            res2 = views_occ(date=dest_date[1], dest_name=dest_name)
            res3 = views_occ(date=dest_date[2], dest_name=dest_name)
            context = {'seat_num2': res2[0], 'seat_num3': res3[0], 'seat_num': res[0], 'per': res[1], 'per2': res2[1], 'per3': res3[1]}
            return HttpResponse(template.render(context, request))
    else:
        res = views_occ(date=dest_date[0], dest_name=dest_name)
        res2 = views_occ(date=dest_date[1], dest_name=dest_name)
        res3 = views_occ(date=dest_date[2], dest_name=dest_name)
        template = loader.get_template("holidays/booking2.html")
        context = {'seat_num2': res2[0], 'seat_num3': res3[0], 'seat_num': res[0], 'per': res[1], 'per2': res2[1], 'per3': res3[1]}
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

            res = views_occ(date=dest_date[0], dest_name=dest_name)
            res2 = views_occ(date=dest_date[1], dest_name=dest_name)

            context = {'seat_num2': res2[0], 'seat_num': res[0], 'per': res[1], 'per2': res2[1]}
            return HttpResponse(template.render(context, request))
    else:
        res = views_occ(date=dest_date[0], dest_name=dest_name)
        res2 = views_occ(date=dest_date[1], dest_name=dest_name)

        template = loader.get_template("holidays/booking3.html")
        context = {'seat_num2': res2[0], 'seat_num': res[0], 'per': res[1], 'per2': res2[1]}
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

            res = views_occ(date=dest_date[0], dest_name=dest_name)
            res2 = views_occ(date=dest_date[1], dest_name=dest_name)

            context = {'seat_num2': res2[0], 'seat_num': res[0], 'per': res[1], 'per2': res2[1]}
            return HttpResponse(template.render(context, request))
    else:
        template = loader.get_template("holidays/booking4.html")

        res = views_occ(date=dest_date[0], dest_name=dest_name)
        res2 = views_occ(date=dest_date[1], dest_name=dest_name)

        context = {'seat_num2': res2[0], 'seat_num': res[0], 'per': res[1], 'per2': res2[1]}
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

            res = views_occ(date=dest_date[0], dest_name=dest_name)
            res2 = views_occ(date=dest_date[1], dest_name=dest_name)

            context = {'seat_num2': res2[0], 'seat_num': res[0], 'per': res[1], 'per2': res2[1]}
            return HttpResponse(template.render(context, request))
    else:
        template = loader.get_template("holidays/booking5.html")

        res = views_occ(date=dest_date[0], dest_name=dest_name)
        res2 = views_occ(date=dest_date[1], dest_name=dest_name)

        context = {'seat_num2': res2[0], 'seat_num': res[0], 'per': res[1], 'per2': res2[1]}
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

            res = views_occ(date=dest_date[0], dest_name=dest_name)
            res2 = views_occ(date=dest_date[1], dest_name=dest_name)

            context = {'seat_num2': res2[0], 'seat_num': res[0], 'per': res[1], 'per2': res2[1]}
            return HttpResponse(template.render(context, request))
    else:
        template = loader.get_template("holidays/booking6.html")

        res = views_occ(date=dest_date[0], dest_name=dest_name)
        res2 = views_occ(date=dest_date[1], dest_name=dest_name)

        context = {'seat_num2': res2[0], 'seat_num': res[0], 'per': res[1], 'per2': res2[1]}
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

            res = views_occ(date=dest_date[0], dest_name=dest_name)
            res2 = views_occ(date=dest_date[1], dest_name=dest_name)
            res3 = views_occ(date=dest_date[2], dest_name=dest_name)
            context = {'seat_num2': res2[0], 'seat_num3': res3[0], 'seat_num': res[0], 'per': res[1], 'per2': res2[1], 'per3': res3[1]}
            return HttpResponse(template.render(context, request))
    else:
        template = loader.get_template("holidays/booking7.html")
        res = views_occ(date=dest_date[0], dest_name=dest_name)
        res2 = views_occ(date=dest_date[1], dest_name=dest_name)
        res3 = views_occ(date=dest_date[2], dest_name=dest_name)
        context = {'seat_num2': res2[0], 'seat_num3': res3[0], 'seat_num': res[0], 'per': res[1], 'per2': res2[1], 'per3': res3[1]}
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

            res = views_occ(date=dest_date[0], dest_name=dest_name)
            res2 = views_occ(date=dest_date[1], dest_name=dest_name)

            context = {'seat_num2': res2, 'seat_num': res}
            return HttpResponse(template.render(context, request))
    else:
        template = loader.get_template("holidays/booking8.html")

        res = views_occ(date=dest_date[0], dest_name=dest_name)
        res2 = views_occ(date=dest_date[1], dest_name=dest_name)

        context = {'seat_num2': res2, 'seat_num': res}
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

            res = views_occ(date=dest_date[0], dest_name=dest_name)
            res2 = views_occ(date=dest_date[1], dest_name=dest_name)

            context = {'seat_num2': res2[0], 'seat_num': res[0], 'per': res[1], 'per2': res2[1]}
            return HttpResponse(template.render(context, request))
    else:
        template = loader.get_template("holidays/booking.html")

        res = views_occ(date=dest_date[0], dest_name=dest_name)
        res2 = views_occ(date=dest_date[1], dest_name=dest_name)

        context = {'seat_num2': res2[0], 'seat_num': res[0], 'per': res[1], 'per2': res2[1]}
        return HttpResponse(template.render(context, request))


def aboutus(request):
    template = loader.get_template("holidays/abus.html")
    context = {}
    return HttpResponse(template.render(context, request))


def dest(request):
    template = loader.get_template("holidays/dest.html")
    context = {}
    return HttpResponse(template.render(context, request))

