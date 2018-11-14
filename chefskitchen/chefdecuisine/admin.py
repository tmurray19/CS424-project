from django.contrib import admin

# Register your models here.

from chefdecuisine.models import sousChef, userAcc

admin.site.register(sousChef)
admin.site.register(userAcc)

