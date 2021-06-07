from celery import shared_task
from django.core.mail import send_mail
from .models import RegisterationNewuser as User

@shared_task
def send_email(data):
    title = data["title"]
    link = data["link"]
    text = data["text"]


    send_mail(
        "Latest News from Africa!",
        str(title)+"\n"+str(text)+"\n"+str(link),
        "from@yourmail.com",
        [user.email for user in User.objects.all()]
    )
