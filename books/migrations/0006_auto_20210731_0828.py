# Generated by Django 3.2.4 on 2021-07-31 08:28

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books', '0005_auto_20210714_2005'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='users',
        ),
        migrations.AddField(
            model_name='book',
            name='favourites',
            field=models.ManyToManyField(blank=True, default=None, related_name='favourite', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Favourite',
        ),
    ]
