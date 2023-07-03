from django.http import JsonResponse


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
