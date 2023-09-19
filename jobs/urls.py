from django.urls import include, path
from .views import JobsList, JobsDetails


app_name = 'jobs'
urlpatterns = [
    path('', JobsList.as_view(), name='list'),
    path('<int:pk>', JobsDetails.as_view(), name='details')
]