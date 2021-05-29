from rest_framework import generics
from .models import TimeUUID
from .serializers import TimeUUIDPostSerializer,TimeUUIDGetSerializer
from rest_framework.response import Response

from rest_framework.decorators import api_view

# Create your views here.




@api_view(['GET','POST'])

def createTimeView(request):
    if request.method == "POST":
        
        serializer = TimeUUIDPostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        if serializer.save():
            queryset = TimeUUID.objects.order_by('-time_date')
            serializer = TimeUUIDGetSerializer(queryset, many=True)
            return Response(serializer.data)
    
    elif request.method == "GET":
        request.method = "POST"
        serializer = TimeUUIDPostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        if serializer.save():
            queryset = TimeUUID.objects.order_by('-time_date')
            serializer = TimeUUIDGetSerializer(queryset, many=True)
            return Response(serializer.data)
    
    else:
        return Response({'Response': 'did not work'})