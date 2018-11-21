from rest_framework import generics
from Ki.api.serializers import TweetModelSerializer
from Ki.models import Ki

class ListTweetAPIView(generics.ListAPIView):
    serializer_class = TweetModelSerializer

    def get_queryset(self, *args, **kwargs):
        return Ki.objects.all()
