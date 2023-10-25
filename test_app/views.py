from django.shortcuts import render
from .models import *
from django.db.models import Sum , F
from django.conf import settings
from django.http import JsonResponse
from utils.charts import  generate_color_palette, get_type_dict
from utils.charts import *
from django.db.models import Q
from django.db.models.functions import ExtractYear
from utils.charts import *



def get_filter_options(request):
    grouped_expenses = Item.objects.annotate(year=ExtractYear("time_purchased")).\
                                    values("year").order_by("-year").\
                                    distinct()
    options = [expense["year"] for expense in grouped_expenses]
    return JsonResponse({
        "options": options,
    })



def expense_types(request,year):
    expenses = Item.objects.filter(time_purchased__year=year)
    grouped_expenses = expenses.annotate(item_price=F("price")).\
                                values("expense_type").annotate(average=Sum("price")).\
                                values("expense_type","average").distinct()

    types_dict = get_type_dict()

    for group in grouped_expenses:
        types_dict[group["expense_type"]] = round(group["average"], 2)

    return JsonResponse({
        "title": f"type od expenses in {year}",
        "data": {
            "labels": list(types_dict.keys()),
            "datasets": [{
                "label": "Amount (ل.س)",
                "backgroundColor": generate_color_palette(len(types_dict)),
                "borderColor": generate_color_palette(len(types_dict)),
                "data": list(types_dict.values()),
            }]
        },
    })



def main(request):
    context = {}
    return render(request, "main.html", context)




