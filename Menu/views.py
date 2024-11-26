from django.shortcuts import render
from Reviews.models import Food,Category
# Create your views here.
def home_view(request):
    foods = Food.objects.all()
    category = Category.objects.all()
    context = {'foods': foods,
               'category': category}
    return render(request,'index.html',context)

def ana_sayfa(request):
     return render(request, 'anasayfa.html')


def gradio_interface(request):
    return render(request, 'gradio_interface.html')
