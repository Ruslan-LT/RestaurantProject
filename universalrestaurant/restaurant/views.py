from django.http import HttpResponseNotFound, HttpResponse

def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Сторінку не знайдено 😕</h1>")

def main_page(request):
    return HttpResponse('<h1>Головна сторінка</)h1>')

