from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from core.paginations import TwJobsPagination

from .models import Jobs
from .serializers import JobsSerializers

from .filters import JobFilterSet


class JobsList(APIView):
    def get(self, request):
        paginator = TwJobsPagination()
        query_set = Jobs.objects.filter(is_active=True)
        filter = JobFilterSet(request.GET, query_set)
        jobs = paginator.paginate_queryset(filter.qs, request)
        serializer = JobsSerializers(jobs, many=True)
        return paginator.get_paginated_response(serializer.data)

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
