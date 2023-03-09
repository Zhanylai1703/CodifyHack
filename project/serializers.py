from rest_framework import serializers
from .models import Establishments, Category, QA


class EstablishmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Establishments
        fields = ('id', 
                  'title',
                  'subtitle',
                  'photo',
                  'location'
                  )
        

class CategorySerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ('id', 
                  'name', 
                  'parent', 
                  'children'
                  )
        
    def get_children(self, obj):
        if obj.is_leaf_node():
            return None
        serializer = self.__class__(obj.get_children(), many=True)
        return serializer.data

class QASerializer(serializers.ModelSerializer):
    class Meta:
        model = QA
        fields = ('id', 
                  'question', 
                  'answer', 
                  'category'
                  )
