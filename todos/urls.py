from django.conf.urls import url
from . import views
from django.urls import path
urlpatterns = [
	url(r'^$', views.index, name='index'),
	path('delete/<list_id>', views.delete, name="delete"),
	path('cross_off/<list_id>', views.cross_off, name="cross_off"),
	path('uncross/<list_id>', views.uncross, name="uncross"),
	path('edit/<list_id>', views.edit, name="edit"),
]