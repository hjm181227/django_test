from django.urls import path
from .views import BoardListCreateAPIView, BoardRetrieveUpdateDestroyAPIView


urlpatterns = [
    path('board/', BoardListCreateAPIView.as_view()),
    path('board/<int:board_pk>/', BoardRetrieveUpdateDestroyAPIView.as_view()),
]
