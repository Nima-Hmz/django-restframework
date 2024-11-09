from .views import UserViewSet, ArticleDetail, UserViewSetAuth, UserViewSetAuthUpdate, ArticleListFilter, ArticleListSearch, ArticleListSearch2, ArticleListOrder, ArticleListOrder2, UserDetail, ArticleListHyper
from django.urls import path, include   

app_name = "api"

urlpatterns = [
    path('', UserViewSet.as_view(), name='userapiview'),
    path('api/', UserViewSetAuth.as_view(), name='userapiauth'),
    path('2/<int:pk>/', UserViewSetAuthUpdate.as_view(), name='article_detail'),
    path('<int:pk>/', ArticleDetail.as_view(), name='article_detail'),
    # path("revoke/", RevokeToken.as_view(), name='api-revoke'),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('listfilter/', ArticleListFilter.as_view(), name='listfilter'),
    path('listsearch/', ArticleListSearch.as_view(), name='listsearch'),
    path('listsearch2/', ArticleListSearch2.as_view(), name='listsearch2'),
    path('listorder/', ArticleListOrder.as_view(), name='listorder'),
    path('listorder2/', ArticleListOrder2.as_view(), name='listorder2'),
    path('user/<int:pk>/', UserDetail.as_view(), name="userdetail"),
    path('hyperishere/', ArticleListHyper.as_view(), name="ArticleListHyper"),    


]