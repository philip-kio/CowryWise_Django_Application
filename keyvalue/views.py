from rest_framework import generics
from .models import TimeUUID
from .serializers import TimeUUIDPostSerializer,TimeUUIDGetSerializer
from rest_framework.response import Response
from django.shortcuts import redirect

# Create your views here.

class ListTimeUuid(generics.ListAPIView):
    queryset = TimeUUID.objects.all().order_by('-time_date')
    serializer_class = TimeUUIDGetSerializer


class CreateTimeView(generics.CreateAPIView):
    queryset = TimeUUID.objects.all()
    serializer_class = TimeUUIDPostSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()
        
        if serializer.save():
            return redirect('key_value')
        else:
            return Response({'Response': 'did not work'})