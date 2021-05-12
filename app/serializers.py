from rest_framework import serializers
from .models import *

class RootSZ(serializers.ModelSerializer):
    class Meta:
        model = Account_Group
        fields = "__all__"

class Sub_GroupSZ(serializers.ModelSerializer):
    class Meta:
        model: Account_Sub_Group
        fields = "__all__"

class ChildSZ(serializers.ModelSerializer):
    class Meta:
        model: Child_Account
        fields = "__all__"

class Sub_GroupNestedSZ(serializers.ModelSerializer):
    root_account = RootSZ(read_only=True)
    class Meta:
        model = Account_Sub_Group
        fields = "__all__"

class ChildNestedSZ(serializers.ModelSerializer):
    account_classification = Sub_GroupNestedSZ(read_only=True)
    class Meta:
        model = Child_Account
        fields = "__all__"
    