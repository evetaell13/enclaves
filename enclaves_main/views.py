from django.shortcuts import render, redirect
#from django.contrib.auth.views import redirect_to_login
from django.conf import settings

# начальная страница
def index(request):
    if request.user.is_authenticated:
        return render(request, 'main/index.html')
    else:
        return redirect('%s' % (settings.LOGIN_URL))
