from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post

class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'  # 게시글 목록 템플릿
    context_object_name = 'posts'

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'  # 게시글 상세보기 템플릿

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'post_form.html'  # 게시글 작성 폼 템플릿
    fields = ['author', 'title', 'content', 'location', 'image']
    success_url = '/user/'          ##### 글작성 완료했을때 갈 url (남승수)

    def form_valid(self, form):
        form.instance.author = self.request.user  # 작성자는 현재 로그인한 사용자
        return super().form_valid(form)         #CreateView의 form_valid() 메서드는 폼의 데이터를 데이터베이스에 저장한 후, 저장이 성공하면 사용자를 리디렉션하는 역할을 합니다.

class PostUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Post
    template_name = 'post_form.html'
    fields = ['title', 'content', 'location', 'image']
    permission_required = 'user.change_post'

    def get_queryset(self):
        return super().get_queryset().filter(author=self.request.user)  # 작성자만 수정 가능

class PostDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Post
    template_name = 'post_confirm_delete.html'
    success_url = reverse_lazy('post-list')
    permission_required = 'user.delete_post'

    def get_queryset(self):
        return super().get_queryset().filter(author=self.request.user)  # 작성자만 삭제 가능

