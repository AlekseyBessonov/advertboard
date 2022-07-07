from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator

from .forms import AdvertForm
from .models import Advert, Reply
from .filters import AdvertFilter
from .forms import AdvertForm, ReplyForm

# Create your views here.
class AdverList(ListView):
    """"Список объявлений"""
    model = Advert
    queryset = Advert.objects.order_by('-created')
    template_name = "advertboard/advert-list.html"
    paginate_by = 2
    slug = Advert.slug
    form_class = AdvertForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = AdvertFilter(self.request.GET, queryset=self.get_queryset())
        context['form'] = AdvertForm()
        return context



   # def post(self, request, *args, **kwargs):
       # form = self.form_class(request.POST)  # создаём новую форму, забиваем в неё данные из POST-запроса
       # if form.is_valid():  # если пользователь ввёл всё правильно и нигде не ошибся, то сохраняем новый товар

           # form.save()

        #return super().get(request, *args, **kwargs)

class AdvertDetail(DetailView):
    """Подробности объявления"""
    model = Advert
    context_object_name = "advert"
    template_name = "advertboard/advert-detail.html"
    slug = Advert.slug

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Reply.objects.filter(
            comment=Advert.objects.get(slug=self.kwargs.get('slug')))
        return context


class AdvertCreate(CreateView, PermissionRequiredMixin):
    model = Advert
    template_name = "advertboard/advert-create.html"
    def self_user(self, **kwargs):
        return self.request.user
    fields = ['category', 'subject', 'description']
    form = AdvertForm
    success_url = reverse_lazy('advert-list')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        ## привязываю пользователя к посту
        self.object.user = User.objects.get(id=self.request.user.id)
        self.object.save()
        return super().form_valid(form)

class AdvertUpdateView(LoginRequiredMixin, UpdateView):
    model = Advert
    form_class = AdvertForm
    template_name = 'advertboard/advert-update.html'
    success_url = reverse_lazy('advert-list')


class AdvertDeleteView(LoginRequiredMixin, DeleteView):
    model = Advert
    template_name = 'advertboard/advert-delete.html'
    success_url = reverse_lazy('profile')

class CommentCreate(CreateView, LoginRequiredMixin):
    model = Reply
    template_name = "advertboard/comment-create.html"
    fields = ['comment', 'user_reply', 'comment']
    success_url = reverse_lazy('advert-list')
    form = ReplyForm


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        #context['comment'] = self.request.get('pk')
        context['comments'] = Reply.objects.all()
        return context


    def form_valid(self, form):
        self.object = form.save(commit=False)
        # достаю и переопределяю id
        id = self.kwargs.get('pk')
        user_id = self.request.user
        # привязываю комментарий к посту
        self.object.advert_id = id
        self.object.user = user_id
        self.object.save()
        return super().form_valid(form)

class CommentListView(LoginRequiredMixin, ListView):
    model = Reply  # указываем модель, объекты которой мы будем выводить
    template_name = 'advertboard/comments.html'  # указываем имя шаблона, в котором будет лежать html, в котором будут все инструкции о том, как именно пользователю должны вывестись наши объекты
    context_object_name = 'comments'  # это имя списка, в котором будут лежать все объекты, его надо указать, чтобы обратиться к самому списку объектов через html-шаблон
    # queryset = Comment.objects.order_by('post', '-date_posted')
    form_class = ReplyForm

    def get_queryset(self):
        queryset = Reply.objects.filter(comment__user=self.request.user).order_by('comment', '-created')
        return queryset
class CommentDelete(LoginRequiredMixin, DeleteView):
    model = Reply
    template_name = 'advertboard/comment_delete.html'
    success_url = reverse_lazy('profile')

