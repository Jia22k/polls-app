from django.urls import path
from . import views

app_name = "polls"  # Keep this

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
    path("post-endpoint/", views.my_post_view, name="post-endpoint"),
    path("create/", views.create_poll, name="create"),  # Fix this line
]
