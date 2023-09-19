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
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

class SkillDetail(APIView):
    def get(self, request, pk):
        skill = get_object_or_404(Skills, pk=pk)
        serializer = SkillSerializer(skill)
        return Response(serializer.data)

    def put(self, request, pk):
        skill = get_object_or_404(Skills, pk=pk)
        serializer = SkillSerializer(skill, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        skill = get_object_or_404(Skills, pk=pk)
        skill.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
