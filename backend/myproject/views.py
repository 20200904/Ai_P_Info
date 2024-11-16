from django.shortcuts import render

def index(request):
    return render(request, 'index.html')  # React의 index.html 렌더링
