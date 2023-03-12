from rest_framework import serializers
from .models import Form, FormHistory

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

class FormHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = FormHistory
        fields = (
            'id',
            'form',
            'sent_time',
            'establishments',
            


        )


