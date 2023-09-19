from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Skills
from .serializers import SkillSerializer
from rest_framework import status


class SkillList(APIView):
    def get(self, request):
        skills = Skills.objects.all()
        serializer = SkillSerializer(skills, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = SkillSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class SkillDetail(APIView):
    def get(self, request, pk):
        skill = get_object_or_404(Skills, pk=pk)
        serializer = SkillSerializer(skill)
        return Response(serializer.data)
