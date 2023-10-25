    # x=list()
    # types = Item.objects.all().values("expense_type").distinct()
    # for i in types:
    #     x.append(i["expense_type"])
    # print(x)

types = ['Medicin','Transport','Food','Leisure','House&Renovations','Electronics','Cloths']
months = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
]
colorPalette = ["#55efc4", "#81ecec", "#a29bfe", "#ffeaa7", "#fab1a0", "#ff7675", "#fd79a8"]
colorPrimary, colorSuccess, colorDanger = "#79aec8", colorPalette[0], colorPalette[5]


def get_year_dict():
    year_dict = dict()

    for month in months:
        year_dict[month] = 0

    return year_dict

def get_type_dict():
    type_dict = dict()

    for expense_type in types:
        type_dict[expense_type] = 0

    return type_dict


def generate_color_palette(amount):
    palette = []

    i = 0
    while i < len(colorPalette) and len(palette) < amount:
        palette.append(colorPalette[i])
        i += 1
        if i == len(colorPalette) and len(palette) < amount:
            i = 0

    return palette