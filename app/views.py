from django.shortcuts import render

# Create your views here.
def test(request):
    return render(request, 'chart_of_accounts.html', {})