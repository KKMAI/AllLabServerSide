from django.http import HttpResponse, JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from snippets.models import Snippet, SnippetCategory
from snippets.serializers import *
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from rest_framework.views import APIView, status

from django.contrib.auth.models import User

from snippets.permissions import SnippetPermission

from django.shortcuts import get_object_or_404

class MyTokenAuthentication(TokenAuthentication):
    keyword = "Bearer" #default in postman

class UserList(APIView):
    authentication_classes = [MyTokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        print("USER:", request.user)
        print("AUTH:", request.auth)
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


class UserDetail(APIView):
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

class SnippetList(APIView):
    authentication_classes = [MyTokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly, SnippetPermission] #permission class ที่ REST FRMEWORK มีให้

    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

...

# use same path but different method
class SnippetDetail(APIView):
    authentication_classes = [MyTokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly, SnippetPermission]

    def get_object(self, pk):
        try:
            return Snippet.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            raise Http404
    """
    Retrieve, update or delete a code snippet.
    """
    def get(self, request):
        snippet = Snippet.objects.all()
        serializer = SnippetSerializer(snippet)
        return JsonResponse(serializer.data)

    def post(self, request, pk):
        snippet = get_object_or_404(Snippet, pk=pk)
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data) # defalut status is 200
        return JsonResponse(serializer.errors, status=400) # errors should send set status  if not It will send staus success(200) althought It error

    def delete(self, request, pk):
        snippet = get_object_or_404(Snippet, pk=pk)
        snippet = Snippet.objects.get(pk=pk)
        snippet.delete()
        return HttpResponse(status=204)
    

def category_list(request):
    """
    List all snippet categories.
    """
    if request.method == 'GET':
        categories = SnippetCategory.objects.all()
        serializer = SnippetCategorySerializer(categories, many=True)
        return JsonResponse(serializer.data, safe=False)