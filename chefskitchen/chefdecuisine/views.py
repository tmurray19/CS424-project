# From the chefdecuisine app, import the 'sousChef' (Member) function
from chefdecuisine.models import sousChef

# Import HttpResponse 
from django.http import HttpResponse

# For debugging
from IPython import embed

# For rendering HTML Files
from django.shortcuts import render


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
