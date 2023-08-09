from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Wishlist


class Wishlists(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        pass

    def pose(self, request):
        pass
