from django.conf import settings
from django.views.decorators.http import require_GET
from django.http import Http404

from utils import restful

from .models import Contest
from .serializers import ContestListSerializer, ContestSerializer


@require_GET
def contests_list(request):
    '''
    需要参数有：
        1. 页数（p）
    '''
    page = int(request.GET.get('p', 1))
    start = (page - 1) * settings.ONE_PAGE_CONTEST_COUNT
    end = start + settings.ONE_PAGE_CONTEST_COUNT

    contests = Contest.objects.filter(defunct=0)[start:end]
    serializer = ContestListSerializer(contests, many=True)
    data = serializer.data
    return restful.result(data=data)


@require_GET
def contest_detail(request, contest_id):
    '''
    需要一个参数：
        竞赛id(contest_id)， 如果找不到返回404页面
    '''
    try:
        contest = Contest.objects.filter(defunct=0).get(pk=contest_id)
        serializer = ContestSerializer(contest)
        data = serializer.data
        return restful.result(data=data)
    except Contest.DoesNotExist:
        raise Http404


