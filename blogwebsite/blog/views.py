from django.shortcuts import render,redirect
from . models import Post
from .forms import blogform



def index(request):
    context = {
        'posts':Post.objects.all()
    }
    return render(request, 'blog/index.html',context)

def add_blog(request):
    if request.method == 'POST':

        form=blogform(request.POST)

        if form.is_valid():

            form.save( )
            #username=form.cleaned_data.get('username')
            return redirect('index')
    else:

      form=blogform
    context={'form':form}
    return render(request, 'blog/blog.html', context)

# Create your views here.
