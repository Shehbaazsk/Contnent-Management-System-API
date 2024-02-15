from rest_framework import serializers
from .models import User
import re

class UserRegisterSerializers(serializers.ModelSerializer):    
    password = serializers.CharField(write_only=True, required=True)
    password2 = serializers.CharField(write_only=True, required=True, label="Password Confirmation")

    class Meta:
        model = User
        exclude = ['last_login']
        read_only_fields = ['id','user_role']
    
    def validate_password(self,value):
        if  not re.findall('[A-Z]',value):
            raise serializers.ValidationError("Password must contain 1 uppercase character")
        elif not re.findall('[a-z]',value):
            raise serializers.ValidationError("Password must contain 1 lowercase character")
        elif len(value)<8:
            raise serializers.ValidationError("Password length should be atleast 8")
        return value

    def validate_mobile_no(self,value):
        if 10 > len(str(value)) < 10 :
            raise serializers.ValidationError('Mobile number must be 10 digits')
        return value
    
    def validate_pincode(self, value):
        if 6 > len(str(value)) < 6:
            raise serializers.ValidationError('Pincode must be 6 digits')
        return value


    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        del attrs['password2']

        return attrs
    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'