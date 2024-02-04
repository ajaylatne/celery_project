from django.shortcuts import render
from .tasks import sub


# Create your views here.
def index(request):
    print('by using delay')
    result = sub.delay(20, 10)
    print('by using apply_async')
    result1 = sub.apply_async(args=[20, 10])
    return render(request, 'myapp/index.html', {"result": result})
