import os
import uuid

from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from common.tool import upload_img
from user.models import User


# 初始页面
def index(request):
    token = request.GET.get('token')
    user_id = request.session[token]
    user = User.objects.filter(user_id=user_id).only('user_id').first()
    if not os.path.exists('~/sse-internal'):
        os.mkdir('~/sse-internal')
    if not user:
        data = {
            'code': 200400,
            'msg': '登录超时',
        }
        return JsonResponse(data)
    if request.method == 'GET':
        return render(request, 'index.html', context={'token': token})
    elif request.method == 'POST':
        pass


# 登录页面
def login(request):
    '''
        用户登录
    :token :用户登录表示
    :user_name:用户名
    :user_pwd:用户密码
    :user : 用户对象

    :return: Json数据
    '''

    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        user_name = request.POST.get('Login_name')
        user_pwd = request.POST.get('Login_paw')
        if not user_name or not user_pwd:
            data = {
                'code': 200400,
                'msg': '身份信息不能为空'
            }
            return JsonResponse(data)
        # User.objects.filter(Q(user_name=user_name)&Q(user_pwd=user_pwd)).first()
        user = User.objects.filter(Q(user_name=user_name, user_pwd=user_pwd)).first()
        if not user:
            data = {
                'code': 200400,
                'msg': '密码或账号错误',
            }
            return JsonResponse(data)
        token = str(uuid.uuid4())
        request.session[token] = user.user_id
        data = {
            'code': 200001,
            'msg': '登录成功',
            'token': token
        }

        return JsonResponse(data)


# 注册页面
def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        user_name = request.POST.get('Login_name')
        user_pwd = request.POST.get('Login_paw')
        user_tel = request.POST.get('tel')
        user_idcard = request.POST.get('Idcard')
        if not user_name or not user_pwd or not user_tel or not user_idcard:
            data = {
                'code': 200400,
                'msg': '身份信息不能为空'
            }
            return JsonResponse(data)

        user = User.objects.filter(Q(user_name=user_name) | Q(user_idcard=user_idcard) | Q(user_tel=user_tel)).first()

        if user:
            data = {
                'code': 200400,
                'msg': '使用本人的信息注册',
            }
            return JsonResponse(data)
        user = User()
        user.user_name = user_name
        user.user_pwd = user_pwd
        user.user_tel = user_tel
        user.user_idcard = user_idcard

        user.save()

        data = {
            'code': 200001,
            'msg': '注册成功'
        }
        return JsonResponse(data)


# 修改密码
def revise(request):
    token = request.GET.get('token')
    user_id = request.session[token]
    user = User.objects.filter(user_id=user_id).first()
    if not user:
        data = {
            'code': 200400,
            'msg': '先登录'
        }
        return JsonResponse(data)
    if request.method == 'GET':
        return render(request, 'change_password.html')
    elif request.method == 'POST':
        old_pwd = request.POST.get('old_psd')
        new_pws = request.POST.get('new_psd')
        re_pwd = request.POST.get('re_psd')
        if not old_pwd or not new_pws or not re_pwd:
            data = {
                'code': 200400,
                'msg': '信息不完整',
                'token': token
            }
            return JsonResponse(data)
        if not old_pwd == user.user_pwd:
            data = {
                'code': 400000,
                'msg': '原密码不正确',
                'token': token
            }
            return JsonResponse(data)
        if not new_pws == re_pwd:
            data = {
                'code': 200400,
                'msg': '新密码两次输入不同',
                'token': token
            }
            return JsonResponse(data)
        user.user_pwd = new_pws
        user.save()
        data = {
            'code': 200100,
            'msg': '密码修改成功',
            'token': token
        }
        return JsonResponse(data)


# 忘记密码
def forget(request):
    if request.method == 'GET':
        return render(request, 'forget_password.html')
    elif request.method == 'POST':
        name = request.POST.get('Login_name')
        old_paw = request.POST.get('Login_paw')
        idcard = request.POST.get('Login_Idcard')
        user = User.objects.filter(user_name=name).first()

        if not user:
            data = {
                'code': 200400,
                'msg': '此用户不存在'
            }
            return JsonResponse(data)
        if not user.user_idcard == idcard:
            data = {
                'code': 200400,
                'msg': '身份证不正确'
            }
            return JsonResponse(data)
        user.user_pwd = old_paw
        user.save()
        data = {
            'code': 200100,
            'msg': '修改成功'
        }
        return JsonResponse(data)


#
# # 个人详情页面
# def detail(request):
#     token = request.Get.get('token')
#     user_id = request.session[token]
#     user = User.objects.filter(user_id=user_id).first()
#     if request.method == 'GET':
#         if not user:
#             data = {
#                 'code': 200400,
#                 'msg': '登录超时重新登录',
#             }
#             return data
#         return render(request, 'user_detail.html')
#     elif request.method == 'POST':
#         data = {
#             'code': 200100,
#             'msg': '个人详情展示',
#             'user_name': user.user_name,
#             'user_tel': user.user_tel,
#             'user_id_card': user.user_idcard,
#             'token': token
#         }
#         return JsonResponse(data)

# 上传
def upload(request):
    token = request.GET.get('token')
    user_id = request.session[token]
    user = User.objects.filter(user_id=user_id).only('user_id').first()
    if not user:
        data = {
            'code': 200400,
            'msg': '登录超时'
        }
        return JsonResponse(data)

    dir_files = request.FILES.getlist("sub_file", '')
    for i in dir_files:
        new_i=str(i)
        if not new_i.endswith('.pcd'):
            data={
                'code':400400,
                'msg':'文件必须全为pcd格式',
                'token':token
            }
            return JsonResponse(data)

    if not dir_files:
        data = {
            'code': 200104,
            'msg': '文件夹为空',
            'token': token
        }

        return JsonResponse(data)
    if not os.path.exists('~/sse-images'):
        os.mkdir('~/sse-images')
    try:
        upload_img(dir_files=dir_files, token=token)
    except BaseException as error:
        print(error)
        data = {
            'code': 400400,
            'msg': '图片上传错误',
            'token': token
        }
        return JsonResponse(data)
    data = {
        'code': 200100,
        'msg': '上传成功',
        'token': token
    }
    return JsonResponse(data)
