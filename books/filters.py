import django_filters

from .models import *

class BookFilter(django_filters.FilterSet):
    class Meta:
        model = Book
        field = '__all__'
