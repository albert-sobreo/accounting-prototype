from django import views
from django.db.models import query
from django.shortcuts import render
from django.views import View
from rest_framework import viewsets
from .serializers import *

# Create your views here.
def chartOfAccounts(request):
    return render(request, 'chart_of_accounts.html', {})

def journalView(request):
    return render(request, 'journal.html', {})

# CHART OF ACCOUNTS
class RootAPI(viewsets.ModelViewSet):
    serializer_class = RootSZ
    queryset = Account_Group.objects.all().order_by('code')

class RootNestedAPI(viewsets.ModelViewSet):
    serializer_class = RootNestedSZ
    queryset = Account_Group.objects.all().order_by('code')

class SubGroupAPI(viewsets.ModelViewSet):
    serializer_class = Sub_GroupSZ
    queryset = Account_Sub_Group.objects.all().order_by('code')

class SubNestedAPI(viewsets.ModelViewSet):
    serializer_class = Sub_GroupNestedSZ
    queryset = Account_Sub_Group.objects.all().order_by('code')

class ChildAPI(viewsets.ModelViewSet):
    serializer_class = ChildSZ
    queryset = Child_Account.objects.all().order_by('pk')

class ChildNestedAPI(viewsets.ModelViewSet):
    serializer_class = ChildNestedSZ
    queryset = Child_Account.objects.all().order_by('pk')

# JOURNAL
class JournalAPI(viewsets.ModelViewSet):
    serializer_class = JournalSZ
    queryset = Journal.objects.all().order_by('date')

class JournalNestedAPI(viewsets.ModelViewSet):
    serializer_class = JournalNestedSZ
    queryset = Journal.objects.all().order_by('date')

class JournalEntriesAPI(viewsets.ModelViewSet):
    serializer_class = JournalEntriesSZ
    queryset = Journal_Entries.objects.all().order_by('pk')

class JournalEntriesNestedAPI(viewsets.ModelViewSet):
    serializer_class = JournalNestedSZ
    queryset = Journal_Entries.objects.all().order_by('pk')

class JournalEntriesNestedChildAccountAPI(viewsets.ModelViewSet):
    serializer_class = JournalEntriesNestedChildAccountSZ
    queryset = Journal_Entries.objects.all().order_by('pk')