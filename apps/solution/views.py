from django.conf import settings
from django.views.decorators.http import require_GET, require_POST
from django.http import Http404
from django.utils.timezone import now as now_func

from utils import restful

from .models import Solution, SourceCode
from .serializers import SolutionListSerializer
from .forms import CreateSolutionForm



@require_GET
def solution_list(request):
    '''
        需要参数有：
            1. 页数（p）
            2. 结果
            3. 可选
                1）用户
    '''
    page = int(request.GET.get('p', 1))
    user_id = int(request.GET.get('user_id', 0))
    result = int(request.GET.get('result', 11))
    start = (page - 1) * settings.ONE_PAGE_SUBMISSION_COUNT
    end = start + settings.ONE_PAGE_SUBMISSION_COUNT

    if result == 11:
        if user_id == 0:
            solutions = Solution.objects.all()[start:end]
        else:
            solutions = Solution.objects.filter(user_id=user_id)[start:end]
    else:
        if user_id == 0:
            solutions = Solution.objects.filter(result=result)[start:end]
        else:
            solutions = Solution.objects.filter(user_id=user_id, result=result)
    serializer = SolutionListSerializer(solutions, many=True)
    data = serializer.data
    return restful.result(data=data)


@require_POST
def create_solution(request):
    form = CreateSolutionForm(request.POST)
    if form.is_valid():
        user_id = form.cleaned_data.get('user_id')
        problem_id = form.cleaned_data.get('problem_id')
        nick = form.cleaned_data.get('nick')
        language = form.cleaned_data.get('language')
        code = form.cleaned_data.get('code')
        contest_id = form.cleaned_data.get('contest_id')
        num = form.cleaned_data.get('num')
        code_length = len(code)
        in_date = now_func()

        # 获取用户的注册ip
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            reg_ip = x_forwarded_for.split(',')[-1].strip()
        else:
            reg_ip = request.META.get('REMOTE_ADDR')

        ip = reg_ip

        if int(contest_id) == 0:
            # 注意这里的result需要调整，看排队中用哪个数字代表？
            solution = Solution.objects.create(user_id=user_id, problem_id=problem_id,
                                               in_date=in_date, ip=ip, language=language,
                                               nick=nick, result=0, code_length=code_length,
                                               valid=1,judger="admin", lint_error=0)
        else:
            solution = Solution.objects.create(user_id=user_id, problem_id=problem_id,
                                               in_date=in_date, ip=ip, language=language,
                                               nick=nick, contest_id=contest_id, num=num,
                                               result=0, code_length=code_length, valid=1,
                                               judger="admin", lint_error=0)
        solution.save()

        sourcecode = SourceCode.objects.create(solution_id=solution.pk, source=code)
        sourcecode.save()

        return restful.ok()
    else:
        return restful.params_error(message=form.get_errors())
