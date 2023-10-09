from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.status import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework.settings import *
from app.models import *
from .permissions import *
from .serializers import *

@api_view(['GET', 'POST'])
@permission_classes([UserPermission])
def user(request):
    if request.method == "GET":
        user = User.objects.all()
        serializer = UserSerializers(user, many=True, context = {'request': request})
        return Response(serializer.data, status=HTTP_200_OK)
    elif request.method == 'POST':
        serializer = UserSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = HTTP_201_CREATED)
        return Response(serializer.errors, status = HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT', 'DELETE'])
@permission_classes([UserDetailPermissions])
def user_detail(request, pk):
    user = User.objects.get(pk=pk)

    if request.method == 'GET':
        serializer = UserSerializers(user)
        return Response(serializer.data, status=HTTP_202_ACCEPTED)
    elif request.method == 'PUT':
        serializer = UserSerializers(user,data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_202_ACCEPTED)
        return Response(serializer.errors, status = HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        user.delete()
        return Response(status=HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
@permission_classes([PostPermissions])
def post(request):
    if request.method == "GET":
        post = Post.objects.all()
        serializer = PostSerializers(post, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
    elif request.method == 'POST':
        serializer = PostSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = HTTP_201_CREATED)
        return Response(serializer.errors, status = HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT', 'DELETE'])
@permission_classes([PostDetailPermissions])
def post_detail(request, pk):
    post = Post.objects.get(pk=pk)

    if request.method == 'GET':
        serializer = PostSerializers(post)
        return Response(serializer.data, status=HTTP_202_ACCEPTED)
    elif request.method == 'PUT':
        serializer = PostSerializers(post,data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_202_ACCEPTED)
        return Response(serializer.errors, status = HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        post.delete()
        return Response(status=HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
@permission_classes([CategoryPermissions])
def category(request):
    if request.method == "GET":
        category = Category.objects.all()
        serializer = CategoryPermissions(category, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
    elif request.method == 'POST':
        serializer = CategorySerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = HTTP_201_CREATED)
        return Response(serializer.errors, status = HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT', 'DELETE'])
@permission_classes([CategoryDetailPermissions])
def category_detail(request, pk):
    category = Category.objects.get(pk=pk)

    if request.method == 'GET':
        serializer = CategorySerializers(category)
        return Response(serializer.data, status=HTTP_202_ACCEPTED)
    elif request.method == 'PUT':
        serializer = CategorySerializers(category,data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_202_ACCEPTED)
        return Response(serializer.errors, status = HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        category.delete()
        return Response(status=HTTP_204_NO_CONTENT)



