
from django.http import HttpResponse

import datetime

import cStringIO

def My_Homepage_view(request):
    return HttpResponse("swing.com")



def hello(request):
    return HttpResponse("Hello world")


def dealin(request):
    now = datetime.datetime.now()
    html = """<html><body><iframe src="https://docs.google.com/forms/d/1U0SW8MkBsIvi1BQByJLHkrijCEpDW3LnsHPIFivoDX4/viewform?embedded=true" width="800" height="1000" frameborder="0" marginheight="0" marginwidth="0"></iframe></body></html>"""
    return HttpResponse(html)



def cgckb(request):
    now = datetime.datetime.now()
    html = """<html><body><iframe src="https://docs.google.com/spreadsheet/ccc?key=0AlZnvpvCu761dEUyZkJiRHdSQlhWTmNTcmtGQ0JJYVE&usp=sharing" width="1600" height="1000" frameborder="0" marginheight="0" marginwidth="0"></iframe></body></html>"""
    return HttpResponse(html)



def cgin(request):
    now = datetime.datetime.now()
    html = """<html><body><iframe src="https://docs.google.com/forms/d/1lnKGI1tsJY6QYqWiU2LljLQ6PNOWuUC78ckHt4YFZNo/viewform?embedded=true" width="1600" height="1000" frameborder="0" marginheight="0" marginwidth="0">Loading...</iframe></body></html>"""
    return HttpResponse(html)

def cginv(request):
    now = datetime.datetime.now()
    html = """<html><body><iframe src="https://docs.google.com/spreadsheet/ccc?key=0Apf9w0x6momDdFItS0Ywa1lXWUUwQWFoRmZqQ3llUlE&usp=sharing" width="1600" height="1000" frameborder="0" marginheight="0" marginwidth="0">Loading...</iframe></body></html>"""
    return HttpResponse(html)


def lljhb(request):
    now = datetime.datetime.now()
    html = """<html><body><iframe src="https://docs.google.com/spreadsheet/ccc?key=0AlZnvpvCu761dHQxVjAwZktBQXRUTzd3WGdmZ1BSTGc&usp=sharing" width="1600" height="1000" frameborder="0" marginheight="0" marginwidth="0">Loading...</iframe></body></html>"""
    return HttpResponse(html)

def llchb(request):
    now = datetime.datetime.now()
    html = """<html><body><iframe src="https://docs.google.com/spreadsheet/ccc?key=0AlZnvpvCu761dDhpc25qT28xZGd2TFJMdm1zM0RjbFE&usp=sharing" width="1600" height="1000" frameborder="0" marginheight="0" marginwidth="0">Loading...</iframe></body></html>"""
    return HttpResponse(html)

def xjjjhb(request):
    now = datetime.datetime.now()
    html = """<html><body><iframe src="https://docs.google.com/spreadsheet/ccc?key=0AlZnvpvCu761dEQtdXN5QXg4UlI3QWVpeEh5dEtuNXc&usp=sharing" width="1600" height="1000" frameborder="0" marginheight="0" marginwidth="0">Loading...</iframe></body></html>"""
    return HttpResponse(html)

def xjjchb(request):
    now = datetime.datetime.now()
    html = """<html><body><iframe src="https://docs.google.com/spreadsheet/ccc?key=0AlZnvpvCu761dEtKTFYydlhBNVJPOFdMRDhNNG92V1E&usp=sharing" width="1600" height="1000" frameborder="0" marginheight="0" marginwidth="0">Loading...</iframe></body></html>"""
    return HttpResponse(html)



text = """<html><head></head><body topmargin = 100 leftmargin = 0><center><form method="get" action="/index/"> <font size="5">Search:</font><input type="text" name="a" value=""
style="width:350px; height:35px; font-size:20px" size="30"><input type="submit" value="GO"></form></center></body></html>"""

def index(request):
        return HttpResponse(text) 
