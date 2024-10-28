from django.urls import path
from.views import BlogDetailView, BlogListView,BlogCreateView, BlogUpdateView,BlogDeleteView


app_name = 'blog'

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),  # blog_list es el nombre que se usará en el template para referirse a esta vista. 
    path('create/', BlogCreateView.as_view(), name='create'),  # blog_create es el nombre que se usará en el template para referirse a esta vista.
    path('<int:pk>/', BlogDetailView.as_view(), name='detail'),  # blog_detail es el nombre que se usará en el template para referirse a esta v
    path('<int:pk>/update/', BlogUpdateView.as_view(), name='update'),  # blog_update es el nombre que se usará en el template para referirse a esta
    path('<int:pk>/delete',BlogDeleteView.as_view(), name='delete') # blog_delete es el nombre que se usará en el template para referirse a esta vista.
   
]