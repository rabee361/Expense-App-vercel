from django.shortcuts import render
from .models import *
from django.db.models import Sum , F , Avg , Count
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



def pie(request,year):
    expenses = Item.objects.filter(time_purchased__year=year)
    grouped_expenses = expenses.annotate(item_price=F("price")).\
                                values("expense_type").annotate(average=Sum("price")).\
                                values("expense_type","average").distinct()

    types_dict = get_type_dict()

    for group in grouped_expenses:
        types_dict[group["expense_type"]] = round(group["average"], 2)

    return JsonResponse({
        "title": f"type of expenses in {year}",
        "data": {
            "key" : 3000,
            "labels": list(types_dict.keys()),
            "datasets": [{
                "label": "Amount (ل.س)",
                "backgroundColor": generate_color_palette(len(types_dict)),
                "borderColor": generate_color_palette(len(types_dict)),
                "data": list(types_dict.values()),
            }]
        },
    })

def line(request,year):
    expenses = Item.objects.filter(time_purchased__year=year)
    grouped_expenses = expenses.annotate(item_price=F("price")).\
                                values("expense_type").annotate(average=Sum("price")).\
                                values("expense_type","average").distinct()

    types_dict = get_type_dict()

    for group in grouped_expenses:
        types_dict[group["expense_type"]] = round(group["average"], 2)

    return JsonResponse({ 
        "data": types_dict,
    })



# @staff_member_required
# def payment_method_chart(request, year):
#     purchases = Item.objects.filter(time__year=year)
#     grouped_purchases = purchases.values("payment_method").annotate(count=Count("id"))\
#         .values("payment_method", "count").order_by("payment_method")

#     payment_method_dict = dict()

#     for payment_method in Item.PAYMENT_METHODS:
#         payment_method_dict[payment_method[1]] = 0

#     for group in grouped_purchases:
#         payment_method_dict[dict(Purchase.PAYMENT_METHODS)[group["payment_method"]]] = group["count"]

#     return JsonResponse({
#         "title": f"Payment method rate in {year}",
#         "data": {
#             "labels": list(payment_method_dict.keys()),
#             "datasets": [{
#                 "label": "Amount ($)",
#                 "backgroundColor": generate_color_palette(len(payment_method_dict)),
#                 "borderColor": generate_color_palette(len(payment_method_dict)),
#                 "data": list(payment_method_dict.values()),
#             }]
#         },
#     })






def main(request):
    context = {}
    return render(request, "main.html", context)




