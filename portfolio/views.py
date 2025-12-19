from django.shortcuts import render
from .models import Contact
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def index(request):

    if request.method=="POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        contact = Contact(name=name,email=email,message=message)
        contact.save()
        send_mail(
            subject=f"New Contact Message from {name}",
            message=f"""
You have received a new message from.

Name: {name}
Email: {email}

Message:
{message}
            """,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=['ashishsikarwar268@gmail.com'],  # where you want to receive mail
            fail_silently=False,
        )
        from django.conf import settings

        print("EMAIL USER:", settings.EMAIL_HOST_USER)
        print("EMAIL PASS EXISTS:", settings.EMAIL_HOST_PASSWORD is not None)

    return render(request,'portfolio/index.html')
