from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.serializers import TokenRefreshSerializer
from rest_framework import filters, generics, status
from .serializers import (
    MyTokenObtainPairSerializer, CreateTodoSerializer,
    ListTodoSerializer, UpdateTodoSerializer
)
from ..models import Todo
from rest_framework.exceptions import ValidationError, NotFound

""" Login View extend from TokenObtainPairView and use MyTokenObtainPairSerializer to customize information"""
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


"""Get token by refresh token"""
class CustomTokenRefreshView(TokenRefreshView):
    serializer_class = TokenRefreshSerializer


""" Create Todo view """
class CreateTodoView(generics.CreateAPIView):
    serializer_class = CreateTodoSerializer
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        request.data['user_id'] = self.request.user.pk 
        return super().create(request, *args, **kwargs)


"""List Todo view"""
class ListTodoView(generics.ListAPIView):
    serializer_class = ListTodoSerializer
    permission_classes = (IsAuthenticated,)
    
    def get_queryset(self):
        return Todo.objects.filter()


"""Detail Todo view"""
class DetailTodoView(generics.RetrieveAPIView):
    serializer_class = ListTodoSerializer
    permission_classes = (IsAuthenticated,)
    
    def get_object(self):
        try:
            todo = Todo.objects.get(is_removed=False, pk=self.kwargs.get("todo_id"))
            return todo
        except Todo.DoesNotExist:
            raise NotFound("Item does not exists!")
        

""" Update Todo view"""
class UpdateTodoView(generics.UpdateAPIView):
    serializer_class = UpdateTodoSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        try:
            todo = Todo.objects.get(pk=self.kwargs.get("todo_id"))
            if todo.user_id.id != self.request.user.pk:
                raise ValidationError("Only the owner can update the item")
            
            if todo and todo.is_removed == True:
                raise ValidationError("Item has been deleted.")
            
            return todo
        except Todo.DoesNotExist:
            raise NotFound("Item does not exists!")


class DeleteTodoView(generics.DestroyAPIView):
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        try:
            todo = Todo.objects.get(pk=self.kwargs.get("todo_id"))
    
            return todo
        except Todo.DoesNotExist:
            raise NotFound("Item does not exists!")

    def delete(self, request, **kwargs):
        item = self.get_object()
        
        if item.user_id.id != self.request.user.pk:
            raise ValidationError("Only the owner can update the item")
        
        if item and item.is_removed == True:
            raise ValidationError("Item has been deleted.")
        
        item.delete()
        return Response("Item has been deleted successful",status=status.HTTP_204_NO_CONTENT)


