from rest_framework import serializers
from .models import Post, Comment


class CommentSerializer(serializers.ModelSerializer):
    writer = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('writer', 'post')


class PostSerializer(serializers.ModelSerializer):
    writer = serializers.StringRelatedField(read_only=True)
    comment_count = serializers.IntegerField(source='comments.count', read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'writer', 'like_count', 'comment_count']
        read_only_fields = ('writer', 'like_count')
