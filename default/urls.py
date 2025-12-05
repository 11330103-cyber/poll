from django.urls import path
from .views import poll_list,polllist,pollview,pollvote

urlpatterns = [
    path("",poll_list),
    path("list",polllist.as_view(),name='poll_list'),
    path("<int:pk>/",pollview.as_view(),name='poll_view'),
    path('<int:pk>/vote',pollvote.as_view(),name='poll_vote'),
]