from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.db.models import Q
from django.urls import reverse_lazy

from .filters import PostFilter
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import UpdateView, DeleteView

from .forms import PostForm
from .models import Post, Author


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
        context['is_not_authors'] = not self.request.user.groups.filter(name='authors').exists()
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




class NewsCreate(PermissionRequiredMixin, LoginRequiredMixin,CreateView):
    model = Post
    fields = ['categories', 'title', 'text']
    success_url = reverse_lazy('authors:posts')
    permission_required = ('authors.NewsCreate',)
    def form_valid(self, form):
        author = Author.objects.filter(user=self.request.user.id).first()
        if not author:
            author = Author.objects.first()
            messages.error(self.request, "You not author, we get first.")
        else:
            messages.success(self.request, "The task was created successfully.")
        form.instance.author = author
        form.instance.type = 'N'

        return super(NewsCreate, self).form_valid(form)


class ArticleCreate(PermissionRequiredMixin, LoginRequiredMixin,CreateView):
    model = Post
    fields = ['categories', 'title', 'text']
    success_url = reverse_lazy('authors:posts')
    permission_required = ('authors.ArticleCreate',)
    def form_valid(self, form):
        author = Author.objects.filter(user=self.request.user.id).first()
        if not author:
            author = Author.objects.first()
            messages.error(self.request, "You not author, we get first.")
        else:
            messages.success(self.request, "The task was created successfully.")
        form.instance.author = author
        form.instance.type = 'A'

        return super(ArticleCreate, self).form_valid(form)

class PostFormView(PermissionRequiredMixin, LoginRequiredMixin,UpdateView):
    model = Post
    permission_required = ('authors.PostFormView',)
    fields = [
        "title",
        "text"
    ]

    success_url = reverse_lazy('authors:posts')


class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = Post

    success_url = reverse_lazy('authors:posts')

    template_name = "authors/confirm_delete.html"