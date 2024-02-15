from rest_framework import status
from rest_framework.response import Response
from rest_framework import filters
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from contents.serializers import ContentSerializer
from contents.models import ContentCategory,Content
from django.db import transaction
from accounts.constants import USER_ROLES




##### HERE WE CAN ALSO USE MODELVIEWSET AND ROUTER #####

class ContentListCreateAPIView(ListCreateAPIView):

    """" List and Create Contents """

    serializer_class = ContentSerializer
    queryset = Content.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['title','body','summary','category__name']

    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.queryset)
        if request.user.user_role == USER_ROLES.AUTHOR:
            queryset = queryset.filter(author=request.user)
        data = self.serializer_class(queryset,many=True).data
        return Response(data,status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        user = request.user
        if user.user_role == USER_ROLES.AUTHOR:
            file = request.FILES['documents']
            categories = request.data['category']
            with transaction.atomic():
                content = Content.objects.create(title=request.data['title'],body=request.data['body'],\
                                                summary=request.data['summary'],author=user,documents=file)
                for category in categories:
                    content.category.add(ContentCategory.objects.get(pk=category))
            data = self.serializer_class(content).data
            return Response(data,status=status.HTTP_201_CREATED)
        return Response({"message":"Admin cannot create content"},status=status.HTTP_400_BAD_REQUEST)
    
class ContentUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):

    """" Retrive,Update and Delete Contents """
    
    serializer_class = ContentSerializer
    queryset = Content.objects.all()

    def get(self, request,pk, *args, **kwargs):
        queryset = self.queryset.filter(pk=pk)
        if request.user.user_role == USER_ROLES.AUTHOR:
            queryset = queryset.filter(author=request.user)
        data = self.serializer_class(queryset, many=True).data
        return Response(data, status=status.HTTP_200_OK)
     

    def patch(self, request, pk):
        content = self.queryset.filter(pk=pk)
        if request.user.user_role == USER_ROLES.AUTHOR:
            content = content.filter(author=request.user)
        if content:
                serializer = self.serializer_class(content[0], data=request.data, partial=True)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        return Response({"message":f"content with given id {pk} not available"}, status=status.HTTP_404_NOT_FOUND)
        
    
    def delete(self, request, pk):
        content = self.queryset.filter(pk=pk)
        if request.user.user_role == USER_ROLES.AUTHOR:
            content = self.queryset.filter(author=request.user)
        if content:
            content.delete()
            return Response(data={"message":"Content Deleted !"},status=status.HTTP_204_NO_CONTENT)
        return Response({"message": f"content with given id {pk} not available"},status=status.HTTP_404_NOT_FOUND)
    