from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from .serializers import CategorySerializer, QuestionAnswerSerializer, QuestionAnswerSerializerFull
from .models import Category, QuestionAnswer
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from django_filters.rest_framework import DjangoFilterBackend


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class QuestionAnswerListCreate(ListCreateAPIView):
    queryset = QuestionAnswer.objects.all()
    serializer_class = QuestionAnswerSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', ]

    def get_queryset(self):
        queryset = QuestionAnswer.objects.order_by('-importance')
        return queryset

    def perform_create(self, serializer):
        serializer.save()


class CategoryUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class QuestionAnswerUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = QuestionAnswer.objects.all()
    serializer_class = QuestionAnswerSerializerFull






