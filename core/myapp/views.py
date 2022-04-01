from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
layout = """

"""

def index(request):
    return render(request,'index.html')

def hello_word(request):
    return render(request, 'hello_word.html')

def page(request, number=0):
    if number==5:
        return redirect('contact',name='franco')
    return render(request, 'page.html')

def contact(request, name=""):
    return render(request, 'contact.html')