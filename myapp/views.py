from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse
from machbaseAPI.machbaseAPI import machbase

# Create your views here.

def hello(request):
    return HttpResponse(connect())

def connect():
    port = 5656
    db = machbase()
    if db.open('127.0.0.1','SYS','MANAGER',port) is 0 :
        return db.result()

    if db.execute('select count(*) from m$tables') is 0 :
        return db.result()

    result = db.result()

    if db.close() is 0 :
        return db.result()

    return result