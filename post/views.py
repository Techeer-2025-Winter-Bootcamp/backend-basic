from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("설정이 완료되었습니다.")
