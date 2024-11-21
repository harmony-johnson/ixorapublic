from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class Index(TemplateView):
  template_name = 'index.html'

class About(TemplateView):
  template_name = 'about.html'

class SalesLetter(TemplateView):
  template_name = 'sales-letter.html'

class LandPurchase(TemplateView):
  template_name = 'land-purchase.html'

class ConsultantSubscription(TemplateView):
  template_name = 'consultant-subscription.html'