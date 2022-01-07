import requests
from celery import shared_task
from .models import Test, Position
from .utils import generate_random_id
from .views import home
import logging

logger = logging.getLogger('__name__')
# from celery.decorators import periodic_task
# from celery.task.schedules import crontab

@shared_task
def create_test_object(name):
    Test.objects.create(name=name)
    logger.info("**LOGGED INFO**")
    add_code.delay()
    print("YESS")

# @periodic_task(run_every=(crontab(minute='*/1')))
# def run_create_objs():
#     create_test_object.delay(name='new2020')

@shared_task
def add_code():
    for i in Test.objects.all():
        i.code=generate_random_id()
        i.save()

# @shared_task
# def refresh():
#     home()
    # url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=INR&order=market_cap_desc&per_page=100&page=1&sparkline=false'
    # data = requests.get(url).json()
    # # return HttpResponse(data)

    # context = {'data': data}
    # print(data)

@shared_task
def fresh_data():

    logger.info("Update of Data Started")
    url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=INR&order=market_cap_desc&per_page=100&page=1&sparkline=false'
    data = requests.get(url).json()

    for item in data:
        p, _ = Position.objects.get_or_create(name=item['name'])
        print("__",p)
        print("__",_)   
        p.image = item['image']
        p.price = item['current_price']
        p.rank = item['market_cap_rank']
        p.market_cap = item['market_cap']
        p.save()
    
    logger.info("Update of Data Ended")

