from rest_framework import serializers

from .models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"
        read_only_fields = ['author',]


class CommentSerializer(serializers.ModelSerializer):
    # status_count = serializers.ReadOnlyField(sourse = 'get_status_count')

    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = ['author', 'post']