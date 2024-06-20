from django.shortcuts import render
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import *
from .serializers import *
from .models import *
# Create your views here.


class InventoryItemViewSet(viewsets.ViewSet):
    serializer_class = InventoryItemSerializer
    queryset = InventoryItems.objects.all()
    permission_classes = (IsAuthenticated,)
    def list(self, request):
        serializers  = self.serializer_class(self.queryset.all(), many=True)
        return Response(serializers.data)
    
    def create(self, request):
        serializers = self.serializer_class(data=request.data)

        if serializers.is_valid():
            serializers.save()

            return Response(serializers.data, status=HTTP_201_CREATED)
        return Response(serializers.errors, status=HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            item = get_object_or_404(self.queryset, pk=pk)
            serializer = self.serializer_class(item)

            return Response(serializer.data, status=HTTP_200_OK)
        except Exception as e:
            return Response({
                "error":str(e)
            }, status=HTTP_200_OK)

    

    def update(self, request, pk=None):
        item = get_object_or_404(self.queryset.all(), pk=pk)
        serializers = self.serializer_class(item, data=request.data, partial=True)

        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=HTTP_200_OK)
        return Response(serializers.errors, status=HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        item = get_object_or_404(self.queryset.all(), pk=pk)
        item.delete()
        return Response('Deleted', status=HTTP_204_NO_CONTENT)
    

class SuppliersViewSet(viewsets.ViewSet):
    queryset = Suppliers.objects.all()
    serializer_class = SuppliersSerializer
    permission_classes = (IsAuthenticated,)
    def list(self, request):
        try:
            self.queryset = Suppliers.objects.all()
            serializers  = self.serializer_class(self.queryset.all(), many=True)
            return Response(serializers.data)
        except Exception as e:
            return Response({'error':str(e)}, status=HTTP_400_BAD_REQUEST)
    
    def create(self, request):
        serializers = self.serializer_class(data=request.data)

        if serializers.is_valid():
            try:
                serializers.save()
                return Response(serializers.data)
            except Exception as e:
                return Response({'error':str(e)}, status=HTTP_400_BAD_REQUEST)
        return Response(serializers.errors, status=HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            supplier = get_object_or_404(self.queryset.all(), pk=pk)
            serializers = self.serializer_class(supplier)
            return Response(serializers.data, status=HTTP_200_OK)
        except Exception as e:
            return Response({
                'error': str(e)}, status=HTTP_400_BAD_REQUEST
            )
        
    def update(self, request, pk=None):
        supplier = get_object_or_404(self.queryset.all(), pk=pk)
        serializers = self.serializer_class(supplier, request.data, partial=True)
        if serializers.is_valid():
            try:
                serializers.save()
                return Response(serializers.data)
            except Exception as e:
                return Response({'error':str(e)}, status=HTTP_400_BAD_REQUEST)
        return Response(serializers.errors, status=HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        try:

            supplier = get_object_or_404(self.queryset.all(), pk=pk)
            supplier.delete()
            return Response('Deleted', status=HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({'error':str(e)}, status=HTTP_400_BAD_REQUEST)