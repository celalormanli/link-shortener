from rest_framework import serializers
from link.models import Link


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ("main_link", "shorted_link", "redirect_counter")
        read_only_fields = ("shorted_link", "redirect_counter")
