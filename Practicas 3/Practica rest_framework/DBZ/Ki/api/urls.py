
from django.urls import path
# from home import views
from Ki.api import views
app_name="api_ki"

urlpatterns = [
    path('list_tweet/',views.ListTweetAPIView.as_view(),name='listAPI_view')

]
