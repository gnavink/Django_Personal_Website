from django.http import HttpResponse
from django.shortcuts import render


# def home_page_view(request):
#     return HttpResponse("Hello, World!")

# def home_page_view(request):
    # return render(request, 'home1.html')    

def home_page_view(request):
    context = { 
        "inventory_list": ["Widget 1", "Widget 2", "Widget 3"],
        "greeting": "THAnk you FOR visitING.",
}
    return render(request,'home2.html', context)
    

# def about_page_view(request):
#     return HttpResponse('About Page')

# def about_page_view(request):
#     return render(request, 'about1.html')
    

def about_page_view(request):
    context = {
        'name': 'Navin',
        'age': 50
    }
    return render(request, 'about2.html', context)