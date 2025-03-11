from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from creation.models import Post
from creation.serializers import BlogsSerializer

class BlogsAPIView(APIView):
    def get(self, request):
        Blogs = Post.objects.all()
        serializer = BlogsSerializer(Blogs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = BlogsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
