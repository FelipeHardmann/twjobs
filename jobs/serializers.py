from rest_framework import serializers
from .models import Jobs


class JobsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Jobs
        exclude = ('is_active',)
