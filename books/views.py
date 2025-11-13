from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Book
from .serializers import BookSerializer
from rest_framework import generics, status


# class BookListApi(generics.ListCreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
class BookListApiView(APIView):

    def get(self, request):
        books = Book.objects.all()
        serializer_data = BookSerializer(books, many=True).data
        data={"status":f"Returned  {len(books)} books",
              "books": serializer_data}
        return Response(data)

#function based view
@api_view(['GET'])
def book_list_view(request,*args, **kwargs):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)
# Create your views here.

# class BookCreateApi(generics.CreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
class BookCreateApiView(APIView):

    def post(self, request):
        data = request.data
        serializer = BookSerializer(data=data)
        if serializer.is_valid():
            books=serializer.save()
            data={'status':f"Book created and saved books",
                  'books':data}
            return Response(data)
        else:
            return Response({
                "status": False,
                "message": "serializer is not valid"
            }, status=status.HTTP_400_BAD_REQUEST )





# class BookDetailApi(generics.RetrieveAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
class BookDetailApiView(APIView):

    def get(self, request,pk):
        try:
            book = Book.objects.get(id=pk)
            serializer_data = BookSerializer(book).data

            data={'status':f"Successfull",
                      'books':serializer_data}
            return Response(data,status=status.HTTP_200_OK)
        except Book.DoesNotExist:
            return Response(
                {'status':'False',
                             'message':'Book not found'},status=status.HTTP_404_NOT_FOUND)

# class BookDeleteApi(generics.DestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
class BookDeleteApiView(APIView):

    def delete(self,request,pk):
        try:
            book = Book.objects.get(id=pk)
            # book=get_object_or_404(Book,id=pk)
            book.delete()
            return Response({'status':True,
                             'message':'Successfully deleted'},status=status.HTTP_200_OK)
        except Book.DoesNotExist:
            return Response({
                "status":False,
                "message":"Book not found"
            },status=status.HTTP_400_BAD_REQUEST)

# class BookUpdateApi(generics.UpdateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookUpdateApiView(APIView):

    def put(self, request,pk):
        try:
            book = get_object_or_404(Book.objects.all(), pk=pk)
            data = request.data
            serializer = BookSerializer(instance=book, data=data, partial=True)
            if serializer.is_valid():
                book_save=serializer.save()
                return Response({'status':True,
                                 'message':f'Successfully {book_save}  updated'},status=status.HTTP_200_OK)
        except Book.DoesNotExist:
            return Response({'status':False,
                             'message':'Book not found'},status=status.HTTP_404_NOT_FOUND)



class BookCreateListApi(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
