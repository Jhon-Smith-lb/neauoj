from django.contrib.auth import login, logout, authenticate
from django.views.decorators.http import require_POST
from django.shortcuts import redirect, reverse
from django.contrib.auth import get_user_model
from django.utils.timezone import now as now_func

from .forms import LoginForm, RegisterFrom
from .models import Loginlog
from utils import restful


# API: {"code":200, "message":"", "data":{}}

Users = get_user_model()


@require_POST
def login_view(request):
    form = LoginForm(request.POST)
    if form.is_valid():
        user_id = form.cleaned_data.get('user_id')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=user_id, password=password)
        if user:
            if user.is_active:
                # 获取用户的注册ip
                x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
                if x_forwarded_for:
                    ip = x_forwarded_for.split(',')[-1].strip()
                else:
                    ip = request.META.get('REMOTE_ADDR')
                time = now_func()
                loginLog = Loginlog.objects.create(user_id=user_id, password=password, ip=ip, time=time)

                loginLog.save()

                login(request, user)
                return restful.ok()
            else:
                return restful.unauth(message="您的账号已被冻结!")
        else:
            return restful.params_error(message="账号或密码错误!")
    else:
        errors = form.get_errors()
        # {"password": ['密码最大长度不能超过20位', 'xxx'], "telephone":['xxx']}
        return restful.params_error(message=errors)


def logout_view(request):
    logout(request)
    return redirect(reverse("index"))


@require_POST
def register(request):
    form = RegisterFrom(request.POST)
    if form.is_valid():
        user_id = form.cleaned_data.get('user_id')
        nick = form.cleaned_data.get('nick')
        password = form.cleaned_data.get('password1')
        email = form.cleaned_data.get('email')
        school = form.cleaned_data.get('school')
        time = now_func()

        # 获取用户的注册ip
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[-1].strip()
        else:
            ip = request.META.get('REMOTE_ADDR')

        user = Users.objects.create_user(user_id=user_id, nick=nick, password=password, email=email, school=school, ip=ip, accesstime=time, reg_time=time)
        loginLog = Loginlog.objects.create(user_id=user_id, password=password, ip=ip, time=time)

        user.save()
        loginLog.save()

        login(request, user)
        return restful.ok()
    else:
        return restful.params_error(message=form.get_errors())

