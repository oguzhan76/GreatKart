from .models import Category

def CategoriesMenuLinks(request):
    links = Category.objects.all()
    return dict(links=links) # Now this links is reachable in every template