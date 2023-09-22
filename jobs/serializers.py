from rest_framework import serializers
from .models import Jobs


class JobsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Jobs
        exclude = ('is_active',)

    def validate_title(self, value):
        if len(value) < 10:
            raise serializers.ValidationError(
                'Deve ter pelo menos 10 caracteres'
            )
        return value

    def validate_salary(self, value):
        if value < 1000:
            raise serializers.ValidationError(
                'O campo deve ser maior do que 1000'
            )
        return value

    def validate_description(self, value):
        if len(value) < 10:
            raise serializers.ValidationError(
                'Deve ter pelo menos 10 caracteres'
            )
        return value

    def validate_company(self, value):
        if len(value) < 3:
            raise serializers.ValidationError(
                'Deve ter pelo menos 3 caracteres'
            )
        return value
