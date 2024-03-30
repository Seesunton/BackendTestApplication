from django.shortcuts import render
from rest_framework import generics
from .sarializers import *
from .models import *

# Create your views here.
class ListTodo(generics.ListAPIView):  # Read
    queryset = ToDo.objects.all() 
    serializer_class = ToDoSerializer

class DetailTodo(generics.RetrieveUpdateAPIView): # Update
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer  # ระบุ serializer_class ที่ต้องใช้

    # หรือ override get_serializer_class() เพื่อระบุคลาส Serializer ที่ต้องใช้
    # def get_serializer_class(self):
    #     return ToDoSerializer

class CreateTodo(generics.CreateAPIView):   # Create
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

class DeleteTodo(generics.DestroyAPIView):   # Delete
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
