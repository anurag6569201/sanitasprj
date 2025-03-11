from rest_framework import serializers
from home.models import spherepost,sphereComment,recentUpdates


class SphereSerializer(serializers.ModelSerializer):
    author_image = serializers.SerializerMethodField()

    class Meta:
        model = spherepost
        fields = '__all__'

    def get_author_image(self, obj):
        if obj.author.userprofile.profile_image:
            return obj.author.userprofile.profile_image.url
        return None 


class SphereCommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = sphereComment
        fields = '__all__'


class RecentUpdatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = recentUpdates
        fields = '__all__'
