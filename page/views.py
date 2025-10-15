from django.http import HttpResponse
from django.shortcuts import render

# Default home page view with hardcoded response
def home_page_view(request):
    return HttpResponse("Hello, World!")

# Default home page view using home.html
# def home_page_view(request):
    # return render(request, 'home1.html')    

# Default home page view with context & filters
# def home_page_view(request):
#     context = {
#         "inventory_list": ["Widget 1", "Widget 2", "Widget 3"],
#         "greeting": "THAnk you FOR visitING.",
# }
#     return render(request,'home2.html', context)
    

# about page view with  hardcoded response
def about_page_view(request):
    return HttpResponse('About Page')

# about page view using about.html
# def about_page_view(request):
#     return render(request, 'about1.html')
    
# about page view using context
# def about_page_view(request):
#     context = {
#         'name': 'Navin',
#         'age': 50
#     }
#     return render(request, 'about2.html', context)