from rest_framework import serializers

from ads.models import Ad, Comment


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(read_only=True, slug_field="pk")
    ad = serializers.SlugRelatedField(read_only=True, slug_field="pk")

    class Meta:
        model = Comment
        fields = '__all__'


class AdSerializer(serializers.ModelSerializer):
    pk = serializers.PrimaryKeyRelatedField(read_only=True)
    author = serializers.SlugRelatedField(read_only=True, slug_field="pk")

    class Meta:
        model = Ad
        fields = '__all__'


class AdMeSerializer(serializers.ModelSerializer):
    pk = serializers.PrimaryKeyRelatedField(read_only=True)
    author = serializers.SlugRelatedField(read_only=True, slug_field="pk")

    class Meta:
        model = Ad
        fields = '__all__'
