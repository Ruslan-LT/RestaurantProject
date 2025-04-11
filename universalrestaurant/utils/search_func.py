from dishes.models import Dishes
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank, SearchHeadline
from django.db.models import Q
def q_serarch(query):
    vector = SearchVector('name','description')
    query = SearchQuery(query)
    result =  Dishes.objects.annotate(rank=SearchRank(vector,query)).filter(rank__gt=0).order_by('-rank')

    result = result.annotate(headline=SearchHeadline("name", query,
                                                     start_sel='<span style="background-color:yellow;">',
                                                     stop_sel='</span>'))

    result = result.annotate(bodyline=SearchHeadline("description", query,
                                                     start_sel='<span style="background-color:yellow;">',
                                                     stop_sel='</span>'))
    return result


    # keywords = [word for word in query.split() if len(word) > 2]
    #
    # q_obj = Q()
    #
    # for token in keywords:
    #     q_obj |= Q(description__icontains=token) | Q(name__icontains=token)
    #
    # return Dishes.objects.filter(q_obj)