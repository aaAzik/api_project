from rest_framework import serializers
from app.models import *

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'name',
            'username',
            'password',
        ]

        def get_image(self, obj):
            request = self.context.get('request')
            if obj.image:
                image = obj.image.url
                return request.build_absolute_uri(image)
            return None

class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
