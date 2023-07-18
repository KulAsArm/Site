from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Destinations


def index(request):
    template = loader.get_template("holidays/index.html")
    context = {'title': 'ГЛАВНАЯ СТРАНИЦА НАШЕГО САЙТА '}
    return HttpResponse(template.render(context, request))



def booking2(request):
    template = loader.get_template("holidays/booking2.html")
    dest = Destinations.objects.get(id=1)
    occ = dest.occ_seats
    tot = dest.tot_seats
    res = int((occ/tot)*100)
    context = {'seat_num':res }
    print(res)
    return HttpResponse(template.render(context, request))
def booking3(request):
    template = loader.get_template("holidays/booking3.html")
    dest=Destinations.objects.get(id=1)
    occ=dest.occ_seats
    tot=dest.tot_seats
    res=int((occ/tot)*100)
    context = {'seat_num':res }
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

