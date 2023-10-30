from rest_framework.serializers import ModelSerializer, CurrentUserDefault, PrimaryKeyRelatedField, SlugField

from shortener.models import Url, User
from shortener.utils import get_short_slug


class UrlSerializer(ModelSerializer):
    author = PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        default=CurrentUserDefault()
    )
    shorted_url = SlugField(required=False)

    class Meta:
        model = Url
        fields = '__all__'

    def create(self, validated_data):
        if validated_data.get('shorted_url') is None:
            validated_data['shorted_url'] = get_short_slug()
        return super().create(validated_data)