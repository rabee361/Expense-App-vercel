from django.contrib import admin
from django.urls import path
from .views import Pie , Line , Test


urlpatterns = [
    path('pie-chart/<int:year>' , Pie.as_view() , name="pie" ),
    path('line-chart/<int:year>' , Line.as_view() , name="line"),
    path('test/' , Test.as_view())
]
