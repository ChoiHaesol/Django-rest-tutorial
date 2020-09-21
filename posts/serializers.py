from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post  # 여기서 말하는 모델은 Post란다
        fields = ['id', 'title', 'url', 'poster',
                  'created']  # id는 필수니깐.장고레스트에는 무조건 다 있음
