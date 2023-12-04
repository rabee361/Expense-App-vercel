from django.urls import path
from .views import *


urlpatterns = [
    path('main/', main, name="main"),
    path('chart/filter-options/', get_filter_options, name="chart-filter-options"),
    path('chart/pie-chart/<int:year>/' , pie , name="expense-types"),
    path('chart/line-chart/<int:year>/' , line , name="expense-type"),

]
