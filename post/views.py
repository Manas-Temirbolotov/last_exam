from rest_framework import generics
from rest_framework import viewsets
import telebot
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from .models import Post, Comment
from .permissions import IsAuthorPermission
from .serializers import PostSerializer, CommentSerializer


bot = telebot.TeleBot("5585848579:AAFZYNwS1y0h6Hige_8uFMnqoj6AU4P7zQ0", parse_mode=None)


class PostListCreateAPIView(generics.ListCreateAPIView, ):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthorPermission, ]
    filter_backends = [OrderingFilter, SearchFilter]
    search_fields = ['title', ]
    ordering_fields = ['created', ]

    def perform_create(self, serializer):
        obj = serializer.save(
            author=self.request.user.author
        )
        bot.send_message(535207177, f"Пост {obj.content} был успешно добавлен")


class PostRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthorPermission, ]


class CommentListCreateAPIView(generics.ListCreateAPIView,):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAdminUser, ]

    def get_queryset(self):
        return super().get_queryset().filter(post_id=self.kwargs.get('post_id'))

    def perform_create(self, serializer):
        obj = serializer.save(
            post_id=self.kwargs.get('post_id'),
            author=self.request.user.author
        )
        bot.send_message(535207177, f"Комментарий к посту {obj.text} был успешно добавлен")


class CommentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView,):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthorPermission, ]

    def get_queryset(self):
        return super().get_queryset().filter(post_id=self.kwargs.get('post_id'))