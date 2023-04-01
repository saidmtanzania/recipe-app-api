"""
Core views api.
"""
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def health_check(request):
    """Return succesful response."""
    return Response({'healthy': True})