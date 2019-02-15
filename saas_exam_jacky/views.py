# -*- coding: utf-8 -*-
import datetime

from django.shortcuts import render
from common.mymako import render_json
import json

# Create your views here.


def api_test(request):
    data = {"username": request.user.username, "accesstime": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
    result = {"result": True, "message": "success", "data": data}
    return render_json(result)

