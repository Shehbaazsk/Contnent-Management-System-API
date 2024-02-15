from rest_framework import serializers
from contents.models import Content,ContentCategory
from accounts.models import User

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','first_name']

class ContentCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentCategory
        fields = "__all__"


class ContentSerializer(serializers.ModelSerializer):
    category = ContentCategorySerializer(many=True)
    author = AuthorSerializer()
    class Meta:
        model = Content
        fields = "__all__"

        