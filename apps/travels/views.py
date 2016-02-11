from django.shortcuts import render, redirect
from django.views.generic import View
from django.views.generic.base import TemplateView
from apps.travels.models import Plan
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from apps.travels.forms import PlanForm
from django.db.models import Q

# Create your views here.
class Dashboard(View):
	
	def get(self, request):

	
		myplans = Plan.objects.filter(Q(created_by_user=request.user.id) | Q(joined_users=request.user.id))
		
		otherplans = Plan.objects.exclude(Q(created_by_user=request.user.id) | Q(joined_users=request.user.id))

		context = {
			'myplans': myplans,
			'otherplans': otherplans,
		}

		return render(request, 'travels/dashboard.html', context)

class Add(View):
	def get(self, request):

		form = PlanForm()

		context = {
			'form': form,
		}


		return render(request, 'travels/add.html', context)
	def post(self, request):

		form = PlanForm(request.POST or None)
		if form.is_valid():

			user = User.objects.get(id=request.user.id)

			plan = Plan(destination=form.cleaned_data['destination'], description=form.cleaned_data['description'], date_from=form.cleaned_data['date_from'], date_to=form.cleaned_data['date_to'], created_by_user=user)

			plan.save()

			return HttpResponseRedirect('/travels')

		context = {
			'form': form,
		}

		return render(request, 'travels/add.html', context)

class Join(View):
	def get(self, request, planid):

		plan = Plan.objects.get(id=planid)
		user = User.objects.get(id=request.user.id)

		plan.joined_users.add(user)

		return HttpResponseRedirect('/travels')

class Show(View):
	def get(self, request, planid):

		plan = Plan.objects.get(id=planid)

		context = {
			'plan': plan,
		}

		return render(request, 'travels/show.html', context)
