from django.db import models


class Solution(models.Model):
    solution_id = models.AutoField(primary_key=True)
    problem_id = models.IntegerField()
    user_id = models.CharField(max_length=48)
    nick = models.CharField(max_length=20)
    # 一共用了多少时间
    time = models.IntegerField(null=True)
    # 用了多少内存
    memory = models.IntegerField(null=True)
    # 什么时候提交的
    in_date = models.DateTimeField()
    # 结果
    result = models.SmallIntegerField()
    # 语言
    language = models.PositiveIntegerField()
    # 提交ip
    ip = models.CharField(max_length=46)
    # 竞赛编号
    contest_id = models.IntegerField(blank=True, null=True)
    # 代码是否合法默认是1， 没用到
    valid = models.IntegerField()
    # 如果竞赛id有的话，它是那一道题
    num = models.IntegerField(null=True)
    # 代码长度
    code_length = models.IntegerField()
    # 什么时候评测的
    judgetime = models.DateTimeField(blank=True, null=True)
    # 通过率
    pass_rate = models.DecimalField(max_digits=3, decimal_places=2, null=True)
    # 都给0，内核不用
    lint_error = models.PositiveIntegerField()
    # 谁判的，内核给的，先随便填一个admin，然后判题机覆盖
    judger = models.CharField(max_length=16)

    class Meta:
        # managed = False
        db_table = 'solution'


class Runtimeinfo(models.Model):
    # 提交id
    solution_id = models.IntegerField(primary_key=True)
    # 出了什么错误
    error = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'runtimeinfo'


class Compileinfo(models.Model):
    solution_id = models.IntegerField(primary_key=True)
    error = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'compileinfo'


class SourceCode(models.Model):
    solution_id = models.IntegerField(primary_key=True)
    # 提交的代码
    source = models.TextField()

    class Meta:
        managed = False
        db_table = 'source_code'


class SourceCodeUser(models.Model):
    solution_id = models.IntegerField(primary_key=True)
    # 提交的代码，同上
    source = models.TextField()

    class Meta:
        managed = False
        db_table = 'source_code_user'

