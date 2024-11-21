from django.urls import path
from . import views

urlpatterns = [
  path('', views.Index.as_view(), name='home'),
  path('about', views.About.as_view(), name='about'),
  path('sales-letter', views.SalesLetter.as_view(), name='sales-letter'), 
  path('land-purchase', views.LandPurchase.as_view(), name='land-purchase'),
  path('consultant-subscription', views.ConsultantSubscription.as_view(), name='consultant-subscription')
]