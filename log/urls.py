from django.urls import path, include
from . import views
from .views import LogAPIView, LogDetailAPIView

urlpatterns = [
    path('', LogAPIView.as_view(), name='log'),
    path('<int:log_id>/', LogDetailAPIView.as_view(), name='log_detail'),
    # path('s/', include('shortener.urls')),
    # path('', views.as_view(), name=''),
]