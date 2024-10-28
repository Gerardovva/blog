from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import View,UpdateView,DeleteView
from .froms import PostCreateForm
from .models import Post
from django.urls import reverse_lazy

# Create your views here.

class BlogListView(View):
    def get(self, request, *args, **kwargs):
        posts=Post.objects.all()  #obtenemos todos los posts de la base de datos
        context = {
            'posts': posts,  #pasamos los posts al contexto
        }
        return render(request, 'blog_list.html', context)
    
    
class BlogCreateView(View):
    def get(self, request, *args, **kwargs):
        form = PostCreateForm()
        context = {'form': form}
        return render(request, 'blog_create.html', context)
    
    
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = PostCreateForm(request.POST)
            if form.is_valid():
                title=form.cleaned_data.get('title') #obtenos el título del post
                content = form.cleaned_data.get('content') #obtenemos el contenido del post
                #guardamos el post en la base de datos
                
                p, created = Post.objects.get_or_create(title=title,content=content) #si el post ya existe, lo recuperamos, sino lo creamos
                p.save() 
                return redirect ('blog:home') #redireccionamos a la lista de posts
                
        context = {'form': form}
        return render(request, 'blog_create.html', context)
    
    
class BlogDetailView(View):
    def get(self, request,pk,*args, **kwargs):
        post=get_object_or_404(Post, pk=pk) #obtenemos el post con el id pk
        context={
            'post':post
        }
        return render(request, 'blog_detail.html', context) 
        


class BlogUpdateView(UpdateView):
    model = Post  # El modelo que va a ser actualizado o editado
    fields = ['title', 'content']  # Los campos que se van a editar
    template_name = 'blog_update.html'  # El template que se va a mostrar para editar el post

    def get_success_url(self):
        pk = self.kwargs.get('pk')  # Cambia esto a paréntesis
        return reverse_lazy('blog:detail', args=[pk])
    
    
    
class BlogDeleteView(DeleteView):
    model = Post # el modelo que va a ser eliminado
    template_name='blog_delete.html' # el template que se va a mostrar para confirmar la eliminación del post
    success_url = reverse_lazy('blog:home') # redireccionamos a la lista de posts al terminar de eliminarlo