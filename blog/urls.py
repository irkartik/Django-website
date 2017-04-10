from django.conf.urls import url
from django.views.generic import DetailView, ListView
from blog.models import Post, Catagory

urlpatterns = [
    url(r'^$', ListView.as_view(queryset=Post.objects.all().order_by("-date")[:25], template_name="blog/home.html")),
    url(r'^(?P<pk>\d+)$', DetailView.as_view(model=Post, template_name="blog/post.html")),
    url(r'(?P<pk>[^/]+)/(?P<slug>[-\w]+)$', DetailView.as_view(model=Catagory, template_name="blog/catagory.html")),
]