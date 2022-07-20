from .models import category

def category_menu_links(request):
    categories_list = category.objects.all()
    return dict(categorieslist = categories_list)
 


