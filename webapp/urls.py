from django.urls import path
from . import views


app_name= 'webapp'
urlpatterns= [
    path('', views.home, name= 'home'),
    path('about', views.about, name= 'about'),
    # individual property details
    path('property/<int:p_id>/', views.property, name= 'property'),
    path('property-form', views.property_details_form, name= 'property_form'),
    # property listing
    path('more-properties', views.property_list, name= 'property_list'),
    path('search-results', views.search, name= 'search'),
]