from django.shortcuts import render
from .models import *
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.template.loader import render_to_string
import json
from django.db.models import Avg
import urllib.request
import urllib.parse

def home(request):
    args = {}
    args['main_service'] = MainService.objects.all()
    args['service_group'] = ServiceGroup.objects.all()
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
    msg = urllib.parse.quote(msg)
    url = "https://api.telegram.org/bot1298743700:AAFKbVPDgPgG8aVO_gIPQ_1KRI6i6d9OhvY/sendMessage?chat_id=-1001304868389&text=" + msg
    contents = urllib.request.urlopen(url).read() 
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
    
    # TELEGRAM
    # msg = comment_type + ': ' + variant.get_absolute_url() + '\n'
    # msg += data['text']
    # msg = urllib.parse.quote(msg)
    # url = "https://api.telegram.org/bot817785032:AAG-Q3s8wRhyZbkoJScSPvE2XDrCVlgZKKA/sendMessage?chat_id=-1001490724377&text=" + msg
    # contents = urllib.request.urlopen(url).read() 
    # response = {'html' : commentHTML }
    return JsonResponse(response)