from django.http import HttpResponse

def index(request):
    return HttpResponse("오늘 운동은 하체 입니다!!")