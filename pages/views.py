from django.http import JsonResponse


def index_view(request):
    return JsonResponse({"wazzup": "hacker!!!"})


