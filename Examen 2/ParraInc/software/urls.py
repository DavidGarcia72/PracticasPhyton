from django.contrib import admin
from django.urls import path
# from home import views
from software import views

app_name="software"

urlpatterns = [
    path('',views.index, name="index_view"),
    path('createSoft',views.createSoft.as_view(), name="createSoft_view"),
    path('createDepa',views.createDepa.as_view(), name="createdepa_view"),
    path('listSoft',views.listSoft.as_view(), name="list_view"),
]
