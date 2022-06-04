from dataclasses import field
from rest_framework import serializers
from mail.models import Email,Tag
from mail_auth.models import User



class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ["id","creator","value"]
        #fields = "__all__"



class EditTagSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Tag
        fields = ["id","creator","value"]
        #fields = "__all__"


class EmailSerializer(serializers.ModelSerializer):
    sender = serializers.StringRelatedField(many=False) 
    #recipients = serializers.StringRelatedField(many=True) 
    recipients  = serializers.SlugRelatedField(
        slug_field="username", many=True, queryset=User.objects.all()
    )
    class Meta:
        model = Email
        fields = "__all__"
        readonly = ["timestamp"]



class EmailDetailSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True,read_only=True)
    sender = serializers.StringRelatedField(many=False) 
    recipients  = serializers.SlugRelatedField(
        slug_field="username", many=True, queryset=User.objects.all()
    )
    #recipients  =  serializers.StringRelatedField(many=False) 

    #fields = ["__all__","tags"] didn't work
    class Meta:
        model = Email
        fields = ["sender","recipients","subject","body","timestamp","read","archived","tags"]
        readonly = ["timestamp"]


#Did not really work for adding tag
class EditEmailEditTagSerializer(serializers.ModelSerializer):
    tags = EditTagSerializer(many=True,read_only=True)
    sender = serializers.StringRelatedField(many=False) 
    recipients  = serializers.StringRelatedField(many=True) 

    #fields = ["__all__","tags"] didn't work
    class Meta:
        model = Email
        fields = ["sender","recipients","subject","body","timestamp","read","archived","tags"]
        readonly = ["timestamp"]

    #Did not really work for adding tag
    def update(self, instance, validated_data):
        tags = validated_data.pop("tags")

        instance = super(EditEmailEditTagSerializer, self).update(instance, validated_data)

        for tag_data in tags:
            if tag_data.get("id"):
                # tag has an ID so was pre-existing
                continue
            tag = Tag(**tag_data)
            tag.creator = self.context["request"].user
            tag.content_object = instance
            tag.save()

        return instance


class CreateEmailSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True,read_only=True)

    sender = serializers.StringRelatedField(many=False)

    recipients = serializers.SlugRelatedField(
        slug_field="email", many=True, queryset=User.objects.all()
    )

    class Meta:
        model = Email
        fields = ["sender","recipients","subject","body","timestamp","read","archived","tags"]
        readonly = ["timestamp"]


