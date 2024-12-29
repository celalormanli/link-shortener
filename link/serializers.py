from rest_framework import serializers
from link.models import Link

class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = "__all__"
        read_only_fields = ("shorted_link", "redirect_counter", "api_key")

