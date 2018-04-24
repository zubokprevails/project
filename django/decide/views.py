# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect

from django.views.decorators.csrf import csrf_exempt

from django.db import connection

from .models import Employee

def index(request):
	return render(request, 'decide/index.html',)

@csrf_exempt
def add(request):
	if request.method=='POST':	
		name=request.POST['name']
		pwd=request.POST['pwd']		
		with connection.cursor() as cursor:
        		cursor.execute("insert into Employee(name,email) values(%s , %s );", [name, pwd])
		e = Employee.setdata(name,pwd)			
		e.save()
		return render(request, 'decide/login.html', {'e':e})
	

# Create your views here.