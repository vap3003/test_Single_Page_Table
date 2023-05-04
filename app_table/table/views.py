from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Record
from .serializers import RecordSerializer


@api_view(['GET'])
def get_table(request):
    if request.method == 'GET':
        data = Record.objects.all()
        serializer = RecordSerializer(data, context={'request': request}, many=True)
        return Response(serializer.data)



# POSTS_ON_PAGE = 10


# def paginator(request, post_list):
#     paginator = Paginator(post_list, POSTS_ON_PAGE)
#     page_number = request.GET.get('page')
#     return paginator.get_page(page_number)


