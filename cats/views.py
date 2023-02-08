from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Cat
from .serializers import CatSerializer


class APICat(APIView):
    def get(self, request):
        cats = Cat.objects.all()
        serializer = CatSerializer(cats, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class APICatDetail(APIView):
    def get_object(self, id):
        try:
            return Cat.objects.get(id=id)
        except Cat.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request, id):
        cat = self.get_object(id)
        serializer = CatSerializer(cat)
        return Response(serializer.data)

    def put(self, request, id):
        cat = self.get_object(id)
        serializer = CatSerializer(cat, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, id):
        cat = self.get_object(id)
        serializer = CatSerializer(cat, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        cat = self.get_object(id)
        cat.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





# @api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
# def cat_detail(request, id):
#     cat = Cat.objects.get(id=id)
#     if request.method == 'PUT' or request.method == 'PATCH':
#         serializer = CatSerializer(cat, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         cat.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#     serializer = CatSerializer(cat)
#     return Response(serializer.data)

