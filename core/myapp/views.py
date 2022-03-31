from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
layout = """<h1>site web with Django | Franco Miguez</h1>
<br>
<ul>
    <li><a href=''>home</a></li>
    <li><a href='/hello-word'>hello word</a></li>
    <li><a href='/page'>page</a></li>
    <li><a href='/contact'>contact</a></li>
</ul>
<br>

"""

def index(request):
    return HttpResponse(layout+"""<h2>Home</h2>
    <p>Welcome</p>
    """)

def hello_word(request):
    return HttpResponse(layout+'<h2>Hello Word whit Django!!!</h2>')

def page(request, number=0):
    if number==5:
        return redirect('contact',name='franco')
    return HttpResponse(layout+"""<h2>My page</h2>
    <p>the Franco Miguez</p>""")

def contact(request, name=""):
    return HttpResponse(layout+f"""<h2>Contacto {name}</h2>""")