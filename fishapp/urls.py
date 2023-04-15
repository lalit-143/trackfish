from django.urls import path
from fishapp import views


urlpatterns = [
    path('<str:url>/<str:uid>', views.home, name='home'),
    path('/<str:url>', views.home2, name='home2'),
    path('saveloc/<str:lat>/<str:lng>', views.save_location, name="save_location"),
]