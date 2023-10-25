from django.urls import path
from .views import *


urlpatterns = [
    path('main/', main, name="main"),
    path('chart/filter-options/', get_filter_options, name="chart-filter-options"),
    path('chart/expense-types/<int:year>/' , expense_types , name="expense-types"),
]
