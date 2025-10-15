from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

# Default home page view with hardcoded response
# def home_page_view(request):
#     return HttpResponse("Hello, World!")

# Default home page view using home.html
# def home_page_view(request):
    # return render(request, 'home1.html')    

# Default home page view with context & filters
def home_page_view(request):
    context = {
        "inventory_list": ["Widget 1", "Widget 2", "Widget 3"],
        "greeting": "THAnk you FOR visitING.",
}
    return render(request,'home3.html', context)
    

# about page view with  hardcoded response
# def about_page_view(request):
#     return HttpResponse('About Page')

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

# Class Based views
class about_page_view(TemplateView):
    template_name = "about3.html"

    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        context["contact_address"] = "123 Main Street"
        context["phone_number"] = "555-555-5555"
        return context
