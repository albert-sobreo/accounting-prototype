from django import views
from django.db.models import query
from django.shortcuts import render
from django.views import View
from rest_framework import viewsets
from .serializers import *

# Create your views here.
def test(request):
    return render(request, 'chart_of_accounts.html', {})

class RootAPI(viewsets.ModelViewSet):
    serializer_class = RootSZ
    queryset = Account_Group.objects.all().order_by('pk')

class SubGroupAPI(viewsets.ModelViewSet):
    serializer_class = Sub_GroupSZ
    queryset = Account_Sub_Group.objects.all().order_by('pk')

class SubNestedAPI(viewsets.ModelViewSet):
    serializer_class = Sub_GroupNestedSZ
    queryset = Account_Sub_Group.objects.all().order_by('pk')

class ChildAPI(viewsets.ModelViewSet):
    serializer_class = ChildSZ
    queryset = Child_Account.objects.all().order_by('pk')

class ChildNestedAPI(viewsets.ModelViewSet):
    serializer_class = ChildNestedSZ
    queryset = Child_Account.objects.all().order_by('pk')

