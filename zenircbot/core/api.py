from rest_framework.decorators import api_view
from rest_framework.response import Response

from zenircbot.lib.schema import validate


@api_view(['POST'])
def submit(request):
    valid, errors = validate(request.DATA)
    return Response({
        'valid': valid,
        'errors': errors
    })
