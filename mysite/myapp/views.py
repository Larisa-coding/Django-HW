from django.shortcuts import render

def data_view(request):
    return render(request, 'myapp/data.html')

def test_view(request):
    return render(request, 'myapp/test.html')