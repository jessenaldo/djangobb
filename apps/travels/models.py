from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Plan(models.Model):
	destination = models.CharField(max_length=90)
	description = models.TextField()
	date_from = models.DateTimeField()
	date_to = models.DateTimeField()
	created_by_user = models.ForeignKey(User, related_name='created_by_user')
	joined_users = models.ManyToManyField(User, related_name='joined_users')
	class Meta:
		db_table = 'plans'


