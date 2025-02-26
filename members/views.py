from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member
from django.db.models import Q

def members(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    mymember = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'mymember': mymember,
    }
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def technology(request):
    template = loader.get_template('mytemplate.html')
    return HttpResponse(template.render())

def quantum(request):
    template = loader.get_template("quantum.html")
    return HttpResponse(template.render())

from django.http import HttpResponse
from django.template import loader

def testing(request):
    mymembers = Member.objects.all().order_by('lastname', '-id').values()
    template = loader.get_template('template.html')
    context = {
    'mymembers': mymembers,
    'greeting': 5,
    'day': 'Friday',
        'cars': [
        {
        'brand': 'Ford',
        'model': 'Mustang',
        'year': '1964',
        },
        {
        'brand': 'Ford',
        'model': 'Bronco',
        'year': '1970',
        },
        {
        'brand': 'Volvo',
        'model': 'P1800',
        'year': '1964',
        }]
    }
    return HttpResponse(template.render(context, request)) 