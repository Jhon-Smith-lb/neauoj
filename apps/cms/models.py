from django.db import models


class Balloon(models.Model):
    balloon_id = models.AutoField(primary_key=True)
    # 发给谁
    user_id = models.CharField(max_length=48)
    # 提交id
    sid = models.IntegerField()
    #
    cid = models.IntegerField()
    pid = models.IntegerField()
    status = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'balloon'


# 练习提交
class Custominput(models.Model):
    solution_id = models.IntegerField(primary_key=True)
    # 放你自己提供的测试数据
    input_text = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'custominput'


# 站内信
class Mail(models.Model):
    mail_id = models.AutoField(primary_key=True)
    to_user = models.CharField(max_length=48)
    from_user = models.CharField(max_length=48)
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True, null=True)
    new_mail = models.IntegerField()
    reply = models.IntegerField(blank=True, null=True)
    in_date = models.DateTimeField(blank=True, null=True)
    defunct = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'mail'


# 看用户在线
class Online(models.Model):
    hash = models.CharField(primary_key=True, max_length=32)
    ip = models.CharField(max_length=46)
    ua = models.CharField(max_length=255)
    refer = models.CharField(max_length=255, blank=True, null=True)
    lastmove = models.IntegerField()
    firsttime = models.IntegerField(blank=True, null=True)
    uri = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'online'


# 把自己交的代码打印出来
class Printer(models.Model):
    printer_id = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=48)
    in_date = models.DateTimeField()
    status = models.SmallIntegerField()
    worktime = models.DateTimeField(blank=True, null=True)
    printer = models.CharField(max_length=16)
    content = models.TextField()

    class Meta:
        managed = False
        db_table = 'printer'


class Privilege(models.Model):
    # 用户
    user_id = models.CharField(max_length=48)
    # 权限
    rightstr = models.CharField(max_length=30)
    # 是否启用
    defunct = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'privilege'


# 讨论板
class Reply(models.Model):
    rid = models.AutoField(primary_key=True)
    author_id = models.CharField(max_length=48)
    time = models.DateTimeField()
    content = models.TextField()
    topic_id = models.IntegerField()
    status = models.IntegerField()
    ip = models.CharField(max_length=46)

    class Meta:
        managed = False
        db_table = 'reply'


class ShareCode(models.Model):
    share_id = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=48, blank=True, null=True)
    share_code = models.TextField(blank=True, null=True)
    language = models.CharField(max_length=32, blank=True, null=True)
    share_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'share_code'


class Sim(models.Model):
    # 查的是谁
    s_id = models.IntegerField(primary_key=True)
    # 和谁重了
    sim_s_id = models.IntegerField(blank=True, null=True)
    # 查重结果
    sim = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sim'


class Topic(models.Model):
    tid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=60)
    status = models.IntegerField()
    top_level = models.IntegerField()
    cid = models.IntegerField(blank=True, null=True)
    pid = models.IntegerField()
    author_id = models.CharField(max_length=48)

    class Meta:
        managed = False
        db_table = 'topic'


