from django.db import models

# Create your models here.
class Account_Group(models.Model):
    code = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    normally = models.CharField(max_length=100)
    permanence = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=24, decimal_places=5, null=True, blank=True)

    class Meta:
        verbose_name = "Account Group"
        verbose_name_plural = "Account Groups"

class Account_Sub_Group(models.Model):
    code = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    root_account = models.ForeignKey(Account_Group, on_delete=models.PROTECT, null=True, blank=True)

    class Meta:
        verbose_name = "Account Sub-Group"
        verbose_name_plural = "Account Sub-Groups"

class Child_Account(models.Model):
    code = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    account_classification = models.ForeignKey(Account_Sub_Group, on_delete=models.PROTECT, null=True, blank=True)
    me = models.ForeignKey('self',null=True,blank=True, on_delete=models.PROTECT)
    contra = models.BooleanField()
    amount = models.DecimalField(max_digits=24, decimal_places=5, null=True, blank=True)

    class Meta:
        verbose_name = "Child Account"
        verbose_name_plural = "Child Accounts"

class Party(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    chart_of_accounts = models.ForeignKey(Child_Account, on_delete=models.PROTECT, null=True, blank=True)

    class Meta:
        verbose_name = "Party"
        verbose_name_plural = "Parties"

class Inventory_Item(models.Model):
    code = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    quantity = models.IntegerField()
    purchasing_price = models.DecimalField(max_digits=24, decimal_places=5, null=True, blank=True)
    chart_of_accounts = models.ForeignKey(Child_Account, on_delete=models.PROTECT, null=True, blank=True)

    class Meta:
        verbose_name = "Inventory Item"
        verbose_name_plural = "Inventory Items"
