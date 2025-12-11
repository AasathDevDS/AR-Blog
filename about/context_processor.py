from .models import Links

def get_link(request):
  links = Links.objects.all()
  return dict(links=links)