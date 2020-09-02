from django.db import models


class Contest(models.Model):
    contest_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    defunct = models.CharField(max_length=1)
    description = models.TextField(blank=True, null=True)
    # 1是私有，0是公开
    private = models.IntegerField()
    # 语言的掩码
    langmask = models.IntegerField()
    # 密码
    password = models.CharField(max_length=16)
    # 创建的人的id
    user_id = models.CharField(max_length=48)

    class Meta:
        managed = False
        db_table = 'contest'


class ContestProblem(models.Model):
    problem_id = models.IntegerField()
    contest_id = models.IntegerField(blank=True, null=True)
    # 在这次比赛中的标题
    title = models.CharField(max_length=200)
    # A->0 B C D E
    num = models.IntegerField()
    # 这场比赛这道题的ac次数
    c_accepted = models.IntegerField()
    # 这场比赛这道题的总提交次数
    c_submit = models.IntegerField()

    class Meta:
        db_table = 'contest_problem'



