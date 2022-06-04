from mail.api.serializers import TagSerializer,EmailSerializer,EmailDetailSerializer
from rest_framework import generics, viewsets
from mail.models import Email, Tag
from mail.api.permissions import AuthorModifyOrReadOnly,IsAdminUserForObject


from rest_framework.decorators import action
from rest_framework.response import Response

from django.db.models import Q
from django.http import Http404


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    # does not work yet it suppose to be accessible at /viewset/tags/1/mails/
    @action(methods=["get"], detail=True, name="Mails with the Tag")
    def mails(self, request, pk=None):
        tag = self.get_object()
        print(f"******** request user: {request.user}")
        mail_serializer = EmailSerializer(
            tag.mails, many=True, context={"request": request}
        )
        return Response(mail_serializer.data)


class EmailViewSet(viewsets.ModelViewSet):
    permission_classes = [AuthorModifyOrReadOnly | IsAdminUserForObject]
    queryset = Email.objects.all()

    def get_serializer_class(self):
        if self.action in ("list", "create"):
            print("create")
            return EmailDetailSerializer
        print("somethingelse")
        return EmailDetailSerializer


    # Filter Example
    def get_queryset(self):     
        queryset= self.queryset.filter(Q(recipients=self.request.user) | Q(sender=self.request.user))

        mailbox_name = self.kwargs.get("mailbox_name")

        if not mailbox_name:
            return queryset
        
        if mailbox_name == "inbox":
            return queryset.filter(Q(recipients=self.request.user) & Q(archived=False))
        elif mailbox_name == "sent":
            return queryset.filter(Q(sender=self.request.user)& Q(archived=False))
        elif mailbox_name == "archived":
            return queryset.filter(Q(archived = True))
        else:
            raise Http404(
                f"Mailbox {mailbox_name} is not valid, should be "
                f"'inbox', 'sent' or 'archived'"
            )



    #    return self.queryset.filter(
    #        #Q(recipients=self.request.user) | Q(sender=self.request.user)
    #        #Q(recipients=self.request.user)
    #        Q(sender=self.request.user)
    #    )
    