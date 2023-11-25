from rest_framework import serializers
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import NewsArticle
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import NewsArticle


class NewsArticleListView(APIView):
    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            model = NewsArticle
            fields = '__all__'

    def get(self, request, pk=None):
        if pk is not None:
            try:
                # fetching articles with an upperlimit
                limit = int(request.GET.get('limit', pk))
                news_articles = NewsArticle.objects.all()[:limit]
                if(news_articles):
                    serializer = self.OutputSerializer(news_articles, many=True)
                    return Response({'data': serializer.data}, status=status.HTTP_200_OK)
                else:
                    return Response({'message': 'data not found'}, status=status.HTTP_400_BAD_REQUEST)
            except NewsArticle.DoesNotExist:
                return Response({'message': 'NewsArticle model does not exist'}, status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                return Response({'message': str(e)}, status=status.HTTP_404_NOT_FOUND)
        else:
            try:
                # fetching default=50 Articles from db
                limit = int(request.GET.get('limit', 5))  # Default limit is 50, adjust as needed
                news_articles = NewsArticle.objects.all()[:limit]
                if(news_articles):
                    serializer = self.OutputSerializer(news_articles, many=True)
                    # context = {'news_articles': serializer.data}
                    # return render(request, 'index.html', context) 
                    return Response({'data': serializer.data}, status=status.HTTP_200_OK)
                else:
                    return Response({'message': 'Data not found'}, status=status.HTTP_400_BAD_REQUEST)
                
            except Exception as e:
                return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)



  



