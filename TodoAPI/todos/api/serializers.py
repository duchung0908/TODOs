from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from ..models import Todo
  

# Customize user infor in token
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):

        token = super().get_token(user)
        token['username'] = user.username
        token['email'] = user.email
        
        return token
    

# Create Todo serializer
class CreateTodoSerializer(serializers.ModelSerializer):

    title = serializers.CharField(max_length=100, required=True)
    description = serializers.CharField(max_length=300, required=False, allow_null=True)

    class Meta:
        model = Todo
        fields = "__all__"


# Get list Todo serializer exclude user_id, is_removed and modified fields
class ListTodoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Todo
        exclude = ('user_id', 'modified', 'is_removed')


class UpdateTodoSerializer(serializers.ModelSerializer):

    title = serializers.CharField(max_length=100, required=False)
    description = serializers.CharField(max_length=300)
    completed = serializers.BooleanField()

    class Meta:
        model = Todo
        exclude = ('user_id', 'modified', 'is_removed')
    



