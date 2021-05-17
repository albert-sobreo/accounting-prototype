from django.db import models

# Create your models here.
class Account_Group(models.Model):
    code = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    normally = models.CharField(max_length=100)
    permanence = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=24, decimal_places=5, null=True, blank=True, default= 0.0)

    class Meta:
        verbose_name = "Account Group"
        verbose_name_plural = "Account Groups"

    def __str__(self):
        return self.name

class Account_Sub_Group(models.Model):
    code = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    root_account = models.ForeignKey(Account_Group, on_delete=models.PROTECT, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Account Sub-Group"
        verbose_name_plural = "Account Sub-Groups"

    def __str__(self):
        return self.name

class Child_Account(models.Model):
    code = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    account_classification = models.ForeignKey(Account_Sub_Group, on_delete=models.PROTECT, null=True, blank=True)
    me = models.ForeignKey('self', null=True,blank=True, on_delete=models.PROTECT)
    contra = models.BooleanField()
    amount = models.DecimalField(max_digits=24, decimal_places=5, null=True, blank=True,default= 0.0)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Child Account"
        verbose_name_plural = "Child Accounts"

    def __str__(self):
        return self.name

    def me_too(self):
        print(self.child_account_set.all())
        return (self.child_account_set.all())

class Party(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    chart_of_accounts = models.ForeignKey(Child_Account, on_delete=models.PROTECT, null=True, blank=True)

    class Meta:
        verbose_name = "Party"
        verbose_name_plural = "Parties"

    def __str__(self):
        return self.name

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
    
    def __str__(self):
        return self.name

class Journal(models.Model):
    code = models.CharField(max_length=100)
    date = models.DateField(null=True, blank=True)
    remarks = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Journal'
        verbose_name_plural = "Journals"

    def __str__(self):
        return self.code

class Journal_Entries(models.Model):
    journal = models.ForeignKey(Journal, on_delete=models.PROTECT, null=True, blank=True)
    normally = models.CharField(max_length=100)
    child_account = models.ForeignKey(Child_Account, on_delete=models.PROTECT, null=True, blank=True)
    amount = models.DecimalField(max_digits=24, decimal_places=5, null=True, blank=True,default= 0)
    balance = models.DecimalField(max_digits=24, decimal_places=5, null=True, blank=True,default= 0)

    class Meta:
        verbose_name = "Journal Entry"
        verbose_name_plural = "Journal Entries"

    def __str__(self):
        return self.journal.code + " " + self.normally + " " + self.child_account.name
