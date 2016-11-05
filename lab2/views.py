# coding=utf-8
from django.shortcuts import render_to_response,render,  redirect, get_object_or_404
import models
# Create your views here.
from .forms import PostForm
import re

def project(request):
    areas = models.Areas.objects.all()
    area_inform = models.Area_inform.objects.all()
    measurment = models.Measurment.objects.all()
    context = {
        'areas': areas,
        'area_info' : area_inform,
        'meas': measurment
    }

    return render(request, 'index.html', context)


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('lab2.views.post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render_to_response(request, 'post_edit.html', {'form': form})


def post_detail(request):
    post = models.Measurment.objects.all()
    return render_to_response(request, 'post_detail.html', {'posts': post})
def post_search(request):
    areas = models.Areas.objects.all()
    area_inform = models.Area_inform.objects.all()
    measurment = models.Measurment.objects.all()
    global data
    get =  request.GET.items()[0][1]
    print "GET:"+ str(get)
    if get == 'all':
        data = measurment.raw("SELECT * FROM lab2_measurment, lab2_areas WHERE lab2_areas.area=lab2_measurment.area;")
    else:
        field = re.findall('^\w*',get)[0]
        print field
        value = re.findall('\w*$', get)[0]
        print value
        mark  = re.findall('[=><]+', get)[0]
        print mark
        data = models.Measurment.objects.raw("SELECT * FROM lab2_measurment WHERE "+ field+mark+"'"+value+"';")
    return render(request, 'post.html', {'data1': data})

def adddata(request):
    return render(request, 'adddata.html', {})