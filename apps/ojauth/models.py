from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserManager(BaseUserManager):
    def _create_user(self, user_id, email, nick, password, reg_time, ip, school, accesstime, **kwargs):
        if not user_id:
            raise ValueError('请传入账号！')
        if not email:
            raise ValueError('请传入邮箱！')
        if not nick:
            raise ValueError('清传入姓名！')
        if not password:
            raise ValueError('请传入密码！')
        if not reg_time:
            raise ValueError('请传入注册时间！')
        if not ip:
            raise ValueError('请传入注册ip！')
        if not school:
            raise ValueError('请传入学校！')
        if not accesstime:
            raise ValueError('请传入最近登录时间！')

        user = self.model(user_id=user_id, email=email, nick=nick, password=password, reg_time=reg_time, ip=ip, school=school, accesstime=accesstime, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, user_id, email, nick, password, reg_time, ip, school, accesstime, **kwargs):
        kwargs['is_superuser'] = False
        return self._create_user(user_id, email, nick, password, reg_time, ip, school, accesstime, **kwargs)

    def create_superuser(self, user_id, email, nick, password, reg_time, ip, school, accesstime, **kwargs):
        kwargs['is_superuser'] = True
        kwargs['is_staff'] = True
        return self._create_user(user_id, email, nick, password, reg_time, ip, school, accesstime, **kwargs)


class Users(AbstractBaseUser, PermissionsMixin):
    # id主键
    user_id = models.CharField(primary_key=True, max_length=48)
    # 邮箱
    email = models.CharField(max_length=100, blank=True, null=True)
    # 一共提交次数
    submit = models.IntegerField(blank=True, null=True)
    # 一共解决了多少题
    solved = models.IntegerField(blank=True, null=True)
    # 是否封号（账号状态）默认是1，代表可用
    defunct = models.CharField(max_length=1, default=0)
    # 注册ip
    ip = models.CharField(max_length=46)
    # 最近登录时间
    accesstime = models.DateTimeField(blank=True, null=True)
    # 点开默认是第几页
    volume = models.IntegerField(default=1)
    # 中文还是英文
    language = models.IntegerField(default=1)
    # 注册时间
    reg_time = models.DateTimeField(blank=True)
    # 昵称
    nick = models.CharField(max_length=20)
    # 学校
    school = models.CharField(max_length=20)

    class Meta:
        db_table = 'users'

    USERNAME_FIELD = 'user_id'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    def get_full_name(self):
        return self.nick

    def get_short_name(self):
        return self.nick


class Loginlog(models.Model):
    user_id = models.CharField(max_length=48, primary_key=True)
    password = models.CharField(max_length=40, blank=True, null=True)
    ip = models.CharField(max_length=46, blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'loginlog'



