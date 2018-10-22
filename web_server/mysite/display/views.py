from django.shortcuts import render

from django.http import HttpResponse

import json
import redis

def index(request):
    pool = redis.ConnectionPool(host='127.0.0.1', port=6379)
    r = redis.StrictRedis(connection_pool=pool)
    displayData = r.zrangebyscore("mydata",1000000,9999999)
    for i, val in enumerate(displayData):
    	#byte==string to dict
    	displayData[i] = eval(val)
    #displayData = [{"ID":123456}]
    context = {"displayData":displayData}
    return render(request, 'display/index.html', context)

def findByID(request,id):
    pool = redis.ConnectionPool(host='127.0.0.1', port=6379)
    r = redis.StrictRedis(connection_pool=pool)
    displaySingleData = r.zrangebyscore("mydata",id,id)
    for i, val in enumerate(displaySingleData):
    	#byte==string to dict
    	displaySingleData[i] = eval(val)
    #displaySingleData = [{"ID":123456}]
    context = {"displaySingleData":displaySingleData}
    return render(request, 'display/displaySingleData.html', context)

