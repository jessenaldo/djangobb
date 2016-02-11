from django.conf.urls import patterns, url
from apps.travels import views
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',
	url(r'^$', login_required(views.Dashboard.as_view()), name="travels-dashboard"),
	url(r'^add$', login_required(views.Add.as_view()), name="travels-add"),
	url(r'^create$', login_required(views.Add.as_view()), name="travels-create"),
	url(r'^(?P<planid>[0-9]+)/join$', login_required(views.Join.as_view()), name="travels-join"),
	url(r'^(?P<planid>[0-9]+)/show$', login_required(views.Show.as_view()), name="travels-show"),
	)