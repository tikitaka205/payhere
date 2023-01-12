from rest_framework import serializers
from .models import User
import re

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=User
        fields='__all__'

    def validate_password(self, password):
        password_regex = '^(?=.*[a-zA-Z])((?=.*\d)(?=.*\W)).{8,16}$'
        if not re.search(password_regex, password):
            raise serializers.ValidationError(detail="비밀번호 8자 이상 16이하 영문, 숫자, 특수문자 하나 이상씩 포함해 주세요.")
        return password

    def validate_email(self, email):
        email_regex = '^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if not re.search(email_regex, email):
            raise serializers.ValidationError(detail="이메일 양식에 맞춰주세요")
        return email

    def create(self, validated_data):
        user  = super().create(validated_data)
        password = user.password
        user.set_password(password)
        user.save()
        return user