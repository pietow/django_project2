from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['key1'] = 'value1'
        context['key2'] = 'value2'
        context['key3'] = ['HELLO', 2, 3, 4, 5]
        return context

# function based view
def homePageView(request):
    print(request.user)
    context = {
        'key1': 'value1',
        'key2': 'value2',
        'key3': [1, 2, 3, 4, 5],
    }
    response = render(request, 'home2.html', context)
    response.write('<p>Here is the text of my page.</p>')
    return response
    # return render(request, 'home2.html', context) #response object

class AboutPageView(TemplateView): #new
    template_name = 'about.html'
