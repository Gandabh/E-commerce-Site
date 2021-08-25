import django_filters
from product.models import Product
from django.core.paginator import Paginator


class ProductFilter(django_filters.FilterSet):

    CHOICES=(
        ('ascending','Ascending'),
        ('descending','Descending')
    )

    ordering = django_filters.ChoiceFilter(label='Ordering', choices=CHOICES ,method='filter_by_ordering')

    class Meta:
        model=Product
        fields=('category','color','tag','brand','title')


    def filter_by_ordering(self,queryset,name,value):
        expression='price' if value=='ascending' else '-price'
        return queryset.order_by(expression)
    

