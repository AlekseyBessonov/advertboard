from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import AdverList, AdvertDetail, AdvertCreate, AdvertUpdateView, AdvertDeleteView, CommentCreate, CommentListView,CommentDelete

urlpatterns = \
    [
        path('', AdverList.as_view(), name='advert-list'),
        path("add/", login_required(AdvertCreate.as_view()), name="advert-create"),
        path('comments/', CommentListView.as_view(), name='comment_list'),
        path("<slug:slug>/", AdvertDetail.as_view(), name='advert-detail'),
        path("<slug:slug>/comments/",login_required(CommentCreate.as_view()), name="comment-create"),
        path('<int:pk>/comment-delete/', CommentDelete.as_view(), name='comment_delete'),
        path("<slug:slug>/update/", login_required(AdvertUpdateView.as_view()), name='advert-update'),
        path('<slug:slug>/delete/', login_required(AdvertDeleteView.as_view()), name='advert-delete'),



    ]
