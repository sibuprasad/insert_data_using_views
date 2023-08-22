from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from app1.models import *

def insert_topic(request):
    tn=input('Enter topic_name: ')
    to=Topic.objects.get_or_create(topic_name=tn)[0]
    to.save()
    return HttpResponse('Data Inserted')

def insert_webpage(request):
    tn=input("Enter topic_name: ")
    to=Topic.objects.get_or_create(topic_name=tn)[0]
    to.save()
    n=input("Enter name: ")
    u=input("Enter url: ")
    wo=Webpage.objects.get_or_create(topic_name=to,name=n,url=u)[0]
    wo.save()
    return HttpResponse("Data Inserted")

def insert_accessrecord(request):
    tn=input("enter topic_name: ")
    to=Topic.objects.get_or_create(topic_name=tn)[0]
    to.save()
    n=input("Enter name: ")
    u=input("Enter url: ")
    wo=Webpage.objects.get_or_create(topic_name=to,name=n,url=u)[0]
    wo.save()
    d=input("Enter date: ")
    a=input("Enter author: ")
    e=input("enter mailid: ")
    ao=AccessRecord.objects.get_or_create(name=wo,date=d,author=a,email=e)[0]
    ao.save()
    return HttpResponse("Data Inserted")