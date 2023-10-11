from django.shortcuts import render
from django.views.generic import TemplateView
from datetime import datetime
from django.http import HttpResponseForbidden

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        print(self.request) # <WSGIRequest: GET '/'>
        context = super().get_context_data(**kwargs)
        # context['key1'] = 'value1'
        # context['key2'] = 'value2'
        # context['key3'] = ['HELLO', 2, 3, 4, 5]
        return context

    # response object

    def render_to_response(self, context, **response_kwargs):
        if True:
            response = render(self.request, self.template_name, context)
            response.write('Hello World'.upper())
            response.set_cookie('my_cookie', 'my_cookie_value')
            return response
        return super().render_to_response(context, **response_kwargs)

# function based view: direct access to the request object
def homePageView(request):
    print(request)
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


def practice_view(request):
    context = {
        'list_of_numbers': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'greeting': "Hello, World!",
        'user_info': {
            'first_name': "John",
            'last_name': "Doe",
            'email': "john.doe@example.com"
        },
        'is_vip': False,
        'notes': "<strong>Note:</strong> Always learn something new!",
        'my_date': datetime.now(),
    }
    return render(request, 'practice_page.html', context)


class ActiveRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        print(request.COOKIES.get('my_cookie'))
        if not request.COOKIES.get('my_cookie'):
            return HttpResponseForbidden('Wrong cookie')
        return super().dispatch(request, *args, **kwargs)


class DashboardView(ActiveRequiredMixin, TemplateView):
    template_name = 'dashboard.html'
