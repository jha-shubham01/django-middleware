from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def index(request):
    print('Index called', request.POST)
    raise Exception("Exception raised from the view")
    return JsonResponse({"message": "Shubham replied hello!"})
