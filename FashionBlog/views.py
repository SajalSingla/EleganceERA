from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from .models import Post, Category
from .forms import EditForm, PostForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-id']
    # ordering = ['-post_date']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

class articledetailView(DetailView):
    model = Post 
    template_name = 'article_detail.html'  

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(articledetailView, self).get_context_data(*args, **kwargs)
        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
       
        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
           liked = True 
       
        context["cat_menu"] = cat_menu
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context
    
class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'
    #fields = ['title','title_tag', 'body',]

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

class addpostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'


def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse('article_detail', args=[str(pk)]))