from django.contrib import admin
from django.urls import path
# from home import views
from investigacion import views

app_name="invest"

urlpatterns = [
    path('create/',views.createInvs.as_view(), name="createInvs_view"),
    path('index/',views.index, name="index_view"),
    path('buscar/',views.buscar, name="buscar_view"),
    path('ciCom/',views.listCiCom.as_view(), name="trabajoCiCom_view"),
    path('ciTi/',views.listCiTi.as_view(), name="trabajoCiTi_view"),
    path('ciNa/',views.listCiNa.as_view(), name="trabajoCiNa_view"),
    path('ciSo/',views.listCiSo.as_view(), name="trabajoCiSo_view"),
    path('ciMe/',views.listCiMe.as_view(), name="trabajoCiMe_view"),
]
