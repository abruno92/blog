from django.shortcuts import render
from django.views import generic

from .models import Post


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'



def sidebar(request):
    num_posts = Post.objects.all().count()
    num_views = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_views + 1

    context = {
        'num_posts': num_posts,
        'num_views': num_views,
    }

    return render(request, 'sidebar.html', context=context)
