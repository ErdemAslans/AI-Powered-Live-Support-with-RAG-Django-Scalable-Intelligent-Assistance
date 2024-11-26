from django.shortcuts import render, redirect
from .models import Rezervasyon
from .forms import RezervasyonForm
from django.contrib.auth.decorators import login_required

@login_required
def create_rezervasyon(request):
    if request.method == 'POST':
        form = RezervasyonForm(request.POST)
        if form.is_valid():
            rezervasyon = form.save(commit=False)
            rezervasyon.user = request.user
            rezervasyon.save()
            return redirect('rezervasyon:rezervasyon_list')
    else:
        form = RezervasyonForm()
    context = {'form': form}
    return render(request, 'create_reservation.html', context)

@login_required
def rezervasyon_list(request):
    reservations = Rezervasyon.objects.filter(user=request.user)
    return render(request, 'rezervasyon_list.html', {'reservations': reservations})
