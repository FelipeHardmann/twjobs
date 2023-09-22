from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Jobs
from .serializers import JobsSerializers


class JobsList(APIView):
    def get(self, request):
        jobs = Jobs.objects.filter(is_active=True)
        serializer = JobsSerializers(jobs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = JobsSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class JobsDetails(APIView):
    def __get_object(self, pk):
        return get_object_or_404(Jobs, pk=pk, is_active=True)

    def get(self, request, pk):
        job = self.__get_object(pk=pk)
        serializer = JobsSerializers(job)
        return Response(serializer.data)

    def put(self, request, pk):
        job = self.__get_object(pk=pk)
        serializer = JobsSerializers(job, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        job = self.__get_object(pk=pk)
        job.is_active = False
        job.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
