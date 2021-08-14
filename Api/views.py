from Api.models import User
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import request
from .serializers import *
#from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.generics import ListAPIView
from rest_framework import filters


""" @api_view(['GET'])     
def home(request):
    UserDetails = User.objects.all()
    serializer = UserSerializer(UserDetails, many=True) 
    # many = True because we might get loads of query sets
    #filter_fields = ('first_name', 'last_name', 'email', 'age', 'dob', 'mobile_no')
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('first_name', 'email', 'age', 'dob', 'mobile_no')

    return Response({'status':200, 'payload': serializer.data}) """


class home(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['^first_name', '^email','=age', '=dob', '^mobile_no']
    # ^ for starts with and = for exact search
    ordering_fields = ['age']

@api_view(['POST']) 
def postuser(request):
    data = request.data
    serializer = UserSerializer(data = request.data)

    if not serializer.is_valid():
        return Response({'status': 403, 'errors': serializer.errors, 'message': 'Check Your Entries'})

    if  serializer.is_valid():
        serializer.save()
    return Response({'status': 200, 'payload': serializer.data, 'message':'Succesful entry'})
