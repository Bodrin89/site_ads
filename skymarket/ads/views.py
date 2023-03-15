
from rest_framework import pagination, viewsets
from rest_framework.viewsets import ModelViewSet

from ads.models import Ad, Comment
from ads.serializers import AdSerializer, AdMeSerializer, CommentSerializer
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser, AllowAny


class AdPagination(pagination.PageNumberPagination):
    pass


class AdViewSet(ModelViewSet):
    """Получение всех объявлений"""
    queryset = Ad.objects.all().order_by('-created_at')
    serializer_class = AdSerializer

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]


class AdMeAPIView(viewsets.ModelViewSet):
    """Получение и редактирование объявлений пользователя"""
    def get_queryset(self):
        author = self.request.user.pk
        return Ad.objects.prefetch_related('author').filter(author_id=author).order_by('title')

    def perform_create(self, serializer):
        return serializer.save(author_id=self.request.user.pk)

    # def get_permissions(self):
    #     if self.action == 'list':
    #         permission_classes = [AllowAny]
    #     else:
    #         permission_classes = [IsAuthenticated]
    #     return [permission() for permission in permission_classes]
    #
    # serializer_class = AdMeSerializer


class CommentViewSet(viewsets.ModelViewSet):

    """Создание и редактирование комментария к объявлению"""
    def get_queryset(self):
        ad_id = self.kwargs.get("ad_pk")
        return Comment.objects.select_related('author', 'ad').filter(ad_id=ad_id).order_by('-created_at')

    def perform_create(self, serializer):
        return serializer.save(author_id=self.request.user.pk, ad_id=self.kwargs.get("ad_pk"))

    serializer_class = CommentSerializer














