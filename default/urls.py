from django.urls import path
from .views import poll_list,polllist,pollview,pollvote,pollcreate,polledit,optioncreate

urlpatterns = [
    #path("",poll_list),
    path("",polllist.as_view(),name='poll_list'),
    path("<int:pk>/",pollview.as_view(),name='poll_view'),
    path('<int:oid>/vote',pollvote.as_view(),name='poll_vote'),
    path('add',pollcreate.as_view(),name='poll_create'),
    path("<int:pk>/edit",polledit.as_view(),name='poll_edit'),
    path("<int:pid>/add",optioncreate.as_view(),name="option_create"),
]