from django.db.models import Q

from .filters import PostFilter
from django.views.generic import ListView, DetailView
from .models import Post


class PostsList(ListView):

    model = Post

    ordering = '-created_at'

    template_name = 'posts.html'

    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()

        self.filterset = PostFilter(self.request.GET, queryset)

        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['filterset'] = self.filterset
        return context

class PostDetail(DetailView):

    model = Post

    template_name = 'post.html'

    context_object_name = 'post'


class PostsSearch(ListView):

    model = Post

    ordering = '-created_at'

    template_name = 'search.html'

    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()

        self.filterset = PostFilter(self.request.GET, queryset)

        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['filterset'] = self.filterset
        return context

