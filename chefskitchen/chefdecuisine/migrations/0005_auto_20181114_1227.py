# Generated by Django 2.1.1 on 2018-11-14 12:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chefdecuisine', '0004_auto_20181114_0921'),
    ]

    operations = [
        migrations.RenameField(
            model_name='useracc',
            old_name='name',
            new_name='username',
        ),
        migrations.RemoveField(
            model_name='useracc',
            name='chef_acc',
        ),
        migrations.AddField(
            model_name='souschef',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owner', to=settings.AUTH_USER_MODEL),
        ),
    ]
