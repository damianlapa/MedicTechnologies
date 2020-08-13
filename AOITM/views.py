from django.shortcuts import render, redirect
from django.views import View
from AOITM.models import UserToken
from django.contrib.auth.models import User
from django.core.mail import send_mail
import random
import os


# own functions
def create_token(token_length):
    low_letters = 'qwertyuiopasdfghjklzxcvbnm'
    upper_letters = low_letters.upper()
    numbers = '0123456789'
    signs = low_letters + upper_letters + numbers
    token = ''
    for _ in range(0, token_length):
        token += str(signs[random.randint(0, len(signs) - 1)])

    return token


class LandingPage(View):

    def get(self, request):
        foundations = []
        organizations = []
        local_collections = []
        return render(request, 'index.html', locals())


class Register(View):

    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password == password2:
            new_user = User.objects.create_user(username=email, email=email, password=password, first_name=name,
                                                last_name=surname,
                                                is_active=False)
            user_token = create_token(16)
            UserToken.objects.create(user=new_user, token=user_token)

            html = """\
                        <html>
                          <body>
                            <p>Hi,<br>
                               Congratulations for create new account! Enter this link to activate your account: <br>
                               <a href="{}/{}">Activate Your Account</a>
                            </p>
                          </body>
                        </html>
                        """.format(os.environ.get('ACTIVATE_LINK'), user_token)

            send_mail('New Account', '', 'Charity Donation', (email,), html_message=html)

            return redirect('landing-page')
