from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def index(request):
    print('Index called', request.POST)
    return JsonResponse({"message": "Shubham replied hello!"})
