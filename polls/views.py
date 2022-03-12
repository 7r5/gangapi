from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.template import loader
from .models import Question
from twilio.rest import Client
import datetime
import os

account = os.environ.get("APIACCOUNT")
token = os.environ.get("APIKEY")
print("@"*40)
print(account)
print(token)

client = Client(account, token)

                                 
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def hello(request):
    time_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='Easi pisi, now: %s'%time_now,      
                              to='whatsapp:+5214421114992')
    return HttpResponse(message.body)

def send_time(request, phone):
    time_now = datetime.datetime.now().strftime("%H:%M:%S")
    message = client.messages.create( 
                                from_='whatsapp:+14155238886',  
                                body='Easi pisi, Time: %s'%time_now,      
                                to='whatsapp:+521%s'%phone)
    return HttpResponse(message.body)