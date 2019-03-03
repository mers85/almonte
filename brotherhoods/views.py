from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

# Create your views here.
from .models import Brotherhood
from .serializers import BrotherhoodSerializer
from django.views.decorators.csrf import csrf_exempt


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'brotherhood': reverse('brotherhood-create', request=request, format=format),
        'brotherhoods': reverse('brotherhood-list', request=request, format=format)
    })


class BrotherhoodList(generics.ListAPIView):
    queryset = Brotherhood.objects.all()
    serializer_class = BrotherhoodSerializer
    permission_classes = (IsAdminUser,)


class BrotherhoodCreate(generics.CreateAPIView):
    authentication_classes = ()
    queryset = Brotherhood.objects.all()
    serializer_class = BrotherhoodSerializer


class BrotherhoodDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Brotherhood.objects.all()
    serializer_class = BrotherhoodSerializer
    permission_classes = (IsAdminUser,)
