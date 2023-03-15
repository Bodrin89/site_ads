from rest_framework import serializers


# TODO Сериалайзеры. Предлагаем Вам такую структуру, однако вы вправе использовать свою
from rest_framework.fields import SerializerMethodField
from rest_framework.response import Response

from ads.models import Ad, Comment
from users.models import User


class CommentSerializer(serializers.ModelSerializer):
    # TODO сериалайзер для модели

    author = serializers.SlugRelatedField(read_only=True, slug_field="pk")
    ad = serializers.SlugRelatedField(read_only=True, slug_field="pk")

    class Meta:
        model = Comment
        fields = '__all__'


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = '__all__'


class AdMeSerializer(serializers.ModelSerializer):

    author = serializers.SlugRelatedField(read_only=True, slug_field="pk")

    class Meta:
        model = Ad
        fields = '__all__'


