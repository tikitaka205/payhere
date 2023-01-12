from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import LogSerializer
from rest_framework import status, permissions
from .models import Log
from rest_framework.generics import get_object_or_404


class LogAPIView(APIView):
    def get(self, request):
        """
        달력정보
        """
        logs=Log.objects.filter(author_id=request.user.id)
        serializer=LogSerializer(logs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """
        가계부 기록 남기기
        """
        serializer=LogSerializer(data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response("성공", status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LogDetailAPIView(APIView):
    def put(self, request, log_id):
        """
        로그수정
        """
        log=Log.objects.get(id=log_id)
        serializer=LogSerializer(log, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, log_id): #삭제
        log=get_object_or_404(Log, id=log_id)
        if request.user.id==log.id:
            log.delete()
            return Response("삭제완료",status=status.HTTP_204_NO_CONTENT)
        else:
            return Response("권한이 없습니다.", status=status.HTTP_403_FORBIDDEN)