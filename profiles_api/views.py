from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Return a list of APIView features"""
        an_apiview = [
        'Uses HTTP methods as function (get, patch, post, put, delete)',
        'Is similar to a traditional Django View',
        'Gives you the most control over your app',
        'I havent had infornation how to connect it to json format yet',
        ]

        return Response({'message':'Hi! Where have you been?','ap_apiview':an_apiview})
