from django.http import JsonResponse, Http404
from rest_framework.views import APIView
from core.api.serializers import BasketListSerializer, BasketSerializer, SubscriberSerializer
from core.models import Subscriber
from rest_framework.generics import CreateAPIView, ListCreateAPIView
from product.models import CartItems
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import status
from requests.models import Response


class SubscribeAPIView(CreateAPIView):
    serializer_class = SubscriberSerializer
    model = Subscriber



class CartItemsAPIView(ListCreateAPIView):
    queryset = CartItems.objects.all()
    serializer_class = BasketListSerializer


class CartItemsAPIView(APIView):

    def get(self,*args, **kwargs):
        items=CartItems.objects.all()
        serializer=BasketListSerializer(items,many=True,context={'request':self.request})
        return JsonResponse(data=serializer.data,safe=False)

    def post(self,*args, **kwargs):
        product_data=self.request.data
        serializer=BasketSerializer(data=product_data,context={'request':self.request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return JsonResponse(data=serializer.data,safe=False,status=201)


    def patch(self, request, *args, **kwargs):
        product_data=self.request.data
        product = CartItems.objects.filter(pk=kwargs.get('pk')).first()
        if not product:
            raise Http404
        serializer = BasketSerializer(data=product_data, instance=product,
                                            partial=True, context={'request': self.request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return JsonResponse(data=serializer.data, safe=False, status=201)


    def delete(self, request, *args, **kwargs):
        product = CartItems.objects.filter(pk=kwargs.get('pk')).first()
        if not product:
            raise Http404
        product.delete()
        return JsonResponse({'message': 'Item  deleted from basket successfully!'}, status=status.HTTP_204_NO_CONTENT)


