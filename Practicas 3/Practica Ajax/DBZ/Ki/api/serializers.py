from rest_framework import serializers
from Ki.models import Ki


class TweetModelSerializer(serializers.ModelSerializer):
    # user = UserDisplaySerializer(read_only=True)
	# date_display = serializers.SerializerMethodField()
	# timesince = serializers.SerializerMethodField()

	class Meta:
		model = Ki
		fields = [
			"id",
			"personaje",
			"raza",
			"nivelDePoder",
			"habilidad",
			# "date_display",
			# "timesince",
			]
	# def get_date_display(self, obj):
	# 	return obj.timestamp.strftime("%b %d %Y at %I: %M %p")
	#
	# def get_timesince(self, obj):
	# 	return timesince(obj.timestamp) + " " + "ago"
