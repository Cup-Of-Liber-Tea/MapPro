from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post

class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'post_form.html'
    fields = ['title', 'content', 'location', 'image']
    success_url = '/user/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# PermissionRequiredMixin 제거
class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'post_form.html'
    fields = ['title', 'content', 'location', 'image']

    def get_queryset(self):
        # 현재 로그인한 사용자가 작성자인 경우에만 쿼리셋 반환
        return super().get_queryset().filter(author=self.request.user)

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'post_confirm_delete.html'
    success_url = reverse_lazy('post-list')

    def get_queryset(self):
        # 현재 로그인한 사용자가 작성자인 경우에만 쿼리셋 반환
        return super().get_queryset().filter(author=self.request.user)
