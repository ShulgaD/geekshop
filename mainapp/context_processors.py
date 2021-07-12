from mainapp.models import ProductCategory


def menu(request):
    menu_list = ProductCategory.objects.all()
    return {
        'categoryes': menu_list
    }