# Create your views here.
import json
from django.shortcuts import render, redirect
from django.utils.timezone import now
from . import models
from .models import TreeEntity, TreeUser
from django.db.models import Q
from django.forms.models import model_to_dict
from datetime import date, datetime
from django.http import JsonResponse


class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, obj)


def maplist(request):
    tree_point = models.TreeEntity.objects.all()
    # datas = []
    # datas['list'] = tree_point
    tree_id = []
    tree_entity_id = []
    tree_x = []
    tree_y = []
    # tree_pno = []
    tree_pname = []
    tree_regionid = []
    tree_company = []
    tree_place = []
    tree_rate = []
    # tree_recorderid = []
    # tree_createdate = []
    # tree_checkerid = []
    # tree_checktime = []

    # tree_altitude = []
    # tree_longtitude = []
    # tree_latitude = []

    # tree_height = []
    # tree_dbh = []
    # tree_date = []

    # tree_health = []

    # 传输数据到json
    for i in range(len(tree_point)):
        tree_x.append(tree_point[i].p_x)
        tree_y.append(tree_point[i].p_y)
        tree_entity_id.append(tree_point[i].entity_id)
        tree_id.append(tree_point[i].id)
        tree_rate.append(tree_point[i].rate)
        tree_place.append(tree_point[i].place)
        tree_pname.append(tree_point[i].pname)
        tree_company.append(tree_point[i].plant_company)
        tree_regionid.append(tree_point[i].region_id)

    # 查询
    keyword = request.POST.get('eids', '')
    keyword2 = request.POST.get('species', '')
    keyword3 = request.POST.get('places', '')
    results = TreeEntity.objects.filter(Q(entity_id__icontains=keyword) &
                                        Q(pname__icontains=keyword2) &
                                        Q(place__icontains=keyword3))
    list_results = []
    for result in results:
        dic = model_to_dict(result)
        list_results.append(dic)
    return render(request, 'maptree2.html', {'tree_x': json.dumps(tree_x, cls=ComplexEncoder),
                                             'tree_y': json.dumps(tree_y, cls=ComplexEncoder),
                                             'tree_entity_id': json.dumps(tree_entity_id, cls=ComplexEncoder),
                                             'tree_rate': json.dumps(tree_rate, cls=ComplexEncoder),
                                             'tree_place': json.dumps(tree_place, cls=ComplexEncoder),
                                             'tree_pname': json.dumps(tree_pname, cls=ComplexEncoder),
                                             'tree_id': json.dumps(tree_id, cls=ComplexEncoder),
                                             'region_id': json.dumps(tree_regionid, cls=ComplexEncoder),
                                             'tree_company': json.dumps(tree_company, cls=ComplexEncoder),
                                             'result': json.dumps(list_results, cls=ComplexEncoder)
                                             })


# def mapinsert(request):
#     treeofuser = models.TreeUser.objects.filter(checked=0)
#     list_usertree = []
#     for users in treeofuser:
#         dics = model_to_dict(users)
#         list_usertree.append(dics)
#     return render(request, 'mapinsert.html', {'usertree': json.dumps(list_usertree, cls=ComplexEncoder)})


def map_insert(request):
    if request.method == 'GET':
        treeofuser = models.TreeUser.objects.filter(checked=0)
        list_usertree = []
        for users in treeofuser:
            dics = model_to_dict(users)
            list_usertree.append(dics)

        lasttree = models.TreeEntity.objects.order_by('entity_id').last()
        lasteid = lasttree.entity_id
        new_id = lasteid + 1

        treeofsystem = models.TreeEntity.objects.all()
        tree_entities = []
        for tr in treeofsystem:
            diction = model_to_dict(tr)
            tree_entities.append(diction)

        mycode = models.Code.objects.filter(cname='树种')
        list_code = []
        for co in mycode:
            di = model_to_dict(co)
            list_code.append(di)
        return render(request, 'mapinsert.html', {'unchecked': json.dumps(list_usertree, cls=ComplexEncoder),
                                                  'last': lasteid, 'code': list_code, 'entity': tree_entities,
                                                  'new': new_id})
    elif request.method == "POST":
        id = models.TreeUser.objects.all().count() + 1
        lasttree = models.TreeUser.objects.exclude(Q(way=1) | Q(checked=1)).order_by('id').last()
        lasteid = lasttree.entity_id
        entity_id = request.POST.get("entity_id")
        if entity_id == '':
            entity_id = lasteid + 1
            print(entity_id)
        obj = models.TreeEntity.objects.filter(entity_id=entity_id).first()
        pno = request.POST.get("pno")
        if pno == '':
            if obj:
                pno = obj.pno
            else:
                pno = None
        pname = request.POST.get("pname")
        if pname == '':
            if obj:
                pname = obj.pname
            else:
                pname = None
        p_x = request.POST.get("p_x", None)
        p_y = request.POST.get("p_y", None)
        lng = request.POST.get("lng")
        if lng == '':
            if obj:
                lng = obj.longitude
            else:
                lng = None
        lat = request.POST.get("lat")
        if lat == '':
            if obj:
                lat = obj.latitude
            else:
                lat = None
        ualtitude = request.POST.get("altitude")
        if ualtitude == '':
            if obj:
                ualtitude = obj.altitude
            else:
                ualtitude = None
        height = request.POST.get("tree_height")
        if height == '':
            if obj:
                height = obj.height
            else:
                height = None
        dbh = request.POST.get("dbh")
        if dbh == '':
            if obj:
                dbh = obj.dbh
            else:
                dbh = None
        region_id = request.POST.get("region_id")
        if region_id == '':
            if obj:
                region_id = obj.region_id
            else:
                region_id = None
        plant_company = request.POST.get("plant_company")
        if plant_company == '':
            if obj:
                plant_company = obj.plant_company
            else:
                plant_company = None
        place = request.POST.get("place")
        if place == '':
            if obj:
                place = obj.place
            else:
                place = None
        rate = request.POST.get("rate")
        if rate == '':
            if obj:
                rate = obj.rate
            else:
                rate = None
        feature = request.POST.get("feature")
        if feature == '':
            if obj:
                feature = obj.feature
            else:
                feature = None
        usage = request.POST.get("usage")
        if usage == '':
            if obj:
                usage = obj.usage
            else:
                usage = None
        health = request.POST.get("health")
        if health == '':
            if obj:
                health = obj.health
            else:
                health = None
        introduction = request.POST.get("introduction")
        if introduction == '':
            if obj:
                introduction = obj.introduction
            else:
                introduction = None
        age = request.POST.get("age")
        if age == '':
            if obj:
                age = obj.age
            else:
                age = None
        gender = request.POST.get("gender")
        if gender == '':
            if obj:
                gender = obj.gender
            else:
                gender = None
        image_id = None
        recorder_id = 3
        create_date = now()
        if obj:
            way = 1
        else:
            way = 0
        checked = 0
        models.TreeUser.objects.create(id=id, entity_id=entity_id,
                                       pno=pno, pname=pname, p_x=p_x, p_y=p_y, longitude=lng, latitude=lat,
                                       altitude=ualtitude, height=height, dbh=dbh,
                                       region_id=region_id, plant_company=plant_company, plant_date=None,
                                       place=place, rate=rate, feature=feature, usage=usage, health=health,
                                       introduction=introduction, gender=gender, age=age, image_id=image_id,
                                       recorder_id=recorder_id, create_date=create_date, way=way, checked=checked
                                       )
        return redirect('maptree:insert')
