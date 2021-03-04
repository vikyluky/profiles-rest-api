from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers


class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Return a list of APIView features"""
        an_apiview = [
        'Uses HTTP methods as function (get, patch, post, put, delete)',
        'Is similar to a traditional Django View',
        'Gives you the most control over your app',
        'I havent had infornation how to connect it to json format yet',
        ]

        return Response({'message':'Hi! Where have you been?','ap_apiview':an_apiview})

    def post(self, request):
        """Create post request just for a test"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
