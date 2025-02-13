from django.shortcuts import render


def showslider(request):
        return render(request, 'index.html')
