from django.urls import path
from . import views


urlpatterns = [
    path("posts/", views.PostListCreateAPIView.as_view()),
    path("posts/<str:pk>/", views.PostRetrieveUpdateDestroyAPIView.as_view()),


    path('menu/', views.PostList.as_view()),
    path('menu/<str:pk>/', views.PostDetails.as_view()),

]