from django.urls import path

from . import views

urlpatterns = [
    path('subrabbles/', views.subrabble_list, name='api-subrabble-list'),
    path('subrabbles/!<str:rabble_name>/', views.subrabble_by_id, name='api-subrabble-by-id'),
    path('subrabbles/!<str:rabble_name>/posts', views.posts_by_subrabble, name='api-posts-by-subrabble'),
    path('subrabbles/!<str:rabble_name>/posts/<int:pk>', views.post_in_subrabble, name='api-post-in-subrabble')
]