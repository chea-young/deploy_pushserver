from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import ImageData
from django.views.decorators.csrf import csrf_exempt
from firebase_admin import messaging

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

@csrf_exempt
def get_image(request):
    if(request.method == 'POST'):
        image = request.FILES.get("image")
        name = request.POST.get('name')
        image_type = request.POST.get('type')
        form = ImageData( image = image, name=name)
        form.save()
        print(image, name, image_type)
        render(request, '알림화면/push.html')
        if(image_type == 'acc'):
            send_to_firebase_cloud_messaging('acc', name)
            send_website2('acc', name)
            send_website3('acc', name)
    return  JsonResponse({'code': '0000', 'msg': '이미지 받았습니다.'}, status=200)

def send_to_firebase_cloud_messaging(type, image_name):
    registration_token = 'dEn7h6FyDEw:APA91bFvJa1wBNZyCwd7d5wkwrAuFm_Dh-ryAlSi0UO-f_dntQEK5G2W6vsqIBtz_QVwRdWJlf6__YFk48P6tJuXmx6-LW8vgoEefdhPpDvhQ6qnW12Sz8vLNdG49Fws9JakpSoa0B5u'
    """
    세종대로 사거리(37.570226, 126.976920),
    청계 2가 좌표 찾기 (37.569834, 127.002028)

    """
    if type == 'acc' :
        message = messaging.Message(
            data={
                'title':'조심하세요',
                'body':'경로에 교통사고가 났습니다. 주의하세요',
                'image_name' : image_name,
                'type' : 'acc',
                'cctv_id_x' : '37.570226',
                'cctv_id_y' : '126.976920',
            },
            token=registration_token,
        )
        response = messaging.send(message)
        print('Successfully sent message:', response)
    elif type == 'ob' :
        message = messaging.Message(
            data={
                'title':'조심하세요',
                'body':'경로의 도로에 장애물이 있습니다. 주의하세요',
                'image_name' : image_name,
                'type' : 'ob',
                'cctv_id_x' : '37.569834',
                'cctv_id_y' : '127.002028',
            },
            token=registration_token,
        )
        response = messaging.send(message)
        print('Successfully  sent message:', response)

def send_website3(type, image_name):
    registration_token = 'foAW7Z5gQd4:APA91bGvbmxUQsckO6uPdEAHkkan0F3RKeXpOb5M2C-xQIuiGsJG54QYu8ww5dkmqrn5aOrKAw9OYtrTLqIJAxUTVncmKi3o1WJtxILtr46WnIbTVDt86UOGHlmnMlZJcPqc7iB3KbeL'
    if type == 'acc' :
        message = messaging.Message(
            data={
                'title':'조심하세요',
                'body':'경로에 교통사고가 났습니다. 주의하세요',
                'cctv_id' : '1',
                'image_name' : image_name,
                'type' : 'acc',
                'cctv_id_x' : '37.570226',
                'cctv_id_y' : '126.976920',
            },
            token=registration_token,
        )
        response = messaging.send(message)
        print('Successfully sent message:', response)
    elif type == 'ob' :
        message = messaging.Message(
            data={
                'title':'조심하세요',
                'body':'경로의 도로에 장애물이 있습니다. 주의하세요',
                'cctv_id' : '1',
                'image_name' : image_name,
                'type' : 'ob',
                'cctv_id_x' : '37.569834',
                'cctv_id_y' : '127.002028',
            },
            token=registration_token,
        )
        response = messaging.send(message)
        print('Successfully  sent message:', response)
def send_website2(type, image_name):
    registration_token = 'e02A3b7dMwA:APA91bHMhP-TJsOfdjZksVXFBh9kEoLZ80a_kl0RooWsa7t1K5gE5zHlepZZPeeY7sz_JGoGwto-Az59jh1Kbrr_49PQmF7bPeM8ctuo3a01AG1jszik98eHThp3nw65Bnumr7-J-E_Y'
    if type == 'acc' :
        message = messaging.Message(
            data={
                'title':'조심하세요',
                'body':'경로에 교통사고가 났습니다. 주의하세요',
                'cctv_id' : '1',
                'image_name' : image_name,
                'type' : 'acc',
                'cctv_id_x' : '37.570226',
                'cctv_id_y' : '126.976920',
            },
            token=registration_token,
        )
        response = messaging.send(message)
        print('Successfully sent message:', response)
    elif type == 'ob' :
        message = messaging.Message(
            data={
                'title':'조심하세요',
                'body':'경로의 도로에 장애물이 있습니다. 주의하세요',
                'cctv_id' : '1',
                'image_name' : image_name,
                'type' : 'ob',
                'cctv_id_x' : '37.569834',
                'cctv_id_y' : '127.002028',
            },
            token=registration_token,
        )
        response = messaging.send(message)
        print('Successfully  sent message:', response)


@csrf_exempt
def start(request):
    return render(request,'알림화면/push.html')
