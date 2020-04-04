from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    # return HttpResponse('<h1>Hello , World!!!</h1>')
    return render(request, 'home.html', {})


def contact_page(request, *args, **kwargs):
    my_contact = {
        'my_phone': 7762021493,
        'my_email': 'thakuraman22july@gmail.com'
    }
    return render(request, 'contact.html', my_contact)


def about_view(request, *args, **kwargs):
    my_context = {
        'my_text': "This is amazing !",
        'my_number': 123,
        'my_list': [123, 256, 'Aman']
    }
    return render(request, 'about.html', my_context)


def social_view(request, *args, **kwargs):
    return render(request, 'social.html', {})
