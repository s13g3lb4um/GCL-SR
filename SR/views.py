from django.shortcuts import render, get_object_or_404, redirect
from .models import Speech_Recognition
from .forms import create_sr
from os import remove
# Create your views here.


def sr_list(request):
    if request.method == 'POST':
        new_sr = create_sr(request.POST, request.FILES)
        if new_sr.is_valid():
            new_sr.save()
    else:
        new_sr = create_sr()
    SR = Speech_Recognition.objects.order_by('-created_date')
    return render(request, 'SR/sr_list.html', {'SR': SR, 'form': new_sr})


def sr_detail(request, item_id):
    item = get_object_or_404(Speech_Recognition, pk=item_id)
    return render(request, 'SR/sr_detail.html', {'item': item})


def analyze_audio(request, item_id):
    item = get_object_or_404(Speech_Recognition, pk=item_id)
    item.analyze_audio()
    return render(request, 'SR/sr_detail.html', {'item': item})


def sr_remove(request, item_id):
    item = get_object_or_404(Speech_Recognition, pk=item_id)
    remove(item.audioFile.path)
    item.delete()
    return redirect('sr_list')
