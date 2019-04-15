from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import status
from rest_framework.response import Response
from .serializer import BoardSerializer
from .models import Board


class BoardListCreateAPIView(ListCreateAPIView):
    serializer_class = BoardSerializer
    queryset = Board.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class BoardRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = BoardSerializer
    lookup_url_kwarg = 'board_pk'

    def get_queryset(self):
        return Board.objects.filter(pk=self.kwargs['board_pk'])

    def update(self, request, *args, **kwargs):
        serializer_instance = self.get_object()
        serializer = self.get_serializer(serializer_instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
