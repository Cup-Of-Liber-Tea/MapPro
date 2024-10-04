from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.db.models import Q

class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Post.objects.filter(Q(title__icontains=query) | Q(content__icontains=query))
        return Post.objects.all()

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = Post.objects.filter(location=self.object.location)  # 해당 위치의 리뷰
        return context

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'post_form.html'
    fields = ['title', 'content', 'location', 'image', 'gender']  # birthdate 필드는 제거

    def form_valid(self, form):
        form.instance.author = self.request.user
        # 생년월일 결합
        birth_year = self.request.POST.get('birth_year')
        birth_month = self.request.POST.get('birth_month')
        birth_day = self.request.POST.get('birth_day')

        if birth_year and birth_month and birth_day:
            form.instance.birthdate = f"{birth_year}-{birth_month}-{birth_day}"

        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'post_form.html'
    fields = ['title', 'content', 'location', 'image', 'gender']  # birthdate 필드는 제거

    def get_queryset(self):
        return super().get_queryset().filter(author=self.request.user)

    def form_valid(self, form):
        # 생년월일 결합
        birth_year = self.request.POST.get('birth_year')
        birth_month = self.request.POST.get('birth_month')
        birth_day = self.request.POST.get('birth_day')

        if birth_year and birth_month and birth_day:
            form.instance.birthdate = f"{birth_year}-{birth_month}-{birth_day}"

        return super().form_valid(form)

    # 성공적으로 업데이트된 후 리다이렉트할 URL 설정
    def get_success_url(self):
        return reverse_lazy('post-detail', kwargs={'pk': self.object.pk})

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'post_confirm_delete.html'
    success_url = reverse_lazy('post-list')

    def get_queryset(self):
        return super().get_queryset().filter(author=self.request.user)
