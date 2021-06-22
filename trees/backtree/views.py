from django.shortcuts import render, redirect
from . import models
from django.http import HttpResponse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage
from django.utils.timezone import now
from .models import TreeEntity, TreeUser, Edit
from .models import Code
from django.db.models import Q
from django.forms.models import model_to_dict
from datetime import date, datetime


# Create your views here.

def lists(req, pIndex):
    list1 = models.TreeEntity.objects.all().order_by("id")
    # 分页
    p = Paginator(list1, 20)
    if pIndex == "":
        pIndex = 1
    else:
        int(pIndex)
    list2 = p.page(pIndex)
    plist = p.page_range

    # 查询
    keyword = req.POST.get('eid', '')
    keyword2 = req.POST.get('species', '')
    keyword3 = req.POST.get('places', '')
    results = TreeEntity.objects.filter(Q(entity_id__icontains=keyword) &
                                        Q(pname__icontains=keyword2) &
                                        Q(place__icontains=keyword3)).order_by("id")
    list_results = []
    for result in results:
        dic = model_to_dict(result)
        list_results.append(dic)

    return render(req, 'back_list.html', {'list': list2, 'plist': plist, 'pIndex': pIndex, 'result': list_results})


def checktree(request):
    ids = request.GET.get('num', 0)
    ifEntered = request.GET.get('isEntered', 2)
    print(ids)
    print(ifEntered)
    if ifEntered == '1':
        print("通过")
        obj = models.TreeUser.objects.filter(Q(id=ids) & Q(checked=0)).first()
        if obj:
            obj.checked = 2
            obj.save()
            eids = obj.entity_id
            obj2 = models.TreeEntity.objects.filter(entity_id=eids).first()
            if obj2:
                obj2.id = ids
                obj2.pno = obj.pno
                obj2.pname = obj.pname
                obj2.p_x = obj.p_x
                obj2.p_y = obj.p_y
                obj2.longitude = obj.longitude
                obj2.latitude = obj.latitude
                obj2.altitude = obj.altitude
                obj2.height = obj.height
                obj2.dbh = obj.dbh
                obj2.region_id = obj.region_id
                obj2.plant_company = obj.plant_company
                obj2.plant_date = obj.plant_date
                obj2.place = obj.place
                obj2.rate = obj.rate
                obj2.feature = obj.feature
                obj2.usage = obj.usage
                obj2.health = obj.health
                obj2.introduction = obj.introduction
                obj2.gender = obj.gender
                obj2.age = obj.age
                obj2.image_id = obj.image_id
                obj2.recorder_id = obj.recorder_id
                obj2.create_date = obj.create_date
                obj2.checker_id = 2
                obj2.check_time = now()
                obj2.save()
                obj.way = 1
                obj.save()
            else:
                models.TreeEntity.objects.create(id=ids, entity_id=obj.entity_id,
                                                 pno=obj.pno, pname=obj.pname, p_x=obj.p_x, p_y=obj.p_y,
                                                 longitude=obj.longitude,
                                                 latitude=obj.latitude,
                                                 altitude=obj.altitude, height=obj.height, dbh=obj.dbh,
                                                 region_id=obj.region_id, plant_company=obj.plant_company,
                                                 plant_date=None,
                                                 place=obj.place, rate=obj.rate, feature=obj.feature, usage=obj.usage,
                                                 health=obj.health,
                                                 introduction=obj.introduction, gender=obj.gender, age=obj.age,
                                                 image_id=obj.image_id,
                                                 recorder_id=obj.recorder_id, create_date=obj.create_date, checker_id=2,
                                                 check_time=now()
                                                 )
    elif ifEntered == '0':
        print("不通过")
        obj = models.TreeUser.objects.filter(Q(id=ids) & Q(checked=0)).first()
        if obj:
            obj.checked = 1
            obj.save()
    list_entity = models.TreeEntity.objects.all().order_by("entity_id")
    list_user = models.TreeUser.objects.all().order_by("checked")
    dischecked = models.TreeUser.objects.filter(checked=0)
    return render(request, 'back_check.html', {'list_entity': list_entity, 'list_user': list_user,
                                               'dischecked': dischecked})


def codes(request):
    code_list = models.Code.objects.all().order_by("cid")
    length = models.Code.objects.all().count()

    # 代码查询
    if request.method == 'GET':
        keyword = request.GET.get('cno', '')
        keyword2 = request.GET.get('cname', '')
        keyword3 = request.GET.get('des', '')
        results = models.Code.objects.filter(Q(cno__icontains=keyword) &
                                             Q(cname__icontains=keyword2) &
                                             Q(des__icontains=keyword3)).order_by("cid")
        list_results = []
        for result in results:
            dic = model_to_dict(result)
            list_results.append(dic)
        return render(request, 'back_code.html', {'list': code_list, 'result': list_results, 'len': length})
    elif request.method == 'POST':
        code_id = request.POST.get('cid_post')
        code_number = request.POST.get('cno_post', '')
        code_name = request.POST.get('cname_post', '')
        code_des = request.POST.get('des_post', '')
        if code_id == '':
            code_id = models.Code.objects.all().count() + 1
            models.Code.objects.create(cid=code_id, cno=code_number, cname=code_name, des=code_des)
        else:
            obj = models.Code.objects.filter(cid=code_id).first()
            if obj:
                obj.cno = code_number
                obj.cname = code_name
                obj.des = code_des
                obj.save()
        return redirect('backtree:codes')


def usertree(request):
    # 查询
    keyword = request.POST.get('id', '')
    keyword2 = request.POST.get('eid', '')
    keyword3 = request.POST.get('pname', '')
    results = models.TreeUser.objects.filter(Q(id__icontains=keyword) &
                                             Q(entity_id__icontains=keyword2) &
                                             Q(pname__icontains=keyword3)).exclude(checked=1).order_by("id")
    list_results = []
    for result in results:
        dic = model_to_dict(result)
        list_results.append(dic)

    # 编辑
    utree_id = request.POST.get("id_insert", '')
    if utree_id != '':
        objs = models.TreeUser.objects.filter(id=utree_id).first()
        if objs:
            pno = request.POST.get("pno")
            if pno == '':
                pno = objs.pno
            pname = request.POST.get("pname_insert")
            if pname == '':
                pname = objs.pname
            lng = request.POST.get("lng")
            if lng == '':
                lng = objs.longitude
            lat = request.POST.get("lat")
            if lat == '':
                lat = objs.latitude
            ualtitude = request.POST.get("altitude")
            if ualtitude == '':
                ualtitude = objs.altitude
            height = request.POST.get("tree_height")
            if height == '':
                height = objs.height
            dbh = request.POST.get("dbh")
            if dbh == '':
                dbh = objs.dbh
            region_id = request.POST.get("region_id")
            if region_id == '':
                region_id = objs.region_id
            plant_company = request.POST.get("plant_company")
            if plant_company == '':
                plant_company = objs.plant_company
            place = request.POST.get("place")
            if place == '':
                place = objs.place
            rate = request.POST.get("rate")
            if rate == '':
                rate = objs.rate
            feature = request.POST.get("feature")
            if feature == '':
                feature = objs.feature
            usage = request.POST.get("usage")
            if usage == '':
                usage = objs.usage
            health = request.POST.get("health")
            if health == '':
                health = objs.health
            introduction = request.POST.get("introduction")
            if introduction == '':
                introduction = objs.introduction
            age = request.POST.get("age")
            if age == '':
                age = objs.age
            gender = request.POST.get("gender")
            if gender == '':
                gender = objs.gender
            create_date = now()
            objs.pno = pno
            objs.pname = pname
            objs.longitude = lng
            objs.latitude = lat
            objs.altitude = ualtitude
            objs.height = height
            objs.dbh = dbh
            objs.region_id = region_id
            objs.plant_company = plant_company
            objs.place = place
            objs.rate = rate
            objs.feature = feature
            objs.usage = usage
            objs.health = health
            objs.introduction = introduction
            objs.age = age
            objs.gender = gender
            objs.create_date = create_date
            objs.save()
            # models.TreeUser.objects.get(id=utree_id).update(longitude=lng, latitude=lat, altitude=ualtitude,
            #                                                 height=height,
            #                                                 dbh=dbh, region_id=region_id, plant_company=plant_company,
            #                                                 place=place, rate=rate, feature=feature, usage=usage,
            #                                                 health=health, introduction=introduction, age=age,
            #                                                 gender=gender, create_date=create_date)

    # 删除
    ids = request.GET.get('num', 0)
    print(ids)
    obj = models.TreeUser.objects.filter(id=ids).first()
    if obj:
        obj.checked = 1
        obj.save()
    utree = models.TreeUser.objects.exclude(checked=1).order_by("id")
    list_user = []
    for u in utree:
        d = model_to_dict(u)
        list_user.append(d)
    # 下拉列表
    mycode = models.Code.objects.filter(cname='树种')
    list_code = []
    for co in mycode:
        di = model_to_dict(co)
        list_code.append(di)

    return render(request, 'back_user.html', {'list': list_user, 'result': list_results, 'code': list_code})


def structure_edit(request):
    if request.method == 'POST':
        inforwindow = request.POST.get("iw", '')
        background = request.POST.get("bg", '')
        addition = request.POST.get("ad", '')
        detail = request.POST.get("de", '')
        models.Edit.objects.create(inforwindow=inforwindow, background=background, addition=addition, details=detail)
        idea_list = models.Edit.objects.all()
        return render(request, 'structure.html', {'idea': idea_list})
    else:
        idea_list = models.Edit.objects.all()
        return render(request, 'structure.html', {'idea': idea_list})
