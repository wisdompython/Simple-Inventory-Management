from rest_framework import serializers
from rest_framework.validators import ValidationError
from .models import *


class InventoryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryItems
        fields = '__all__'

    
    
    def create(self, validated_data):
        suppliers  = validated_data.pop('suppliers', None)
        item = InventoryItems.objects.create(**validated_data)
        if suppliers is not None:
            item.suppliers.set(suppliers)
            item.save()
            return item
    
    
    def update(self, instance, validated_data):

        suppliers = validated_data.pop('suppliers',None)
        instance.item_name = validated_data.get('item_name', instance.item_name)
        instance.price = validated_data.get('price', instance.price)
        instance.item_description = validated_data.get('item_description', instance.item_description)
        if suppliers is not None:
            instance.suppliers.clear()
            instance.suppliers.set(suppliers)
        instance.save()
        return instance
        

class SuppliersSerializer(serializers.ModelSerializer):
    supplies = serializers.PrimaryKeyRelatedField(many=True, queryset=InventoryItems.objects.all())

    class Meta:
        model = Suppliers
        fields = ['id', 'name', 'address', 'phone_number', 'supplies']

    def validate(self, attrs):
        
        for supply in attrs['supplies']:
            if not InventoryItems.objects.filter(id=supply.id).exists():
                raise serializers.ValidationError({'error': 'Item does not exist'})
        return attrs

    def create(self, validated_data):
        
        supplies_data = validated_data.pop('supplies')
       
        supplier = Suppliers.objects.create(**validated_data)
        if supplies_data is not None:
            supplier.supplies.set(supplies_data)
        
            supplier.save()
        return supplier
    def update(self, instance, validated_data):
        supplies = validated_data.pop('supplies', None)
        if supplies is not None:
            instance.supplies.clear()
            instance.supplies.set(supplies)
        
        instance.name = validated_data.get('name', instance.name)
        instance.address = validated_data.get('address', instance.name)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.save()
        return instance


