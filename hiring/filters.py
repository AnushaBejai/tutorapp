import django_filters
from .models import * 
from django_filters import DateFilter, CharFilter

class tutorpostfilter(django_filters.FilterSet):
    start_date = DateFilter(field_name = "created_Date", lookup_expr = 'gte')
    end_date = DateFilter(field_name = "created_Date", lookup_expr = 'lte')
    subject = CharFilter(field_name = "subject", lookup_expr = 'icontains')
    #ordered_posts=TutorPost.objects.order_by('-created_Date')

    class Meta:
        model = TutorPost
        fields = {
            'level',
            'tutor', 
            
            }

        
