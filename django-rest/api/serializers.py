from rest_framework import serializers
from django.contrib.auth import get_user_model
from home.models import Article


# validation plus nested serializer 

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = "__all__"


class ArticleSerializer(serializers.ModelSerializer):
    author = AuthorSerializer() 

    class Meta:
        model = Article
        fields = "__all__"


    def validate_title(self, value):
        list_filter = ["nima", "ob"]

        for i in list_filter:
            if i in value:
                raise serializers.ValidationError("you can not say ob or nima in title")

        return value


# hyper link

class ArticleSerializer2(serializers.ModelSerializer):

    author = serializers.HyperlinkedIdentityField(view_name="api:userdetail")

    class Meta:
        model = Article
        fields = "__all__"




# just send the author username

class ArticleSerializer3(serializers.ModelSerializer):

    author = serializers.CharField(source="author.username", read_only=True)

    class Meta:
        model = Article
        fields = "__all__"


# just send the author username

class ArticleSerializer4(serializers.ModelSerializer):

    def get_author(self, obj):
        return obj.author.username

    author = serializers.SerializerMethodField("get_author")

    class Meta:
        model = Article
        fields = "__all__"