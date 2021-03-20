from django.db import models
from django.contrib.auth.models import User
from django import forms
from .search_options import Province, PropertyOption, PropertyType

class PropertyDetails(models.Model):
    """"Property description"""
    property_type = models.CharField(max_length=7, choices=PropertyType, verbose_name='Type')
    property_option = models.CharField(max_length=7, choices=PropertyOption, verbose_name='Category')
    property_title = models.CharField(max_length=200)
    main_image = models.ImageField(upload_to='image', help_text='A clear image showing the whole property.')
    image2 = models.ImageField(upload_to='image', blank=True)
    image3 = models.ImageField(upload_to='image', blank=True)
    image4 = models.ImageField(upload_to='image', blank=True)
    property_description = models.TextField(blank=True)
    price = models.IntegerField()
    negotiable = models.BooleanField(default=False)
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    uploaded_on = models.DateTimeField(auto_now_add=True)
    bedrooms = models.IntegerField(default=0)
    bathrooms = models.IntegerField(default=0)
    address = models.CharField(max_length= 100)
    district = models.CharField(max_length=100)
    Province = models.CharField(max_length=50, choices=Province, default=Province[2][1])
    is_published= models.BooleanField(default=False)

    def __str__(self):
        return self.property_title

class PropertyDetailsForm(forms.ModelForm):
    class Meta:
        model = PropertyDetails
        fields = '__all__'
        exclude= ['is_published', 'uploaded_on', 'seller']


class Comment(models.Model):
    post = models.ForeignKey(PropertyDetails, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    commented_on = models.DateTimeField(auto_now_add=True)
    publish = models.BooleanField(default=True)
    def __str__(self):
        return f'{self.user}: {self.comment[:10]}'


