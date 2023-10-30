from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from api.serializers import UrlSerializer
from shortener.models import Url


class UrlViewSet(ModelViewSet):
    queryset = Url.objects.select_related('author')
    serializer_class = UrlSerializer
    permission_classes = (IsAuthenticated,)


class PostViewSet(...):
    ...

    
class CommentViewSet(...):

    def perform_create(...):
        ... # логика создания коммента к посту

    def get_queryset(...):
        ... # получить все комменты к посту через related_name