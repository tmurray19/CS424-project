# From the chefdecuisine app, import the 'sousChef' (Member) function
from chefdecuisine.models import sousChef

# Import HttpResponse 
from django.http import HttpResponse, HttpResponseRedirect

# Import reverse for form submission
from django.urls import reverse

# For debugging
from IPython import embed

# For rendering HTML Files
from django.shortcuts import render

# For updating user information
from chefdecuisine.forms import chefForm

# To check if a user is logged in
from django.contrib.auth.decorators import login_required

# User authentication
from django.contrib.auth import authenticate, login

# Creating user accounts
from django.contrib.auth.forms import UserCreationForm


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleared_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
        else:
            form = UserCreationForm()
        
        response = render(request, 'signup.html', {
            'form':form,
        })
        # embed()
        return response



# Detail view for the sousChef model
def souschef(request, souschef_id):
    souschef = sousChef.objects.get(id = souschef_id)

    # return HttpResponse('Welcome, Chef %s %s' % (souschef.first_name, souschef.lastname))
    response = render(request, 'chefdecuisine/chef_detail.html', {
        'souschef':souschef,
     })
    # embed()
    return response
    
# Returns a lost of all sousChef members
def souschef_list(request):
    souschef = sousChef.objects.all()
    # return HttpResponse('This should be a list of all Sous Chefs')
           
    response = render(request, 'chefdecuisine/chef_list.html', {
        'souschef':souschef,
    })
    # enbed()
    return response


# Allows user to update their info on the website
@login_required
def souschef_update(request, souschef_id):
    souschef = sousChef.objects.get(id = souschef_id)   
    if request.method == "POST":
        form = chefForm(request.POST, instance = souschef)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('souschef_profile', kwargs={'souschef_id':souschef_id}))
            # return HttpResponseRedirect(request.POST.get('next'))
        else:
            return HttpResponseRedirect('/')
    
    
    form = chefForm(instance = souschef)
    response =  render(request, 'chefdecuisine/chef_update.html', {
        'form':form,
        })

#    embed()
    return response



