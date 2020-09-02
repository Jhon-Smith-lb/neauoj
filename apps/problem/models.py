from django.db import models


class Problem(models.Model):
    # 问题id
    problem_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    # 输入描述
    input = models.TextField(blank=True, null=True)
    # 输出描述
    output = models.TextField(blank=True, null=True)
    sample_input = models.TextField(blank=True, null=True)
    sample_output = models.TextField(blank=True, null=True)
    # 是否特判，1是特判
    spj = models.CharField(max_length=1)
    # 提示
    hint = models.TextField(blank=True, null=True)
    # 题目来源，也可以叫分类，一个题可以有多个来源
    source = models.CharField(max_length=100, blank=True, null=True)
    # 修改时间
    in_date = models.DateTimeField(blank=True, null=True)
    time_limit = models.IntegerField()
    memory_limit = models.IntegerField()
    defunct = models.CharField(max_length=1, default=0)
    accepted = models.IntegerField(blank=True, null=True)
    submit = models.IntegerField(blank=True, null=True)
    # 几个人解决了这道题
    solved = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'problem'


class Tag(models.Model):
    problem_id = models.CharField(max_length=48)
    title = models.CharField(max_length=50)

