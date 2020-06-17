import requests
import json
from django.http import HttpResponse

def countries_stat(request):
    
    data = {
            'status':'ok',
            'country':'colombia',
        }

    return HttpResponse(json.dumps(data))


