from django.shortcuts import render
from .models import *
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.template.loader import render_to_string
import json
from django.db.models import Avg
import requests

def home(request):
    args = {}
    args['main_service'] = MainService.objects.all()
    args['service_group'] = ServiceGroup.objects.all()
    args['price_table'] = PriceTable.objects.all()
    args['comments'] = Comment.objects.all()
    if len(args['comments']) > 0:
        args['comments_avg'] = round(list(args['comments'].aggregate(Avg('stars')).values())[0], 1)
    else:
        args['comments_avg'] = 0

    return render(request, 'home.html', args)


def success(request):
    return render(request, 'success.html')

@require_http_methods(["POST"])
def order(request):
    data = request.body.decode("utf-8")
    data = json.loads(json.loads(data))
    msg = '\n'.join(data)
    token = "5441075219:AAGkYgRGNXbMk0Bqa68wU_D7gIwfB2RW7Kk"
    chat_id = "-1001582747453"
    url = "https://api.telegram.org/bot"+token+"/sendMessage?chat_id="+chat_id+"&text=" + msg
    requests.get(url)
    return JsonResponse({'order':'success', 'url':'/success/'})


@require_http_methods(["POST"])
def comment(request):
    data = request.POST

    comment = Comment(
        stars = data['rate'],
        name =  data['first_name'],
        phone = data['phone'],
        service = MainService.objects.get(slug=data['service']),
        text = data['comment'],
    )
    comment.save()
    commentHTML = render_to_string('comments/comment__object.html', {'comment':comment})
    
    msg = "Комментарий\n"
    msg += "Оценка: " + str(comment.stars) + "\n"
    msg += "Телефон: " + str(comment.phone) + "\n"
    msg += "Услуга: " + str(comment.service) + "\n"
    msg += "Текст: " + str(comment.text) + "\n"
    
    token = "5441075219:AAGkYgRGNXbMk0Bqa68wU_D7gIwfB2RW7Kk"
    chat_id = "-1001582747453"
    url = "https://api.telegram.org/bot"+token+"/sendMessage?chat_id="+chat_id+"&text=" + msg
    requests.get(url)
    return JsonResponse({'html' : commentHTML })