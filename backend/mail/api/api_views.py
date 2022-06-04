from rest_framework import generics

from mail.api.serializers import EmailSerializer, TagSerializer,EmailDetailSerializer,EditEmailEditTagSerializer,CreateEmailSerializer
from mail.models import Email,Tag
from mail_auth.models import User

from rest_framework.permissions import IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly
from mail.api.permissions import AuthorModifyOrReadOnly,IsAdminUserForObject ,IsSenderOrRecipients

from django.db.models import Q
from django.http import Http404

class MailList(generics.ListCreateAPIView):
    #permission_classes = [IsAuthenticatedOrReadOnly]
    permission_classes = [IsAuthenticated]
    queryset = Email.objects.all()
    serializer_class = EmailSerializer

    def get_queryset(self):

        #fetch the  mailbox name URL parameter from self.kwargs
        mailbox_name = self.kwargs.get("mailbox_name")

        if mailbox_name == "inbox":
            return self.queryset.filter(Q(recipients=self.request.user) & Q(archived=False))
        elif mailbox_name == "sent":
            return self.queryset.filter(Q(sender=self.request.user)  & Q(archived=False))
        elif mailbox_name == "archived":
            return self.queryset.filter(Q(archived=True) & ( Q(recipients=self.request.user) | Q(sender=self.request.user)) )
        else:
            raise Http404(
                f"Mailbox {mailbox_name} is not valid, should be "
                f"'inbox', 'sent' or 'archived'"
            )

        #return self.queryset.filter(
            #Q(recipients=self.request.user) | Q(sender=self.request.user)
            #Q(recipients=self.request.user)
            #Q(sender=self.request.user)
        #)


class MailDetail(generics.RetrieveUpdateDestroyAPIView):
    #permission_classes = [IsAuthenticated & AuthorModifyOrReadOnly]
    permission_classes = [IsAuthenticated & IsSenderOrRecipients]
    #permission_classes = [IsAuthenticated]
    queryset = Email.objects.all()
    serializer_class = EmailDetailSerializer
    #serializer_class = EmailSerializer


class MailSend(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Email.objects.all()
    serializer_class = CreateEmailSerializer

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)




class TagList(generics.ListCreateAPIView):
    permission_classes = [AuthorModifyOrReadOnly | IsAdminUserForObject]
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


#class EditMailTag(generics.CreateAPIView):
class EditMailTag(generics.RetrieveUpdateDestroyAPIView):
    queryset = Email.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = EditEmailEditTagSerializer