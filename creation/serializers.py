from rest_framework import serializers
from creation.models import Post

class BlogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
