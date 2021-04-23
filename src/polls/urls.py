from django.urls import path
from .views import index,detail

app_name="polls"
urlpatterns = [
    path('',index,name='index'),
    path('<int:i>/detail/',detail,name='detail'),
]
