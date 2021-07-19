from django.urls import path
from craigslist_app import views
urlpatterns = [
    path('', views.index, name="home"),
    path('new', views.category_new, name="category_new"),
    path('<int:category_id>', views.category_detail, name="category_detail"),
    path('<int:category_id>/edit', views.category_edit, name="category_edit"),
    path('<int:category_id>/posts', views.post_list, name="post_list"),
    path('<int:category_id>/posts/<int:post_id>', views.post_detail, name="post_detail"),
   
]
