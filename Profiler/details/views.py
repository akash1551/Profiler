from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
import os
from django.contrib.auth.models import User
from details.models import Employee,Address,Skills
import json
from django.template import TemplateDoesNotExist


def add_data_page(request):
	return render_to_response('add_details.html')

"""def send_file_to_json(request):
	print request.POST
	id=2
	employee_obj=Employee.objects.get(id=id)
	employee_obj.thumbnail
	thumbnail=request.POST['file']
	thumbnail.save()"""

def save_data(request):
	print request.POST
	name=request.POST['name']
	address_line_1=request.POST['address_line_1']
	address_line_2=request.POST['address_line_2']
	city=request.POST['city']
	state=request.POST['state']
	pin_code=request.POST['pin_code']
	contact_no=request.POST['contact_no']
	skillset=request.POST['skillset']
	file=request.FILES['file']

	print name,address_line_1,address_line_2,city,state,pin_code,contact_no,skillset,file
	
	obj=Address(address_line_1=address_line_1,address_line_2=address_line_2,city=city,state=state,pin_code=pin_code)
	obj.save()
	
	skills_obj=Skills(skillset=skillset)
	skills_obj.save()


	detail=Employee(name=name,address=obj,contact_no=contact_no,thumbnail=file)
	detail.save()
	detail.skills.add(skills_obj)
	
	#return HttpResponse(json.dumps({"jason_obj": jason_obj}), content_type="application/json")

	return HttpResponseRedirect('/employee')

def save_json_data(request):
	print request.body
	json_obj=json.loads(request.body)
	print json_obj
	name=json_obj['name']
	address_line_1=json_obj['address_line_1']
	address_line_2=json_obj['address_line_2']
	city=json_obj['city']
	state=json_obj['state']
	pin_code=json_obj['pin_code']
	skillset=json_obj['skillset']
	contact_no=json_obj['contact_no']

	address_obj=Address(address_line_1=address_line_1,address_line_2=address_line_2,city=city,state=state,pin_code=pin_code)
	address_obj.save()
	
	skills_obj=Skills(skillset=skillset)
	skills_obj.save()

	employee_detail=Employee(name=name,address=address_obj,contact_no=contact_no,thumbnail=file)
	employee_detail.save()
	employee_detail.skillset.add(skills_obj)

	#file=request.FILES['file']
	json_details=json_obj(name=name,address=address_obj,skills=skills_obj,contact_no=contact_no)
	return render_to_response('')

def get_data_from_db(request):
	employee = Employee.objects.all()
	employee_list = []
	for i in employee:
		obj = {"name": i.name, "address_line_1": i.address.address_line_1, "address_line_2": i.address.address_line_2, "city": i.address.city, "state":i.address.state, "pin_code":i.address.pin_code, "contact_no": i.contact_no}
		employee_list.append(obj)

	print employee_list
	return render_to_response(json.dumps('templates/employee_data.html',{"employee_list": employee_list}))

