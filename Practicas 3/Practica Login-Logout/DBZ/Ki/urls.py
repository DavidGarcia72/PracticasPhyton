from django.contrib import admin
from django.urls import path
# from home import views
from Ki import views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, logout_then_login
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
app_name="Ki"

urlpatterns = [
    path('accounts/login/',auth_views.LoginView.as_view(), name="login_view"),
    path('logout/', logout_then_login, name='logout'),
    path('registro/',views.RegistroUsuario.as_view(), name="registroUsuario_view"),
    path('list_tweets/',login_required(views.listTweets.as_view()), name="list_tweets_view"),
    path('detail/<int:pk>',login_required(views.detailTweets.as_view()), name="detail_tweets_view"),
    path('create/',login_required(views.Create.as_view()), name="create_view"),
    path('update/<int:pk>/',login_required(views.updateTweet.as_view()), name="update_view"),
    path('delete/<int:pk>/',login_required(views.deleteTweet.as_view()), name="delete_view"),
]
