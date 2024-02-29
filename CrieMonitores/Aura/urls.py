from django.urls import path, include
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='/accounts/login/', permanent=False)),
    path('accounts/',include("django.contrib.auth.urls")),
    path('salas/', views.salas, name = "salas"),
    path('cubiculos/', views.cubiculos, name = "cubiculos"),

]

