# Generated by Django 3.2.4 on 2021-07-14 20:05

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books', '0004_alter_book_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='users',
            field=models.ManyToManyField(through='books.Favourite', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='ReadList',
        ),
    ]