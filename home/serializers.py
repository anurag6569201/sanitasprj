from rest_framework import serializers
from home.models import spherepost,sphereComment,recentUpdates


class SphereSerializer(serializers.ModelSerializer):
    author_image = serializers.SerializerMethodField()
    author_name = serializers.SerializerMethodField()

    class Meta:
        model = spherepost
        fields = '__all__'

    def get_author_image(self, obj):
        if obj.author.sanitizer.is_verified:
            return obj.author.sanitizer.profile_image.url
        elif not obj.author.sanitizer.is_verified:
            return obj.author.userprofile.profile_image.url
        return None 
    
    def get_author_name(self, obj):
        if obj.author.sanitizer.is_verified:
            return obj.author.sanitizer.name
        elif not obj.author.sanitizer.is_verified:
            return obj.author.userprofile.name + " " + obj.author.userprofile.surname 
        return None


class SphereCommentsSerializer(serializers.ModelSerializer):
    author_image = serializers.SerializerMethodField()
    author_name = serializers.SerializerMethodField()
    class Meta:
        model = sphereComment
        fields = '__all__'

    def get_author_image(self, obj):
        if obj.author.sanitizer.is_verified:
            return obj.author.sanitizer.profile_image.url
        elif not obj.author.sanitizer.is_verified:
            return obj.author.userprofile.profile_image.url
        return None 
    
    def get_author_name(self, obj):
        if obj.author.sanitizer.is_verified:
            return obj.author.sanitizer.name
        elif not obj.author.sanitizer.is_verified:
            return obj.author.userprofile.name + " " + obj.author.userprofile.surname 
        return None

class RecentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = recentUpdates
        fields = '__all__'
