from django.shortcuts import render,redirect
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Advocate,Company
from.serializers import AdvocateSerializer,CompanySerializer
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
import requests
from dotenv import load_dotenv
import os
load_dotenv()

TWITTER_API_KEY = os.environ.get('TWITTER_API_KEY')

@api_view(['GET'])
def endpoints(request):
    print('TWITTER_API_KEY:',TWITTER_API_KEY)
    data = [
        '/advocates',
        '/advocates/:username'
    ]
    return Response(data)
    
@api_view(['GET','POST'])
def advocates_list(request):
    if request.method == "GET":
        query = request.GET.get('query')
        if query == None:
            query = ''
        advocate = Advocate.objects.filter(Q(username__icontains=query)|Q(bio__icontains=query))
        serialized_data = AdvocateSerializer(advocate, many=True)
        return Response(serialized_data.data)

    if request.method == "POST":
        advocate = Advocate.objects.create(
            username=request.data['username'],
            bio=request.data['bio']
        )
        serializer = AdvocateSerializer(advocate, many=False)

        return Response(serializer.data)


class Advocate_details(APIView):
    def get_object(self, username):
        try:
            return Advocate.objects.get(username=username)
        except Advocate.DoesNotExist:
            raise JsonResponse('Advocate does not exit')
            
    def get(self, request, username):
        head = {'Authorization': "Bearer " + str(TWITTER_API_KEY) }

        fields = "?user.fields=profile_image_url,description,public_metrics"

        url = "https://api.twitter.com/2/users/by/username/" + str(username) + fields
        response_data = requests.get(url,headers=head).json()
        data = response_data['data']
        data['profile_image_url'] = data['profile_image_url'].replace('normal','400x400')
        print("Data:" ,response_data)


        advocate = self.get_object(username)
        advocate.name = data['name']
        advocate.image = data['profile_image_url']
        advocate.bio = data['description']
        advocate.twitter = "https://twitter.com/" + username
        advocate.save()
        serialize = AdvocateSerializer(advocate, many=False)
        return Response(serialize.data)

    def post(self, request, username):
        advocate = self.get_object(username)
        advocate.username = request.data['username']
        advocate.bio = request.data['bio']
        advocate.save()
        serialize = AdvocateSerializer(advocate, many=False)
        return Response(serialize.data)

    def delete(self, request, username):
        advocate = self.get_object(username)
        advocate.delete()
        return Response('User was deleted')


@api_view(['GET'])
def companies_list(request):
    companies = Company.objects.all()
    serializer = CompanySerializer(companies, many=True)
    return Response(serializer.data)
