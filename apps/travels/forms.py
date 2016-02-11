from django import forms
from apps.travels.models import Plan
from django.utils import timezone
from django.core.exceptions import ValidationError

class PlanForm(forms.Form):

	destination = forms.CharField(label="Destination")
	description = forms.CharField(label="Description", widget=forms.Textarea)
	date_from = forms.DateTimeField(label="Date From Ex:(10/25/2006)")
	date_to = forms.DateTimeField(label="Date To Ex:(10/25/2006)")

	def clean(self):
		
		
		if not self.cleaned_data.get('date_from'):
			raise ValidationError("No Date From")
		if not self.cleaned_data.get('date_to'):
			raise ValidationError("No Date To")


		if (self.cleaned_data.get('date_from') < timezone.now() ):
			print('validation error')
			raise ValidationError("Invalid Date From")

		#if the date from number is higher(more in the future) than date to number
		if (self.cleaned_data.get('date_to') < self.cleaned_data.get('date_from')):
			print('validation error')
			raise ValidationError("Invalid Date To")

		print(self.cleaned_data.get('date_to'))

		return self.cleaned_data

