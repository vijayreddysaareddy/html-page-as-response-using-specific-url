from django.urls import path
from app1.views import *
app_name='something1'
urlpatterns=[
    path('assign1/',assign1,name='assign1'),
    path('assign2/',assign2,name='assign2'),
    path('assign3/',assign3,name='assign3'),
]