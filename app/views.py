from decimal import Decimal
from django import views
from django.db.models import query
from django.shortcuts import render, HttpResponse
from django.views import View
from rest_framework import viewsets
from .serializers import *

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import *

########## FUNCTION-BASED VIEWS ##########
def chartOfAccounts(request):
    return render(request, 'chart_of_accounts.html', {})

def journalView(request):
    return render(request, 'journal.html', {})

def ledgerView(request):
    return render(request, "ledger.html", {})

def testView(request):
    print(Child_Account.objects.get(name='Trade Receivables').me_too())
    return HttpResponse(Child_Account.objects.get(name='Trade Receivables').me_too().name)




########## CHART OF ACCOUNTS ##########
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





########## JOURNAL ##########
class JournalAPI(viewsets.ModelViewSet):
    serializer_class = JournalSZ
    queryset = Journal.objects.all().order_by('code').reverse()

class JournalNestedAPI(viewsets.ModelViewSet):
    serializer_class = JournalNestedSZ
    queryset = Journal.objects.all().order_by('code').reverse()

class JournalEntriesAPI(viewsets.ModelViewSet):
    serializer_class = JournalEntriesSZ
    queryset = Journal_Entries.objects.all().order_by('pk')

class JournalEntriesNestedAPI(viewsets.ModelViewSet):
    serializer_class = JournalNestedSZ
    queryset = Journal_Entries.objects.all().order_by('pk')

class JournalEntriesNestedChildAccountAPI(viewsets.ModelViewSet):
    serializer_class = JournalEntriesNestedChildAccountSZ
    queryset = Journal_Entries.objects.all().order_by('pk')







########## SAVE JOURNAL ##########
class SaveJournalAPI(APIView):
    def post(self, request, format=None):
        journal = request.data
        debit = request.data['debit']
        credit = request.data['credit']

        j = Journal()

        j.code = journal['code']
        j.date = journal['date']
        j.remarks = journal['remarks']

        j.save()

        for item in debit:
            je = Journal_Entries()

            je.journal = j
            je.normally = item['normally']
            je.child_account = Child_Account.objects.get(pk=item['child_account'])
            je.amount = Decimal(item['amount'])

            if je.normally == je.child_account.account_classification.root_account.normally:
                je.child_account.amount += je.amount
                je.child_account.save()
                je.balance = je.child_account.amount
            else:
                je.child_account.amount -= je.amount
                je.child_account.save()
                je.balance = je.child_account.amount
            je.save()


        for item in credit:
            je = Journal_Entries()

            je.journal = j
            je.normally = item['normally']
            je.child_account = Child_Account.objects.get(pk=item['child_account'])
            je.amount = Decimal(item['amount'])

            if je.normally == je.child_account.account_classification.root_account.normally:
                je.child_account.amount += je.amount
                je.child_account.save()
                je.balance = je.child_account.amount
            else:
                je.child_account.amount -= je.amount
                je.child_account.save()
                je.balance = je.child_account.amount 
            je.save()
        return Response()

########## LEDGER ##########
class LedgerAPI(viewsets.ModelViewSet):
    serializer_class = LedgerSZ
    queryset = Child_Account.objects.all().order_by('pk')