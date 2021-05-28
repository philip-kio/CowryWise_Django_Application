from rest_framework import generics
from .models import TimeUUID
from .serializers import TimeUUIDPostSerializer,TimeUUIDGetSerializer
from rest_framework.response import Response
from django.shortcuts import redirect
from rest_framework.decorators import api_view
# Create your views here.

class ListTimeUuid(generics.ListAPIView):
    queryset = TimeUUID.objects.all().order_by('-time_date')
    serializer_class = TimeUUIDGetSerializer


# class CreateTimeView(generics.CreateAPIView):
#     queryset = TimeUUID.objects.all()
#     serializer_class = TimeUUIDPostSerializer


@api_view(['POST'])
def createTimeView(request):
    if request.method == "POST":
        serializer = TimeUUIDPostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        if serializer.save():
            return redirect('key_value')
    else:
        return Response({'Response': 'did not work'})