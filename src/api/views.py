from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rabble.models import *
from .serializers import *

@api_view(['GET'])
def subrabble_list(request):
    if request.method == 'GET':
        subrabbles = SubRabbles.objects.all()
        serializer = SubRabblesSerializer(subrabbles, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def subrabble_by_id(request, rabble_name):
    if request.method == 'GET':
        subrabble = SubRabbles.objects.get(rabble_name=rabble_name)
        serializer = SubRabblesSerializer(subrabble, many=False)
        return Response(serializer.data)

@api_view(['GET', 'POST'])
def posts_by_subrabble(request, rabble_name):
    if request.method == 'GET':
        subrabble = SubRabbles.objects.get(rabble_name=rabble_name)
        posts = Posts.objects.filter(subrabble_id=subrabble.id)
        serializer = PostsSerializer(posts, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = PostsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PATCH', 'DELETE'])
def post_in_subrabble(request, rabble_name, pk):
    try:
        subrabble = SubRabbles.objects.get(rabble_name=rabble_name)
        post = Posts.objects.get(subrabble_id=subrabble.id, id=pk)
    except Posts.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PostsSerializer(post, many=False)
        return Response(serializer.data)
    elif request.method == 'PATCH':
        serializer = PostsSerializer(post, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
