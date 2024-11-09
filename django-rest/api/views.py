from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import ArticleSerializer, AuthorSerializer, ArticleSerializer2
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser,AllowAny
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from home.models import Article
from rest_framework import filters

# Create your views here.

#simple with nested serializer for authors
class UserViewSet(ListCreateAPIView):
    serializer_class = ArticleSerializer
    def get_queryset(self):
        return Article.objects.all().order_by('-date')

# with hyper link serializer for authors
class ArticleListHyper(ListCreateAPIView):
    serializer_class = ArticleSerializer2
    queryset = Article.objects.all()
    permission_classes = (AllowAny, )

class UserViewSetAuth(ListCreateAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all().order_by('-date')
    permission_classes = [IsAdminUser]

class UserViewSetAuthUpdate(RetrieveUpdateDestroyAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all().order_by('-date')
    permission_classes = [IsAdminUser]

class UserDetail(RetrieveAPIView):
    serializer_class = AuthorSerializer
    queryset = get_user_model()
    permission_classes = (AllowAny, )


class ArticleDetail(RetrieveAPIView): 
    serializer_class = ArticleSerializer
    queryset = Article.objects.all().order_by('-date')


# class RevokeToken(APIView):
#     permission_classes = [IsAdminUser]
#     authentication_classes = [TokenAuthentication]

#     def delete(self, request):
#         request.auth.delete()
#         return Response(status=204)


class ArticleListFilter(ListCreateAPIView):
    permission_classes = (AllowAny, )
    serializer_class = ArticleSerializer

    def get_queryset(self):
        queryset = Article.objects.all()
        status = self.request.query_params.get('status')
        if status is not None:
            queryset = Article.objects.all().filter(status = status)
        title = self.request.query_params.get('title')
        if title is not None:
            queryset = queryset.filter(title = title)
        return queryset


class ArticleListSearch(ListCreateAPIView):
    permission_classes = (AllowAny, )
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']

class ArticleListSearch2(ListCreateAPIView):
    permission_classes = (AllowAny, )
    serializer_class = ArticleSerializer 
    
    def get_queryset(self):
        queryset = Article.objects.all()
        search = self.request.query_params.get('search')
        if search is not None:
            queryset = queryset.filter(title__icontains = search)
        return queryset


class ArticleListOrder(ListCreateAPIView):
    permission_classes = (AllowAny, )
    serializer_class = ArticleSerializer 
    queryset = Article.objects.all()
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['date', 'status']

class ArticleListOrder2(ListCreateAPIView):
    permission_classes = (AllowAny, )
    serializer_class = ArticleSerializer 

    def get_queryset(self):
        queryset = Article.objects.all()
        ordering = self.request.query_params.get('ordering')
        if ordering is not None:
            queryset = queryset.order_by(ordering)
        return queryset
    


