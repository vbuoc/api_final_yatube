from django_filters import rest_framework as filters

from .models import *


class GroupPostsFilter(filters.FilterSet):

    class Meta:
        model = Post
        fields = ['group', ]