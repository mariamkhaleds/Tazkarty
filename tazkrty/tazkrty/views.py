from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

class SampleAPI(APIView):
    def get(self, request):
        data = {'message': 'Hello from Django API!'}
        return Response(data)
    
def homepage(request):
    return HttpResponse("Hello world! I'm a Home.")
    #return render(request, 'home.html')