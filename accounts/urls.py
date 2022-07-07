from django.urls import path

from . import views
from advert.views import CommentListView

urlpatterns = [
    path('profile/', views.UserProfile.as_view(), name='profile'),
    path('edit/', views.ProfileUpdateView.as_view(), name='edit'),
    path('<slug:slug>/commentlist/', CommentListView.as_view(), name='comment-list'),
]