from django.urls import path,include
from .views import article_list,article_detail,ArticleApiview,ArticledetailApiview,GenericApiview,ArticleViewset,ArticleGenericviewset,ArticleModelviewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('article',ArticleModelviewset, basename="article")


urlpatterns = [
    path('viewset/',include(router.urls)),
    #path('article/',article_list),
    #path('article/',ArticleApiview.as_view()),
    path('article/<int:id>/',GenericApiview.as_view()),
    path('article_detail/<int:id>/',ArticledetailApiview.as_view())
]