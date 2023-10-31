from django.urls import path
#from . import views
from .views import HomeView, articledetailView, UpdatePostView, DeletePostView, addpostView, LikeView

urlpatterns = [
   path('', HomeView.as_view(), name="home"),
   path('article/<int:pk>', articledetailView.as_view(), name = "article_detail" ),
   path('add_post/', addpostView.as_view(), name ="addpost"),
   path('article/edit/<int:pk>', UpdatePostView.as_view(), name ="update_post"),
   path('article/<int:pk>/remove', DeletePostView.as_view(), name ="delete_post"),
   path('like/<int:pk>', LikeView, name='like_post'),
]