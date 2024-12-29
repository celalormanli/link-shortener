from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_api_key.models import APIKey
from rest_framework_api_key.permissions import HasAPIKey
from django.http import HttpResponsePermanentRedirect
from django.db.models import F

from link.models import Link
from link.serializers import LinkSerializer
import uuid

class LinkViewSet(viewsets.ViewSet):
    permission_classes = [HasAPIKey]

    def create(self, request):
        serializer = LinkSerializer(data=request.data)
        key = request.META["HTTP_AUTHORIZATION"].split()[1]
        api_key = APIKey.objects.get_from_key(key)
        if serializer.is_valid():
            serializer.validated_data["shorted_link"] = uuid.uuid4().hex[:10]
            serializer.validated_data["api_key"] = api_key
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        key = request.META["HTTP_AUTHORIZATION"].split()[1]
        api_key = APIKey.objects.get_from_key(key)
        list_of_links = Link.objects.filter(api_key = api_key)
        serializer = LinkSerializer(list_of_links, many=True)
        return Response(serializer.data)

class LinkRedirectViewSet(APIView):
    permission_classes = []

    def get(self, request, *args, **kwargs):
        link = Link.objects.filter(shorted_link=kwargs["shorted_link"]).first()
        Link.objects.filter(shorted_link=kwargs["shorted_link"]).update(redirect_counter=F("redirect_counter") + 1)
        return HttpResponsePermanentRedirect(link.main_link)
