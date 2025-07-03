
from .models import Categorie

def get_links(request):
    links = Categorie.objects.all()
    return dict(link=links)