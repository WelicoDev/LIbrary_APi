from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Book

class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('title' , 'subtitle','content', 'author' ,'isbn','price')

    def validate(self ,data):
        title = data.get('title',None)
        author = data.get('author',None)

        #check title if it containes only alhabetical chars
        if not title.isalpha():
            raise ValidationError(
                {
                    'status':False,
                    'message':'Kitobni sarlavhasi harflardan tashkil topgan bo\'lishi kerak'
                }
            )

        # check title and author from database existence
        if Book.objects.filter(title=title , author=author).exists():
            raise ValidationError(
                {
                    'status': False,
                    'message': 'Kitobni sarlavhasi va muallifi bir xil bo\lgan kitobni yuklay olmaysiz  !'
                }
            )
        return data

    def validate_price(self ,price):
        if price < 0 or price > 9999999999:
            raise ValidationError(
                {
                    'status': False,
                    'message': 'Narx noto\'g\'ri kiritilgan  !'
                }
            )


# class BookSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=200)
#     subtitle = serializers.CharField(max_length=250)
#     content = serializers.CharField()