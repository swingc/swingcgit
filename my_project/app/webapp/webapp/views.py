from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.template import Context
import datetime

import cStringIO
def current_time(request):
	now = datetime.datetime.now()
	t = get_template('/srv/my_project/app/templates/current_time.html')
	html = t.render(Context({'current_date':now}))
	return HttpResponse(html)


def My_Homepage_view(request):
    return HttpResponse("swing.com")



def hello(request):
    return HttpResponse("Hello world")

 

def instockbaby(request):
    now = datetime.datetime.now()
    html = """<html><body><iframe src="https://docs.google.com/spreadsheet/ccc?key=0AlZnvpvCu761dEE4UXBsTGtUcUlSaTQyUmROS194aWc&usp=sharing" width="1000" height="800" frameborder="0" marginheight="0" marginwidth="0"></iframe></body></html>"""
    return HttpResponse(html)

def dealin(request):
    now = datetime.datetime.now()
    html = """<html><body><iframe src="https://docs.google.com/forms/d/1U0SW8MkBsIvi1BQByJLHkrijCEpDW3LnsHPIFivoDX4/viewform?embedded=true" width="800" height="1600" frameborder="0" marginheight="0" marginwidth="0"></iframe></body></html>"""
    return HttpResponse(html)

def dr(request):
    now = datetime.datetime.now()
    html = """<html><body><iframe src="https://docs.google.com/spreadsheet/ccc?key=0AlZnvpvCu761dG9sX1I0Tm5KZ3hLMG5KR2pUb19HMFE&usp=sharing" width="1250" height="800"  frameborder="0" marginheight="0" marginwidth="0"></iframe></body></html>"""
    return HttpResponse(html)

def cgckb(request):
    now = datetime.datetime.now()
    html = """<html><body><iframe src="https://docs.google.com/spreadsheet/ccc?key=0AlZnvpvCu761dEUyZkJiRHdSQlhWTmNTcmtGQ0JJYVE&usp=sharing" width="1600" height="800" frameborder="0" marginheight="0" marginwidth="0"></iframe></body></html>"""
    return HttpResponse(html)



def cgin(request):
    now = datetime.datetime.now()
    html = """<html><body><iframe src="https://docs.google.com/forms/d/1V7Bcos6dluQqBP9E45sVDBxMvFUhVoNcRMZMOqrjy3w/viewform?embedded=true" width="800" height="1000" frameborder="0" marginheight="0" marginwidth="0">Loading...</iframe></body></html>"""
    return HttpResponse(html)

def cginv(request):
    now = datetime.datetime.now()
    html = """<html><body><iframe src="https://docs.google.com/spreadsheet/ccc?key=0Apf9w0x6momDdFRHRmh0bzZzd0ZGS2lZVW13MWVYakE&usp=sharing" width="1600" height="800" frameborder="0" marginheight="0" marginwidth="0">Loading...</iframe></body></html>"""
    return HttpResponse(html)


def lljhb(request):
    now = datetime.datetime.now()
    html = """<html><body><iframe src="https://docs.google.com/spreadsheet/ccc?key=0AlZnvpvCu761dHQxVjAwZktBQXRUTzd3WGdmZ1BSTGc&usp=sharing" width="1600" height="800" frameborder="0" marginheight="0" marginwidth="0">Loading...</iframe></body></html>"""
    return HttpResponse(html)

def llchb(request):
    now = datetime.datetime.now()
    html = """<html><body><iframe src="https://docs.google.com/spreadsheet/ccc?key=0AlZnvpvCu761dDhpc25qT28xZGd2TFJMdm1zM0RjbFE&usp=sharing" width="1600" height="1000" frameborder="0" marginheight="0" marginwidth="0">Loading...</iframe></body></html>"""
    return HttpResponse(html)

def sjyjh(request):
    now = datetime.datetime.now()
    html = """<html><body><iframe src="https://docs.google.com/forms/d/1LU6-1tsECyiaSq1JzrTbgAs_ZPesm2ps0q9AdsVYrUg/viewform?embedded=true" width="760" height="1000" frameborder="0" marginheight="0" marginwidth="0">Loading...</iframe></body></html>"""
    return HttpResponse(html)


def sjyjhb(request):
    now = datetime.datetime.now()
    html = """<html><body><iframe src="https://docs.google.com/spreadsheet/ccc?key=0AlZnvpvCu761dEQtdXN5QXg4UlI3QWVpeEh5dEtuNXc&usp=sharing" width="1600" height="800" frameborder="0" marginheight="0" marginwidth="0">Loading...</iframe></body></html>"""
    return HttpResponse(html)
    
 
def sjych(request):
    now = datetime.datetime.now()
    html = """<html><body><iframe src="https://docs.google.com/forms/d/1ba4pS28e5MVnibkzLUaTYTGFUpfyMVCyr8L62utSG0w/viewform?embedded=true" width="760" height="1000" frameborder="0" marginheight="0" marginwidth="0">Loading...</iframe></body></html>"""
    return HttpResponse(html)


def sjychb(request):
    now = datetime.datetime.now()
    html = """<html><body><iframe src="https://docs.google.com/spreadsheet/ccc?key=0AlZnvpvCu761dEtKTFYydlhBNVJPOFdMRDhNNG92V1E&usp=sharing" width="1600" height="1000" frameborder="0" marginheight="0" marginwidth="0">Loading...</iframe></body></html>"""
    return HttpResponse(html)
    
    
def baojia(request):
    now = datetime.datetime.now()
    html = """<html><body><iframe src="https://docs.google.com/spreadsheets/d/1yS80jWkXkXZuYLOSzuesPeZKuoQgcEnOZXRkeNckMH8/edit?usp=sharing" width="1600" height="1000" frameborder="0" marginheight="0" marginwidth="0">Loading...</iframe></body></html>"""
    return HttpResponse(html)

def baojiabiao(request):
    now = datetime.datetime.now()
    html = """<html><body><iframe src="https://docs.google.com/forms/d/1P0YKbDlGq6AOhWmSfyJNQOlRwfnKD16abwWWoUWiOyA/viewform?embedded=true" width="760" height="800" frameborder="0" marginheight="0" marginwidth="0">Loading...</iframe></body></html>"""
    return HttpResponse(html)




def jipiao(request):
    now = datetime.datetime.now()
    html = """<html><body><iframe src="https://docs.google.com/spreadsheets/d/1MLuuPcB5Of71uXa-Evwyh0--AZxcZjzsKQbf71vw_0I/edit?usp=sharing" width="1600" height="800" frameborder="0" marginheight="0" marginwidth="0">Loading...</iframe></body></html>"""
    return HttpResponse(html)



def lishulink(request):
    now = datetime.datetime.now()
    html = """<html><body><iframe src="http://www.wuyoumall.com/stock/register/updatestock.php?id=kpf&ref=$H$9q/6cLaukg8N/RVQyX6vEAjURt0B3R/" width="1600" height="1000" frameborder="0" marginheight="0" marginwidth="0">Loading...</iframe></body></html>"""
    return HttpResponse(html)
    
    

def legolink(request):
    now = datetime.datetime.now()
    html = """<html><body><iframe src="http://www.wuyoumall.com/ctmcmx-store/stock.php?id=KPF&alias=$H$9Bn9/SXRI14k16viDpgk97ImoWdt7q/&display=all" width="1600" height="1000" frameborder="0" marginheight="0" marginwidth="0">Loading...</iframe></body></html>"""
    return HttpResponse(html)
 

text = """<html><head></head><body topmargin = 100 leftmargin = 0><center><form method="get" action="/index/"> <font size="5">Search:</font><input type="text" name="a" value=""
style="width:350px; height:35px; font-size:20px" size="30"><input type="submit" value="GO"></form></center></body></html>"""

def index(request):
        return HttpResponse(text) 
