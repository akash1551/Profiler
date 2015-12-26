from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
import os
from django.contrib.auth.models import User
from details.models import Employee,Address


def employee(request):
	return render_to_response('employee_data.html')

def home(request):
	return render_to_response('home.html')