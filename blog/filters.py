import django_filters
from blog.models import Post



class PostFilter(django_filters.FilterSet):

    CHOICES=(
        ('april','April'),
        ('may','May'),
        ('june','June'),
        ('july','July'),
        ('august','August')
    )

    archives = django_filters.ChoiceFilter(label='Archive', choices=CHOICES ,method='filter_by_created_at')

    class Meta:
        model=Post
        fields=('category','tag','created_at','title')


    def filter_by_created_at(self,queryset,name,value):
        if value=='april': month=4
        if value=='may': month=5
        if value=='june': month=6
        if value=='july': month=7
        if value=='august': month=8
        return queryset.filter(created_at__year='2021').filter(created_at__month=month)

