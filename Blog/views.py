from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import BlogModel
from .forms import BlogModelForm

@login_required
def create_blog(request):
    if request.method == 'POST':
        form = BlogModelForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False) #Formu ilk başta kaydetmiyoruz çünkü author formda yok daha sonra ekliyoruz bunun sebebi kimse yazar olarak başkasını yazmasın ve güvenlik önlemleri..
            blog.author = request.user
            blog.save()
            return redirect('blog_detail', slug=blog.slug)
    else:
        form = BlogModelForm()
    context = dict({
    'form':form
    })
    return render(request, 'create_blog.html', context)

def blog_detail(request, blog_slug):
    blog = get_object_or_404(BlogModel, slug=blog_slug)
    context = dict({
        'blog': blog })
    return render(request, 'blog_detail.html', context)

def blog_list(request):
    blogs = BlogModel.objects.all().order_by('-created_at')
    context = dict(
        {
        'blogs': blogs })
    return render(request, 'blog_list.html',context)