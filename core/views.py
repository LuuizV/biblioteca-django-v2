from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.models import Livro
from core.serializers import LivroSerializer

class LivroListCreate(APIView):
    def get(self, request):
        livros = Livro.objects.all()
        serializer = LivroSerializer(livros, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = LivroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LivroDetail(APIView):
    def get(self, request, pk):
        try:
            livro = Livro.objects.get(pk=pk)
        except Livro.DoesNotExist:
            return Response({'error': 'Livro não encontrado'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = LivroSerializer(livro)
        return Response(serializer.data)
    
    def put(self, request, pk):
        try:
            livro = Livro.objects.get(pk=pk)
        except Livro.DoesNotExist:
            return Response({'error': 'Livro não encontrado'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = LivroSerializer(livro, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            livro = Livro.objects.get(pk=pk)
        except Livro.DoesNotExist:
            return Response({'error': 'Livro não encontrado'}, status=status.HTTP_404_NOT_FOUND)
        
        livro.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)