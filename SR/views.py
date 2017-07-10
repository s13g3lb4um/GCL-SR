from django.shortcuts import render, get_object_or_404, redirect
from .models import Speech_Recognition
from .forms import create_sr
from os import remove
# Create your views here.


def sr_list(request, tab='Visualize'):
    SR = Speech_Recognition.objects.order_by('-created_date')
    if request.method == 'POST':
        new_sr = create_sr(request.POST, request.FILES)
        if new_sr.is_valid():
            new_sr.save()
            item = get_object_or_404(Speech_Recognition,
                                     pk=Speech_Recognition.objects.all()[len(
                                        Speech_Recognition.objects.all())-1].
                                     pk)
            item.analyze_audio()
            item.clean_text()
            return render(request, 'SR/sr_detail.html', {'item': item})
        else:
            return render(request, 'SR/sr_list.html',
                          {'SR': SR, 'form': new_sr, 'tab': 'Create'})
    else:
        new_sr = create_sr()
    return render(request, 'SR/sr_list.html', {'SR': SR, 'form': new_sr,
                                               'tab': tab})


def sr_detail(request, item_id):
    item = get_object_or_404(Speech_Recognition, pk=item_id)
    return render(request, 'SR/sr_detail.html', {'item': item})


def analyze_audio(request, item_id, modo):
    item = get_object_or_404(Speech_Recognition, pk=item_id)
    item.analyze_audio(modo)
    item.clean_text()
    return render(request, 'SR/sr_detail.html', {'item': item})


def sr_remove(request, item_id):
    item = get_object_or_404(Speech_Recognition, pk=item_id)
    remove(item.audioFile.path)
    item.delete()
    return redirect('sr_list')
