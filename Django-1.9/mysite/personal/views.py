from django.shortcuts import render

def index(request):
    return render(request, 'personal/home.html')

def contacts(request):
    return rener(request, 'personal/basic.html', {'content':['If you like to contact with me email me','gu14.0020@gmail.com']})
