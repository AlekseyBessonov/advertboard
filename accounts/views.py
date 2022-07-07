from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, UpdateView, DetailView
from django.urls import reverse_lazy

from .models import Profile
from .forms import ProfileEditForm
from  advert.models import Advert, Reply


class UserProfile(LoginRequiredMixin, ListView):
    model = Advert
    template_name = 'accounts/profile.html'
    context_object_name = 'profil'
    slug = Advert.slug
    #queryset = Reply.objects.all()

    def get_context_data(self, **kwargs):
        #slug = self.kwargs.get('slug')
        context = super().get_context_data(**kwargs)
       # добавляю в контекст только посты определенного пользователя
        context['adverts'] = Advert.objects.filter(user=self.request.user)
        #context['comments'] = Reply.objects.filter(comment=Advert.objects.get(slug=self.kwargs.get('slug')))
        return context


class ProfileUpdateView(UpdateView, LoginRequiredMixin):
    model = Profile
    form_class = ProfileEditForm
    template_name = 'accounts/edit.html'
    success_url = reverse_lazy('profile')

    def get_object(self, **kwargs):

        return self.request.user
