from rest_framework import viewsets, permissions

from .models import Info

from .serializers import InfoSerializer



# Bookrides Viewset

class InfoViewSet(viewsets.ModelViewSet):

    queryset = Info.objects.all()

    permission_classes = [

        permissions.AllowAny

    ]

    serializer_class = InfoSerializer