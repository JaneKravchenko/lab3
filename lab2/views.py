# coding=utf-8
from django.shortcuts import render_to_response,render,  redirect, get_object_or_404
import models
# Create your views here.
from .forms import MeasurmentForm, AreasForm, AreaInformForm
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

    get_items = (request.GET.items()[0][1]).split("&")
    get_area = request.GET.items()[1][1]
    list_of_value = []
    for i in get_items:
        list_of_value.append(re.findall('=.*$', i)[0][1:])
    if get_area == "areas":
        for i in list_of_value:
            if len(models.Areas.objects.filter(area = i)) == 1:
                news = "Сталася помилка. Поле  вже існує."
                break
            else:
                news = None
        if not news:
            getintable = models.Areas(area=list_of_value[0], area_name=list_of_value[1])
            getintable.save()
    if get_area == "area_inform":


        try:
            print models.Area_inform.objects.raw("SELECT * FROM lab2_area_inform WHERE lab2_area_inform.areas = '"+ list_of_value[0]+ "' AND lab2_area_inform.station = '"+ list_of_value[1]+ "';")[0]
            news = "Сталася помилка. Поле  вже існує."

        except:
            news = None
        if not news:
            getintable = models.Area_inform(areas=list_of_value[0], station=list_of_value[1], elevation=list_of_value[2],point_x=list_of_value[3], point_y=list_of_value[4])
            getintable.save()
    if get_area == "measurment":
        if len(models.Area_inform.objects.filter(areas=list_of_value[0])) == 1 and len(models.Areas.filter(station=list_of_value[1])) == 1 and len(models.Area_inform.objects.filter(date_field=list_of_value[2])) == 1 and len(models.Area_inform.objects.filter(time_field=list_of_value[3])) == 1:
            news = "Сталася помилка. Поле  вже існує."
        else:
            news = None
        if not news:
            getintable = models.Measurment(area=list_of_value[0], station=list_of_value[1], date_field=list_of_value[2] , time_field=list_of_value[3], m1=list_of_value[4] , m2=list_of_value[5], m3=list_of_value[6], m4=list_of_value[7])
            getintable.save()

    if news == None:
        news = "Ваші дані успішно додані."
    return render_to_response('post_edit.html', {"news": news})


def post_detail(request):
    post = models.Measurment.objects.all()
    return render_to_response(request, 'post_detail.html', {'posts': post})
def post_search(request):
    areas = models.Areas.objects.all()
    area_inform = models.Area_inform.objects.all()
    measurment = models.Measurment.objects.all()
    global data

    gett  = ""
    for i in request.GET.items():
        for j in i:
            gett+=j
    print gett
    print re.findall("e$", gett)
    if re.findall("all", gett)!=[]:
        data = measurment.raw("SELECT lab2_areas.*,lab2_area_inform.elevation, lab2_area_inform.point_x, lab2_area_inform.point_y, lab2_measurment.station, lab2_measurment.date_field, lab2_measurment.time_field, lab2_measurment.m1, lab2_measurment.m2, lab2_measurment.m3, lab2_measurment.m4  FROM lab2_measurment, lab2_areas, lab2_area_inform WHERE lab2_areas.area=lab2_measurment.area AND lab2_areas.area=lab2_area_inform.areas AND lab2_measurment.station = lab2_area_inform.station ;")
        fields = ["area", "area name", "elevation", "point_x", "point_y", "station", "date_field", "time_field", "m1", "m2", "m3", "m4"]
        return render(request, 'post.html', {'data': data, 'field': fields})

    else:
        if re.findall("e$", gett)==[]:
            get = request.GET.items()[1][1]
            print get

            field = re.findall('^\w*',get)[0]
            print field
            value = re.findall('\w*$', get)[0]
            print value
            mark  = re.findall('[=><]+', get)[0]
            print mark
        areass = request.GET.items()[0][1]
        if areass == "areas":
            if re.findall("e$", gett)!=[]:
                data = areas.raw("SELECT * FROM lab2_areas;")
            else:
                data = areas.raw("SELECT * FROM lab2_areas WHERE "+ field+mark+"'"+value+"';")
            fields = ["area", "area name"]
            ar = "areas"
        if areass == "area_inform":
            if re.findall("e$", gett)!= []:
                data = area_inform.raw("SELECT * FROM lab2_area_inform;")
            else:
                data = area_inform.raw("SELECT * FROM lab2_area_inform WHERE " + field + mark + "'" + value + "';")
            fields = ["areas", "station", "elevation", "point_x", "point_y"]
            ar = "area_inform"
        if areass == "measurment":
            if re.findall("e$", gett)!= []:
                data = measurment.raw("SELECT * FROM lab2_measurment")
            else:
                data = measurment.raw("SELECT * FROM lab2_measurment WHERE "+ field+mark+"'"+value+"';")
            fields = ["area", "station",  "date_field",  "time_field",  "m1", "m2", "m3", "m4"]
            ar = "measurment"
        if areass == "search_a":
            try:
                data = measurment.raw("SELECT lab2_areas.*,lab2_area_inform.elevation, lab2_area_inform.point_x, lab2_area_inform.point_y, lab2_measurment.station, lab2_measurment.date_field, lab2_measurment.time_field, lab2_measurment.m1, lab2_measurment.m2, lab2_measurment.m3, lab2_measurment.m4  FROM lab2_measurment, lab2_areas, lab2_area_inform WHERE lab2_areas.area=lab2_measurment.area AND lab2_areas.area=lab2_area_inform.areas AND lab2_measurment.station = lab2_area_inform.station AND lab2_areas."+ field+mark+"'"+value+"';")
            except:
                pass
            try:
                data = measurment.raw("SELECT lab2_areas.*,lab2_area_inform.elevation, lab2_area_inform.point_x, lab2_area_inform.point_y, lab2_measurment.station, lab2_measurment.date_field, lab2_measurment.time_field, lab2_measurment.m1, lab2_measurment.m2, lab2_measurment.m3, lab2_measurment.m4  FROM lab2_measurment, lab2_areas, lab2_area_inform WHERE lab2_areas.area=lab2_measurment.area AND lab2_areas.area=lab2_area_inform.areas AND lab2_measurment.station = lab2_area_inform.station AND lab2_area_inform." + field + mark + "'" + value + "';")
            except:
                data = measurment.raw(
                    "SELECT lab2_areas.*,lab2_area_inform.elevation, lab2_area_inform.point_x, lab2_area_inform.point_y, lab2_measurment.station, lab2_measurment.date_field, lab2_measurment.time_field, lab2_measurment.m1, lab2_measurment.m2, lab2_measurment.m3, lab2_measurment.m4  FROM lab2_measurment, lab2_areas, lab2_area_inform WHERE lab2_areas.area=lab2_measurment.area AND lab2_areas.area=lab2_area_inform.areas AND lab2_measurment.station = lab2_area_inform.station AND lab2_measurment." + field + mark + "'" + value + "';")
            fields = ["area", "area name", "elevation", "point_x", "point_y", "station", "date_field", "time_field", "m1", "m2", "m3", "m4"]
            ar = "all"
    return render(request, 'post.html', {'data1': data, 'field': fields, 'ar': ar})

def adddata(request):
    form_measurment = MeasurmentForm()
    form_areas = AreasForm()
    form_area_inform = AreaInformForm()
    return render(request, 'adddata.html', {"form_measurment": form_measurment, "form_areas": form_areas, "form_area_inform":form_area_inform})