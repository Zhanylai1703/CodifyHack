from rest_framework import serializers
from .models import Form

class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Form
        fields = (
            'id',
            'name',
            'email',
            'establishments',
            'text_form',
            'data_time',
        )

