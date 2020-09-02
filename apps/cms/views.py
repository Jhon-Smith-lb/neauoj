from django.conf import settings
from django.views.decorators.http import require_GET, require_POST

from utils import restful

from .serializers import CmsUsersListSerializer
from .forms import CreateProblemForm, CreateContestForm, CreateContestProblemForm
from apps.problem.models import Problem
from apps.contest.models import Contest, ContestProblem
from apps.ojauth.models import Users

import os
import zipfile


@require_GET
def users_list(request):
    '''
        用户列表
        需要参数有：
            1. 页数（p）
        '''
    page = int(request.GET.get('p', 1))
    start = (page - 1) * settings.ONE_PAGE_USER_COUNT
    end = start + settings.ONE_PAGE_USER_COUNT

    users = Users.objects.filter(defunct=0)[start:end]
    serializer = CmsUsersListSerializer(users, many=True)
    data = serializer.data
    return restful.result(data=data)


@require_POST
def create_problem(request):
    form = CreateProblemForm(request.POST, request.FILES)
    if form.is_valid():
        title = form.cleaned_data.get('title')
        description = form.cleaned_data.get('description')
        input = form.cleaned_data.get('input')
        output = form.cleaned_data.get('output')
        sample_input = form.cleaned_data.get('sample_input')
        sample_output = form.cleaned_data.get('sample_output')
        spj = form.cleaned_data.get('spj')
        hint = form.cleaned_data.get('hint')
        source = form.cleaned_data.get('source')
        time_limit = form.cleaned_data.get('time_limit')
        memory_limit = form.cleaned_data.get('memory_limit')
        defunct = form.cleaned_data.get('defunct')
        file = form.cleaned_data.get('test_data')

        problem = Problem.objects.create(title=title, description=description, input=input,
                                         output=output, sample_input=sample_input,
                                         sample_output=sample_output,
                                         time_limit=time_limit,
                                         memory_limit=memory_limit, hint=hint,
                                         spj=spj, source=source,defunct=defunct)
        problem.save()

        # 创建以题目id为为名称的文件夹，用来存放.in和.out文件

        # 1. 创建路径
        filepath = settings.MEDIA_ROOT + '\\' + str(problem.problem_id) + '\\'
        os.mkdir(filepath)
        # 2.将压缩文件分块儿写入服务器指定位置
        filepath_name = os.path.join(filepath, file.name)
        print(filepath_name)
        destination = open(filepath_name, 'wb+')
        for chunk in file.chunks():
            destination.write(chunk)
        destination.close()
        zip_file = zipfile.ZipFile(filepath_name)
        zip_list = zip_file.namelist()              # 得到压缩包里所有文件
        for f in zip_list:
            zip_file.extract(f, filepath)           # 循环解压文件到指定目录
        zip_file.close()                            # 关闭文件，必须有，释放内存
        os.remove(filepath_name)
        return restful.ok()
    else:
        return restful.params_error(message=form.get_errors())


@require_POST
def create_contest(request):
    form = CreateContestForm(request.POST)
    if form.is_valid():
        title = form.cleaned_data.get('title')
        description = form.cleaned_data.get('description')
        start_time = form.cleaned_data.get('start_time')
        end_time = form.cleaned_data.get('end_time')
        password = form.cleaned_data.get('password')
        defunct = form.cleaned_data.get('defunct')
        private = form.cleaned_data.get('private')
        langmask = form.cleaned_data.get('langmask')

        contest = Contest.objects.create(title=title, description=description,
                                         start_time=start_time,
                                         end_time=end_time, password=password,
                                         user_id=request.user.user_id,
                                         defunct=defunct, private=private,
                                         langmask=langmask)
        contest.save()
        return restful.ok()
    else:
        return restful.params_error(message=form.get_errors())


@require_POST
def create_contest_problem(request):
    form = CreateContestProblemForm(request.POST)
    if form.is_valid():
        problem_id = form.cleaned_data.get('problem_id')
        contest_id = form.cleaned_data.get('contest_id')
        title = form.cleaned_data.get('title')
        # A->0 B C D E
        num = form.cleaned_data.get('num')
        # 这场比赛这道题的ac次数
        c_accepted = 0
        # 这场比赛这道题的总提交次数
        c_submit = 0

        contest_problem = ContestProblem.objects.create(problem_id=problem_id,
                                                        contest_id=contest_id,
                                                        title=title, num=num,
                                                        c_accepted=c_accepted,
                                                        c_submit=c_submit)
        contest_problem.save()
        return restful.ok()
    else:
        return restful.params_error(message=form.get_errors())

