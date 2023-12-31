from rest_framework.response import Response
from rest_framework.views import APIView
from test_app.models import Item
from utils.charts import months , types, colorPrimary, colorSuccess, colorDanger, generate_color_palette, get_year_dict , get_type_dict
from utils.charts import *
from django.db.models.functions import ExtractYear, ExtractMonth
from django.db.models import Avg, Max, Min, Sum , F
from .serializers import ItemSerializer

class Pie(APIView):
    def get(self,request,year):
        grouped_expenses = Item.objects.filter(time_purchased__year=year).\
                                        annotate(item_price=F("price")).values("expense_type").\
                                        annotate(sum=Sum("price"))\
                                        .values("expense_type","sum").distinct()
        types_dict = get_type_dict()
        for group in grouped_expenses:
            types_dict[group["expense_type"]] = round(group["sum"], 2)

        test_list = []
        for i in types_dict:
            test_dict = {}
            test_dict['name'] = i
            test_dict['value'] = types_dict[i]
            test_list.append(test_dict)


        return Response({
                "data": test_list,
                }
        )


class Line(APIView):
    def get(self,request, year):
        grouped_expenses = Item.objects.filter(time_purchased__year=year).\
                                        annotate(item_price=F("price")).\
                                        annotate(month=ExtractMonth("time_purchased")).\
                                        values("month").annotate(sum=Sum("price")).\
                                        values("month", "sum").order_by("month")
        sales_dict = get_year_dict()

        for group in grouped_expenses:
            sales_dict[months[group["month"]-1]] = group["sum"]

        return Response({
                         "data": sales_dict}
                         )




class Test(APIView):
    def get(self,request):
        exp = Item.objects.all()[:50]
        serializer = ItemSerializer(exp , many=True)
        return Response(serializer.data)