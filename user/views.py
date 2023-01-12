from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status, permissions
from rest_framework.response import Response
from .serializers import UserSerializer

class UserView(APIView):
    def post(self, request):
        serializer=UserSerializer(data=request.data)
        print("view",serializer)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "회원가입 완료."}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": "에러"}, status=status.HTTP_400_BAD_REQUEST)

