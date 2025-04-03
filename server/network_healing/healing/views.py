from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

DATA = [{"id": 1, "name": "Item 1"}, {"id": 2, "name": "Item 2"}]

def get_items(request):
    return JsonResponse(DATA, safe=False)

@csrf_exempt
def create_item(request):
    if request.method == "POST":
        body = json.loads(request.body)
        new_item = {"id": len(DATA) + 1, "name": body["name"]}
        DATA.append(new_item)
        return JsonResponse(new_item, status=201)