from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Destinations
from users.models import Booking

count = 0

def index(request):
    template = loader.get_template("holidays/index.html")
    context = {'title': 'ГЛАВНАЯ СТРАНИЦА НАШЕГО САЙТА '}
    return HttpResponse(template.render(context, request))


def booking2(request):
    dest_date = ['2023-06-10', '01.07.23', '20.07.23']
    global count
    if request.method == 'POST':
        print('2')
        date = request.POST.getlist('date')
        ids = request.user.id
        print(ids)
        print(date)
        if date == [dest_date[0]]:
            dest = Destinations.objects.get(name='СОЛ "Бауманец"', date=date[0])
            print(f' its id: {dest.id}')
            count += 1
            dest.occ_seats = count
            dest.save()
            booking = Booking()
            booking.id_student = request.user.student.id
            booking.id_destination = dest.id
            booking.save()
            template = loader.get_template("holidays/booking2.html")
            occ = dest.occ_seats
            tot = dest.tot_seats
            res = int((occ / tot) * 100)
            context = {'seat_num': res}

            return HttpResponse(template.render(context, request))
    else:
        template = loader.get_template("holidays/booking2.html")
        context = {}
        return HttpResponse(template.render(context, request))


def booking3(request):
    template = loader.get_template("holidays/booking3.html")
    dest = Destinations.objects.get(id=1)
    occ = dest.occ_seats
    tot = dest.tot_seats
    res = int((occ/tot)*100)
    context = {'seat_num': res}
    print(res)
    return HttpResponse(template.render(context, request))
def booking4(request):
    template = loader.get_template("holidays/booking4.html")
    dest = Destinations.objects.get(id=1)
    occ = dest.occ_seats
    tot = dest.tot_seats
    res = int((occ/tot)*100)
    context = {'seat_num':res }
    print(res)
    return HttpResponse(template.render(context, request))
def booking5(request):
    template = loader.get_template("holidays/booking5.html")
    dest = Destinations.objects.get(id=1)
    occ = dest.occ_seats
    tot = dest.tot_seats
    res = int((occ/tot)*100)
    context = {'seat_num':res }
    print(res)
    return HttpResponse(template.render(context, request))
def booking6(request):
    template = loader.get_template("holidays/booking6.html")
    dest = Destinations.objects.get(id=1)
    occ = dest.occ_seats
    tot = dest.tot_seats
    res = int((occ/tot)*100)
    context = {'seat_num':res }
    print(res)
    return HttpResponse(template.render(context, request))
def booking7(request):
    template = loader.get_template("holidays/booking7.html")
    dest = Destinations.objects.get(id=1)
    occ = dest.occ_seats
    tot = dest.tot_seats
    res = int((occ/tot)*100)
    context = {'seat_num':res }
    print(res)
    return HttpResponse(template.render(context, request))
def booking8(request):
    template = loader.get_template("holidays/booking8.html")
    dest = Destinations.objects.get(id=1)
    occ = dest.occ_seats
    tot = dest.tot_seats
    res = int((occ/tot)*100)
    context = {'seat_num':res }
    print(res)
    return HttpResponse(template.render(context, request))
def booking(request):
    template = loader.get_template("holidays/booking.html")
    dest = Destinations.objects.get(id=1)
    occ = dest.occ_seats
    tot = dest.tot_seats
    res = int((occ/tot)*100)
    context = {'seat_num':res }
    print(res)
    return HttpResponse(template.render(context, request))



def aboutus(request):
    template = loader.get_template("holidays/abus.html")
    context = {}
    return HttpResponse(template.render(context, request))


def dest(request):
    template = loader.get_template("holidays/dest.html")
    context = {}
    return HttpResponse(template.render(context, request))

