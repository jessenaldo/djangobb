from django.conf.urls import url
from apps.users import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
	url(r'^$', views.Register.as_view(), name='users-register'),
	url(r'^login/$', views.Login.as_view(), name='users-login'),
	url(r'^logout/$', views.Logout.as_view(), name='users-logout'),
	]
