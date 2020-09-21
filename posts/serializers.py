from rest_framework import serializers
from .models import Post, Vote


class PostSerializer(serializers.ModelSerializer):

    poster = serializers.ReadOnlyField(source='poster.username')
    poster_id = serializers.ReadOnlyField(source='poster.id')
    votes = serializers.SerializerMethodField()

    class Meta:
        model = Post  # 여기서 말하는 모델은 Post란다
        fields = ['id', 'title', 'url', 'poster', 'poster_id',
                  'created', 'votes']  # id는 필수니깐.장고레스트에는 무조건 다 있음

    def get_votes(self, post):
        return Vote.objects.filter(post=post).count()


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ['id', ]
