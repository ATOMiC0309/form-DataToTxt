from django.shortcuts import render
from django.http import HttpResponse, HttpRequest


def write_to_txt(file_name, *args):
    content = ""
    for arg in args:
        content += (str(arg) + " ")
    content += "\n"
    with open(f"{file_name}.txt", 'a') as file:
        file.write(content)


def for_book(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        book_name = request.POST.get('book_name')
        author = request.POST.get('author')
        pages = request.POST.get('pages')
    else:
        book_name = request.GET.get('book_name')
        author = request.GET.get('author')
        pages = request.GET.get('pages')

    context = {
        'book_name': book_name,
        'author': author,
        'pages': pages
    }
    if book_name or author or pages:
        write_to_txt("books", book_name, author, pages)
    return render(request, 'index.html', context=context)


def for_car(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        car_name = request.POST.get('car_name')
        color = request.POST.get('color')
        speed = request.POST.get('speed')
        brand = request.POST.get('brand')
        price = request.POST.get('price')
    else:
        car_name = request.GET.get('car_name')
        color = request.GET.get('color')
        speed = request.GET.get('speed')
        brand = request.GET.get('brand')
        price = request.GET.get('price')

    context = {
        'car_name': car_name,
        'color': color,
        'speed': speed,
        'brand': brand,
        'price': price
    }
    if car_name or color or speed or brand or price:
        write_to_txt("cars", car_name, color, speed, brand, price)
    return render(request, 'car.html', context=context)


def for_human(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        age = request.POST.get('age')
        lang = request.POST.get('lang')
        height = request.POST.get('height')
        weight = request.POST.get('weight')
        b_day = request.POST.get('day')
        address = request.POST.get('address')
    else:
        first_name = request.GET.get('first_name')
        last_name = request.GET.get('last_name')
        age = request.GET.get('age')
        lang = request.GET.get('lang')
        height = request.GET.get('height')
        weight = request.GET.get('weight')
        b_day = request.GET.get('day')
        address = request.GET.get('address')

    context = {
        'f_name': first_name,
        'l_name': last_name,
        'age': age,
        'lang': lang,
        'height': height,
        'weight': weight,
        'b_day': b_day,
        'address': address
    }
    write_to_txt('humans', first_name, last_name, age, lang, height, weight, b_day, address)
    return render(request, 'human.html', context)


def for_house(request):
    if request.method == 'POST':
        address = request.POST.get('address')
        type_h = request.POST.get('type')
        floor = request.POST.get('floor')
        price = request.POST.get('price')
    else:
        address = request.GET.get('address')
        type_h = request.GET.get('type')
        floor = request.GET.get('floor')
        price = request.GET.get('price')

    context = {
        'address': address,
        'type': type_h,
        'floor': floor,
        'price': price
    }
    write_to_txt('houses', address, type_h, floor, price)
    return render(request, 'house.html', context)
