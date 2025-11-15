import django_filters
from .models import Blog

class BlogFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='title', lookup_expr='iexact')
    description = django_filters.CharFilter(field_name='description', lookup_expr='icontains')
    id = django_filters.RangeFilter(field_name='id')
    id_min = django_filters.CharFilter(method='filter_by_id_range', label='From ID')
    id_max = django_filters.CharFilter(method='filter_by_id_range', label='To ID')

    class Meta:
        model = Blog
        fields = ['title', 'description', 'id']
    
    def filter_by_id_range(self, queryset, name, value):
        if(name) == 'id_min':
            return queryset.filter(id__gte = value)
        elif(name == 'id_max'):
            return queryset.filter(id__lte = value)
        return queryset