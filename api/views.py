from django.shortcuts import render
from todos.models import Todo
from .serializers import TodoSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view # Function based view import

from rest_framework.views import APIView # Class based view import
from users.models import User
from .serializers import UserSerializer
from django.http import Http404
# Create your views here.

@api_view(['GET', 'POST'])
def todosView(request):
    if request.method == 'GET':
        todos = Todo.objects.all() # GET ALL Todos from db.
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    elif request.method == 'POST':
        serializer = TodoSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save() # Store into database
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'PUT', 'DELETE'])
def todoDetailView(request, pk):
    try:
        todo = Todo.objects.get(pk=pk)
    except Todo.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if(request.method == 'GET'):
        serializer = TodoSerializer(todo)
        return Response(serializer.data, status = status.HTTP_200_OK)
    elif(request.method == 'PUT'):
        serializer = TodoSerializer(todo, data = request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    elif(request.method == 'DELETE'): 
        todo.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
    
# Request types: GET, POST
class Users(APIView):
    def get(self, request): # GET ALL
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)


    def post(self, request): # POST
        serializer = UserSerializer(data = request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

# Request types: GET/:id, PUT, DELETE
class UserDetail(APIView):
    def get_object(self, pk):
        try:
            return User.objects.get(pk = pk)
        except User.DoesNotExist:
            # return Http404
            return None
        
    def get(self, request, pk): # GET/:ID
        user = self.get_object(pk)
        if(user is None):
            return Response({'detail': 'User Not Found.'}, status = status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(user)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    def put(self, request, pk):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data = request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user = self.get_object(pk)
        user.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)