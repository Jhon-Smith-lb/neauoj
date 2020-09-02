from django.conf import settings
from django.views.decorators.http import require_GET
from django.http import Http404

from utils import restful

from .models import Problem
from .serializers import ProblemListSerializer, ProblemSerializer


@require_GET
def problems_list(request):
    '''
    需要参数有：
        1. 页数（p）
        2. 标签id（tag_id）
        3. 竞赛id（contest_id）
    '''
    page = int(request.GET.get('p', 1))
    start = (page - 1) * settings.ONE_PAGE_PROBLEM_COUNT
    end = start + settings.ONE_PAGE_PROBLEM_COUNT

    problems = Problem.objects.filter(defunct=0)[start:end]
    serializer = ProblemListSerializer(problems, many=True)
    data = serializer.data
    return restful.result(data=data)


@require_GET
def problem_detail(request, problem_id):
    '''
    需要一个参数：
        问题id(problem_id)， 如果找不到返回404页面
    '''
    try:
        problem = Problem.objects.filter(defunct=0).get(pk=problem_id)
        serializer = ProblemSerializer(problem)
        data = serializer.data
        return restful.result(data=data)
    except Problem.DoesNotExist:
        raise Http404




