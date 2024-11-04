from django.contrib import messages
from django.shortcuts import render, redirect

from blog.forms import ContactForm
from blog.models import Post


# Create your views here.

def index_view(request):
    posts = Post.objects.filter(status=True, published_date__isnull=False)
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'your Message Sent Successfully')
            return redirect('blog:index')

    context = {
        'posts': posts,
        'form': form
    }
    return render(request, 'index.html', context)
