from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
import logging
from .models import Post, AboutUs
from django.http import Http404
from django.core.paginator import Paginator
from django.contrib import messages
from .forms import ContactForm
from .models import Contact


def index(request):
    blog_title = "OurPost"

    # getting data from post model
    all_posts = Post.objects.all()

    # paginate
    paginator = Paginator(all_posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request,'blog/index.html', {'blog_title': blog_title, 'page_obj': page_obj})

def detail(request, slug):
    

    try:
        # getting data from model by post id
        post = Post.objects.get(slug=slug)
        related_posts  = Post.objects.filter(category = post.category).exclude(pk=post.id)

    except Post.DoesNotExist:
        raise Http404("Post Does not Exist!")
  
    return render(request,'blog/detail.html', {'post': post, 'related_posts':related_posts})


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        logger = logging.getLogger("TESTING")
        if form.is_valid():
            logger.debug(f'POST Data is {form.cleaned_data['name']} {form.cleaned_data['email']} {form.cleaned_data['message']}')           
            success_message = 'Your Email has been sent!'
            return render(request,'blog/contact.html', {'form':form,'success_message':success_message})
        else:
            logger.debug('Form validation failure')
        return render(request,'blog/contact.html', {'form':form, 'name': name, 'email':email, 'message': message})
    return render(request,'blog/contact.html')

def about_view(request):
    about_content = AboutUs.objects.first().content
    return render(request,'blog/about.html',{'about_content':about_content})



def search(request):
    query = request.GET.get('q')  
    if query:
        results = Post.objects.filter(title__icontains=query)  
    else:
        results = Post.objects.none() 

    context = {
        'query': query,
        'results': results,
    }
    return render(request, 'blog/search_results.html', context)



def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()          
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('blog:contact')

        else:
           
            messages.error(request, 'Please correct the errors below.')

    else:
        form = ContactForm()

    return render(request, 'blog/contact.html', {'form': form})
