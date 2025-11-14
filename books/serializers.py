from django.core.exceptions import ValidationError
from rest_framework import serializers


from books.models import Book


class BookSerializer(serializers.ModelSerializer):
    #we can overwrite fields
    class Meta:
        model = Book
        fields = ('id','title', 'author','subtitle','content','isbn','price')
    def validate(self, data):
        # print(data)
        title = data.get('title', None)
        author = data.get('author', None)
        #check title if it contains letters
        if not title.isalpha():
            raise ValidationError(
                {
                "status":False,'message':'Title must be str'})
        #check title and author
        if Book.objects.filter(title=title,author=author).exists():
            raise ValidationError({
                "status":False,
                'message':'title and author already exists in library'})

        # print(title)
        return data
    def validate_price(self, price):
        if price <= 0 or price > 99999999:
            raise ValidationError({
                "status":False,
                'message':'price is not valid'
            })


# class BookSerializerCustom(serializers.Serializer):
#     title = serializers.CharField()
#     author = serializers.CharField()
#     subtitle = serializers.CharField()
#     content = serializers.CharField()

class CashSerializer(serializers.Serializer):
    input=serializers.CharField(max_length=100)
    output=serializers.CharField(max_length=100)