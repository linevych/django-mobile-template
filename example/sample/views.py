from django.views.generic import TemplateView
from mobile_template.views import MobileTemplateView


class Home(MobileTemplateView, TemplateView):
    template_name = 'index.html'
