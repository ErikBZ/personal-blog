from django.conf.urls import url

from . import admin, views

from .views import (
    blog_list,
    blog_detail,
    contact_me,
    project_list,
)

urlpatterns = [
    url(r'^$', blog_list, name="blog_list"),
    # this is used for letting the url decide which blog
    # id to open
    # apprently it needs to be name="thing"
    url(r'^(?P<id>\d+)/$', blog_detail, name="blog_detail"),
]
