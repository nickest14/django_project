from django.utils.timesince import timesince
from rest_framework import serializers


from accounts.api.serializers import UserDisplaySerializer
from tweets.models import Tweet # from ..models import Tweet


class ParentTweetModelSerializer(serializers.ModelSerializer):
    user = UserDisplaySerializer(read_only=True) #write_only
    date_display = serializers.SerializerMethodField()
    timesince = serializers.SerializerMethodField()
    likes = serializers.SerializerMethodField()
    did_like = serializers.SerializerMethodField()

    class Meta:
        model = Tweet
        fields = [
            'id',
            'user',
            'content',
            'timestamp',
            'date_display',
            'timesince',
            'likes',
            'did_like',
        ]

    def get_did_like(self, obj):
        try:
            user = request.user
            if user.is_authenticated():
                if user in obj.liked.all():
                    return True
        except:
            pass
        return False


    def get_likes(self, obj):
        return obj.liked.all().count()

    def get_date_display(self, obj):
        return obj.timestamp.strftime("%b %d, %Y at %I:%M %p")

    def get_timesince(self, obj):
        return timesince(obj.timestamp) + " ago"


class TweetModelSerializer(serializers.ModelSerializer):
    parent_id       = serializers.CharField(write_only=True, required=False)
    user            = UserDisplaySerializer(read_only=True) #write_only
    date_display    = serializers.SerializerMethodField()
    timesince       = serializers.SerializerMethodField()
    parent          = ParentTweetModelSerializer(read_only=True)
    likes           = serializers.SerializerMethodField()
    did_like        = serializers.SerializerMethodField()
    children_count  = serializers.SerializerMethodField()
    showimage           = serializers.SerializerMethodField()
    # image = serializers.Base64ImageField（max_length = None，use_url = True）


    class Meta:
        model = Tweet
        fields = [
            'parent_id',
            'id',
            'user',
            'content',
            'image',
            'showimage',
            'timestamp',
            'date_display',
            'timesince',
            'parent',
            'likes',
            'did_like',
            'reply',
            'children_count'
        ]
        #read_only_fields = ['reply']

    def get_showimage(self, obj):
        try:
            showimage = obj.image.url
        except:
            showimage = None
        return showimage

    def get_did_like(self, obj):
        request = self.context.get("request")
        try:
            user = request.user
            if user.is_authenticated():
                if user in obj.liked.all():
                    return True
        except:
            pass
        return False

    def get_children_count(self, obj):
        return obj.get_children_size()
        # return 0
    def get_likes(self, obj):
        return obj.liked.all().count()

    def get_date_display(self, obj):
        return obj.timestamp.strftime("%b %d, %Y at %I:%M %p")

    def get_timesince(self, objj):
        return timesince(objj.timestamp) + " ago"
