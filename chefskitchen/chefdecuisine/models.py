from django.db import models

from django.contrib.auth.models import User

# Create your models here.


# Create a Member class, called sous chef
# Has at least 2 different Model Fields (CharField for Names, DateField for DOB)



class sousChef(models.Model):

    first_name = models.CharField(max_length = 50)

    last_name = models.CharField(max_length = 50)

    date_of_birth = models.DateField(null = True, blank = True)

    owner = models.ForeignKey(User, null=True,  on_delete = models.CASCADE)

    # exclude['owner']
