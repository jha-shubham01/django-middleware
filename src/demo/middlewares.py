from django.http import JsonResponse, HttpResponse


def set_request_data(get_response):
    print('set_request_data middleware')

    def wrapper(request):
        print(f'post data={request.POST}')
        data = request.POST.get('number')
        request.POST = {'data': data}
        print(f'start of set_request_data')
        response = get_response(request)
        print(f'end of set_request_data')
        return response
    return wrapper


def check_even(get_response):
    print('check_even middleware')

    def wrapper(request):
        print('Start of check_even')
        number = request.POST.get('number')
        is_odd = False
        if number and int(number) % 2:
            return JsonResponse({"message": "Failed from the middleware",})
        response = get_response(request)
        print('End of check_even')
        return response
    return wrapper


class SetRequestData:
    def __init__(self, get_response):
        print('SetRequestData initalized')
        self.get_response = get_response

    def __call__(self, request):
        print(f'post data={request.POST}')
        data = request.POST.get('number')
        request.POST = {'data': data}
        print(f'start of SetRequestData')
        response = self.get_response(request)
        print(f'end of SetRequestData')
        return response


class CheckEvent:
    def __init__(self, get_response):
        print('CheckEvent initalized')
        self.get_response = get_response

    def __call__(self, request):
        print('Start of CheckEvent')
        number = request.POST.get('number')
        if number and int(number) % 2:
            return JsonResponse({"message": "Failed from the middleware",})
        request.POST = {'data': number}
        response = self.get_response(request)
        print('End of CheckEvent')
        return response

    def process_view(request, view_fun, *args, **kwargs):
        # This is called after Djagno figures which view to call
        # but this is called before the view is called.
        print("process_view of CheckEvent")
        return None
        # return JsonResponse({"msg" : "Returned from the Django middleware CheckEvent's process_view"})
        # return HttpResponse("Returned from the Django middleware CheckEvent's process_view")


    def process_exception(self, request, exception):
        # https://docs.djangoproject.com/en/4.2/topics/http/middleware/#process-exception
        print("Exception in CheckEvent")
        msg = str(exception)
        return JsonResponse({"msg": msg,}, status=400)

    # def process_template_response(request, response):
    #   This is called when response has render() method
