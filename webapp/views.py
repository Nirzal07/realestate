from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .search_options import bedroom, bathroom, State, price_options
from .models import PropertyDetails, Comment, PropertyDetailsForm
from userapp.models import ProfilePic


def home(request):
    properties= PropertyDetails.objects.order_by('-uploaded_on')[:6]
    context= {
        'properties': properties,
        'bedroom_choice': bedroom,
        'bathroom_choice': bathroom,
        'state_choice': State,
        'price_range': price_options
    }
    return render(request, 'webapp/home.html', context)

def about(request):
    realtors = PropertyDetails.objects.all()

    context= {}
    return render(request, 'webapp/about.html', context)

def property(request, p_id):
    """individual property details"""
    property= get_object_or_404(PropertyDetails, id=p_id)
    picture = ProfilePic.objects.get(user=property.seller)
    if request.method=="POST":
        post = property
        comment = request.POST.get('comment')
        if comment != '':
            if request.user.is_authenticated:
                commented_by = request.user
            else:
                return redirect('userapp:user_login')
            Comment.objects.create(post= post, comment= comment, user= commented_by)
        return redirect('webapp:property', p_id=property.id)

    comments= Comment.objects.filter(post=property).filter(publish=True)
    context= {'property': property, 'picture': picture, 'comments': comments}
    return render(request, 'webapp/property.html', context)

@login_required
def property_details_form(request):
    if request.method == "POST":
        form = PropertyDetailsForm(request.POST, request.FILES)
        
        if form.is_valid():
            messages.success(request, "Property Form Submitted, we'll review it and add it ASAP.")
            n_form=form.save(commit=False)
            n_form.seller= request.user
            n_form.save()
            return redirect('webapp:home')
        else:
            messages.error(request, form.errors)
            
    else:
        form= PropertyDetailsForm
    context= {'form': form}
    return render(request, 'webapp/property_details_form.html', context)

def property_list(request):
    """list of all properties with filters"""
    properties= PropertyDetails.objects.order_by('-uploaded_on')
    # filtering properties
    # filter by type [House or land]
    if 'type' in request.POST:
        type= request.POST.get('type')
        properties = properties.filter(property_type__iexact= type)

    # filter by purpose[Buy or rent]
    if 'for' in request.POST:
        fore= request.POST.get('for')
        properties = properties.filter(property_option__iexact= fore)
    paginator = Paginator(properties, 6)
    page = request.POST.get('page')
    paged_properties = properties
    context= {
        'properties': paged_properties,
        'price_range': price_options,
    }
    return render(request, 'webapp/proplisting.html', context)

def search(request):
    search_properties = PropertyDetails.objects.order_by('-uploaded_on')
    # with special feature
    if 'features' in request.GET:
        feature = request.GET.get('features')
        if feature:
            search_properties= search_properties.filter(property_description__icontains=feature)

    # with address
    if 'address' in request.GET:
        address = request.GET.get('address')
        if address:
            search_properties= search_properties.filter(address__iexact=address)

    # with requested bedroom numbers
    if 'bedrooms' in request.GET:
        bedrooms = request.GET.get('bedrooms')
        if bedrooms:
            search_properties = search_properties.filter(bedrooms__iexact=bedrooms)

    # with requested price range
    if 'price' in request.GET:
        price = request.GET.get('price')
        if price:
            search_properties = search_properties.filter(price__lte=price)

    context = {
        'bedroom_choice': bedroom,
        'bathroom_choice': bathroom,
        'state_choice': State,
        'properties': search_properties,
        'values': request.GET,
        'price_range': price_options,
    }

    return render(request, 'webapp/search.html', context)
