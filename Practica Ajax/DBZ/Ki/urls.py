from django.contrib import admin
from django.urls import path
# from home import views
from Ki import views

app_name="Ki"

urlpatterns = [
    # path('',views.index, name="index_view"),
    path('list_tweets/',views.listTweets.as_view(), name="list_tweets_view"),
    path('detail/<int:pk>',views.detailTweets.as_view(), name="detail_tweets_view"),
    path('create/',views.Create.as_view(), name="create_view"),
    path('update/<int:pk>/',views.updateTweet.as_view(), name="update_view"),
    path('delete/<int:pk>/',views.deleteTweet.as_view(), name="delete_view"),
]
