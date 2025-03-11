from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from home.models import spherepost,sphereComment,recentUpdates
from home.serializers import SphereSerializer,SphereCommentsSerializer,RecentUpdateSerializer

class SphereAPIView(APIView):
    def get(self, request):
        sphere = spherepost.objects.all()
        serializer = SphereSerializer(sphere, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = SphereSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SphereCommentsAPIView(APIView):
    def get(self, request,sphere_id):
        spherecomments = sphereComment.objects.filter(post=sphere_id)
        serializer = SphereCommentsSerializer(spherecomments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = SphereCommentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RecentUpdateAPIView(APIView):
    def get(self, request):
        recupdates = recentUpdates.objects.all()
        serializer = RecentUpdateSerializer(recupdates, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
