from rest_framework import serializers

from social.models import Post, Comment, UserProfile


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):

    comments = CommentSerializer(many=True)

    author = serializers.ReadOnlyField(source='author.username')
    title = serializers.CharField(required=True)
    slug = serializers.SlugField(required=True)
    body = serializers.CharField(required=True)
    photo = serializers.ImageField(required=True)
    created_at = serializers.DateTimeField(required=True)

    class Meta:
        model = Post
        fields = (
            'id', 'author', 'title', 'slug', 'body', 'photo', 'created_at', 'comments'
        )


class UserProfileSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='profile.username')
    name = serializers.CharField(required=True)
    bio = serializers.CharField(required=True)
    birth_date = serializers.TimeField(required=True)
    location = serializers.CharField(required=True)
    picture = serializers.ImageField(required=True)

    class Meta:
        model = UserProfile
        fields = (
            'id', 'user', 'name', 'bio', 'birth_date', 'location', 'picture'
        )