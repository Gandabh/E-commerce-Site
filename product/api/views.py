from django.http import JsonResponse, Http404
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAuthenticated
from product.api.serializers import CategoryCreateSerializer, CategoryListSerializer, CategorySerializer, LikedItemSerializer, LikedItemListSerializer, ProductListSerializer, ProductSerializer
from product.models import Category,Product
from rest_framework.generics import ListCreateAPIView
from product.models import Category, Product, Wishlist
from rest_framework import status



class CategoriesAPIView(ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Category.objects.filter(is_published=True)
    serializer_class = CategoryListSerializer


class CategoryAPIView(APIView):
    def get(self, *args, **kwargs):
        category = Category.objects.filter(pk=kwargs.get('pk')).first()
        if not category:
            raise Http404
        serializer =CategoryListSerializer(category, context={'request': self.request})
        return JsonResponse(data=serializer.data, safe=False)


    def put(self, request, *args, **kwargs):
        category_data = self.request.data
        category = Category.objects.filter(pk=kwargs.get('pk')).first()
        if not category:
            raise Http404
        serializer = CategoryCreateSerializer(data=category_data, instance=category, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return JsonResponse(data=serializer.data, safe=False, status=201)


    def patch(self, request, *args, **kwargs):
        category_data = self.request.data
        category = Category.objects.filter(pk=kwargs.get('pk')).first()
        if not category:
            raise Http404
        serializer = CategoryCreateSerializer(data=category_data, instance=category,
                                            partial=True, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return JsonResponse(data=serializer.data, safe=False, status=201)


    def delete(self, request, *args, **kwargs):
        category = Category.objects.filter(pk=kwargs.get('pk')).first()
        if not category:
            raise Http404
        category.delete()
        return JsonResponse(safe=False, status=201)




class ProductAPIView(APIView):

    permission_classes=(IsAuthenticatedOrReadOnly,)

    def get(self,*args, **kwargs):
        products=Product.objects.all()
        serializer=ProductListSerializer(products,many=True,context={'request':self.request})
        return JsonResponse(data=serializer.data,safe=False)

    def post(self,*args, **kwargs):
        story_data=self.request.data
        serializer=ProductSerializer(data=story_data,context={'request':self.request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return JsonResponse(data=serializer.data,safe=False,status=201)

    

class ProductDetailAPIView(APIView):

    def get(self,*args, **kwargs):
        product=Product.objects.filter(pk=kwargs.get('pk')).first()
        if not product:
            raise Http404
        serializer=ProductListSerializer(product,context={'request':self.request})
        return JsonResponse(data=serializer.data,safe=False)


    def delete(self, request, *args, **kwargs):
        product = Product.objects.filter(pk=kwargs.get('pk')).first()
        if not product:
            raise Http404
        product.delete()
        return JsonResponse(safe=False, status=201)


    def put(self, request, *args, **kwargs):
        category_data = self.request.data
        product = Product.objects.filter(pk=kwargs.get('pk')).first()
        if not product:
            raise Http404
        serializer = ProductSerializer(data=category_data, instance=product, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return JsonResponse(data=serializer.data,safe=False,status=201)




class LikedItemsAPIView(ListCreateAPIView):
    queryset = Wishlist.objects.all()
    serializer_class = LikedItemListSerializer
    

class LikedItemsAPIView(APIView):

    def get(self,*args, **kwargs):
        items=Wishlist.objects.all()
        serializer=LikedItemListSerializer(items,many=True,context={'request':self.request})
        return JsonResponse(data=serializer.data,safe=False)

    def post(self,*args, **kwargs):
        product_data=self.request.data
        serializer=LikedItemSerializer(data=product_data,context={'request':self.request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return JsonResponse(data=serializer.data,safe=False,status=201)


    def delete(self, request, *args, **kwargs):
        product = Wishlist.objects.filter(pk=kwargs.get('pk')).first()
        if not product:
            raise Http404
        product.delete()
        return JsonResponse({'message': 'Item was deleted from Wishlist successfully!'}, status=status.HTTP_204_NO_CONTENT)

