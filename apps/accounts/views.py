from django.shortcuts import render
from rest_framework.response import Response

from apps.accounts.serializer import UserCustomSerializer
# Create your views here.
from .models import User
from rest_framework.views import APIView

class ProfileView(APIView):

    def get(self, request, pk):
        user = User.objects.filter(pk=pk, is_active=True)
        serialiser = UserCustomSerializer
        return Response(serialiser.data)
