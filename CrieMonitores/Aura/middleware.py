from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout
import datetime

class RedirectIfAuthenticatedMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Si el usuario está autenticado y está intentando acceder a la página de inicio de sesión, redirigirlo
        if request.user.is_authenticated and request.path == reverse('login'):
            return HttpResponseRedirect(reverse('salas'))
        
        response = self.get_response(request)
        return response
    
class SessionTimeoutMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            last_activity = request.session.get('last_activity', None)
            if last_activity:
                last_activity = datetime.datetime.strptime(last_activity, '%Y-%m-%d %H:%M:%S')
                if (datetime.datetime.now() - last_activity).seconds > 360: # 120 seconds = timeout duration
                    logout(request)
            request.session['last_activity'] = current_time
        response = self.get_response(request)
        return response