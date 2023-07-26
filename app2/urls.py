from django.urls import path
from app2.views import *
app_name='someting3'
urlpatterns=[
    path('work1/',work1,name='work1'),
    path('work2/',work2,name='work2'),
    path('work3/',work3,name='work3'),
]