from django.shortcuts import render

def landPage(request):
    return render(request, 'landPage.html')