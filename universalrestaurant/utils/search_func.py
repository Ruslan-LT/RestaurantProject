
from dishes.models import Dishes
from django.db.models import Q
def q_serarch(query):

    keywords = [word for word in query.split() if len(word) > 2]

    q_obj = Q()

    for token in keywords:
        q_obj |= Q(description__icontains=token) | Q(name__icontains=token)

    return Dishes.objects.filter(q_obj)