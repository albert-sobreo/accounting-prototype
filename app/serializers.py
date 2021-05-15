from rest_framework import serializers
from .models import *

class RootSZ(serializers.ModelSerializer):
    class Meta:
        model = Account_Group
        fields = '__all__'

class RootNestedSZ(serializers.ModelSerializer):
    childAccount = serializers.SerializerMethodField()
    subGroup = serializers.SerializerMethodField()
    class Meta:
        model = Account_Group
        fields = [
            'id',
            'code',
            'name',
            'normally',
            'permanence',
            'childAccount',
            'subGroup',
        ]

    def get_childAccount(self, thisObj):
        childAccount = Child_Account.objects.filter(account_classification__root_account=thisObj)

        return ChildNestedSZ(instance=childAccount, many=True).data

    def get_subGroup(self, thisObj):
        subGroup = thisObj.account_sub_group_set.all()
        return Sub_GroupSZ(instance=subGroup, many=True).data

class Sub_GroupSZ(serializers.ModelSerializer):
    class Meta:
        model = Account_Sub_Group
        fields = "__all__"

class Sub_GroupNestedSZ(serializers.ModelSerializer):
    root_account = RootSZ(read_only=True)
    childAccount = serializers.SerializerMethodField()
    class Meta:
        model = Account_Sub_Group
        fields = [
            'id',
            'code',
            'name',
            'root_account',
            'childAccount',
        ]

    def get_childAccount(self, thisObj):
        childAccount = thisObj.child_account_set.all()
        return ChildSZ(instance=childAccount, many=True).data

class ChildSZ(serializers.ModelSerializer):
    class Meta:
        model = Child_Account
        fields = '__all__'

class ChildNestedSZ(serializers.ModelSerializer):
    account_classification = Sub_GroupNestedSZ(read_only=True)
    me = ChildSZ(read_only=True)
    class Meta:
        model = Child_Account
        fields = "__all__"

class JournalSZ(serializers.ModelSerializer):
    class Meta:
        model = Journal
        fields = "__all__"

class JournalNestedSZ(serializers.ModelSerializer):
    journalEntries = serializers.SerializerMethodField()
    class Meta:
        model = Journal
        fields = [
            'code',
            'date',
            'remarks',
            'journalEntries',
        ]
    def get_journalEntries(self, thisObj):
        journalEntries = thisObj.journal_entries_set.all()

        return JournalEntriesNestedChildAccountSZ(instance=journalEntries, many=True).data

class JournalEntriesSZ(serializers.ModelSerializer):
    class Meta:
        model = Journal_Entries
        fields = "__all__"

class JouralEntriesNestedSZ(serializers.ModelSerializer):
    journal = JournalSZ(read_only=True)
    child_account = serializers.SerializerMethodField()
    class Meta:
        model = Journal_Entries
        fields = [
            'journal',
            'normally',
            'amount',
            'child_account',
        ]

    def get_childAccount(self, thisObj):
        child_account = Child_Account.objects.filter(account_classification__root_account=thisObj)
        return ChildNestedSZ(instance=child_account, many=True).data

class JournalEntriesNestedChildAccountSZ(serializers.ModelSerializer):
    child_account = ChildSZ(read_only=True)
    class Meta:
        model = Journal_Entries
        fields = '__all__'

class LedgerSZ(serializers.ModelSerializer):
    journalEntries = serializers.SerializerMethodField
    class Meta:
        model = Child_Account
        fields = [
            'code',
            'name',
            'account_classfication',
            'amount',
            'journalEntries',
        ]
    def get_journalEntries(self, thisObj):
        journalEntries = thisObj.journal_entries_set.all()

        return JournalEntriesNestedChildAccountSZ(instance=journalEntries, many=True).data