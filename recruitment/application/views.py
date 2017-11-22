from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from models import Application
import datetime
import recruitment.settings as settings
import json
#from django.views.decorators.csrf import csrf_protect

# Create your views here.
def check_session(func):
	#print "check_session"
	def check_username(request):
		try:
			if request.session['username']:
				return func(request)
			else:
				return admin(request)
		except Exception as e:
			print "Exception ", e
			return admin(request)

	return check_username

#@csrf_protect
@csrf_exempt
def application_form(request):
	if request.method == "GET":
		return render(request, "application/application.html",  {'error':'', 'success': ''})
	else:
		if len(Application.objects.filter(email= request.POST['email'])) == 0:
			new_user = Application.objects.create(
				first_name = request.POST['first_name'],
				last_name =  request.POST['last_name'],
				email =  request.POST['email'],
				position =  request.POST['position'],
				year_of_exp =  request.POST['yoe'],
				message =  request.POST['message'],
				app_status = "new",
				created_on = datetime.datetime.now()
				)
			new_user.save()
			return render(request, "application/application.html",  {'error':'', 'success': 'Application saved successfully '})
		else:
			return render(request, "application/application.html",  {'error':'Email already exists', 'success': ''})


@csrf_exempt
def admin(request):
	if request.method == "GET":
		return render(request, "application/login.html", {'error': ''})
	else:
		if request.POST['username'] == settings.ADMIN_USERNAME and request.POST['password'] == settings.ADMIN_PASSWORD:
			request.session['username'] = request.POST['username']
			return redirect('/dashboard')
		else:
			return render(request, "application/login.html", {'error': 'Please check the username and password'})

@check_session
def dashboard(request):
	count = {
			'new': Application.objects.filter(app_status='new').count() , 
			'accepted': Application.objects.filter(app_status='accepted').count() , 
			'rejected':Application.objects.filter(app_status='rejected').count() }
	users = Application.objects.all().order_by('created_on')[::-1]
	return render(request, "application/dashboard.html", {'count': count, 'users': users})

def users(request,status):
	users = Application.objects.filter(app_status=status).order_by('created_on')[::-1]
	return render(request, "application/users_list.html", {'users': users})

def user(request, user_id):
	user_id = int(user_id)
	user = Application.objects.get(id=user_id)
	return render(request, "application/user.html", {'user': user})



def logout(request):
	del request.session['username']
	return redirect('/admin')

@csrf_exempt
def update_status(request):
	user_id = int(request.POST['user_id'])
	user = Application.objects.get(id = user_id)
	user.app_status = request.POST['status']
	user.save()
	return HttpResponse(json.dumps({'status':"success"}))