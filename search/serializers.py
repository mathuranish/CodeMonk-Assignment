from rest_framework import serializers
from .models import Paragraph


class ParagraphSerializer(serializers.ModelSerializer):

    # serialising model data
    class Meta:
        model = Paragraph
        fields = ["id", "paragraph", "created", "author"]
