from django.shortcuts import HttpResponse, render

def greet(request):

    return HttpResponse('<h1>Hello World! in my Django Project</h1>')


def wow(request):

    l = tuple(str(i**2)+'<br>' for i in range(20))
    
    return HttpResponse(l)

def hey(request):

    name = 'Zeus Online'

    return HttpResponse(f'Hey {name} welcome to Django web App')

def func1(request):

    mydict = {
        'name': 'Amit',
        'location': 'Andheri'
    }
    
    return render(request, 'index.html', mydict)
