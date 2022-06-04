from django.urls import path



from mail.api.api_views import MailList, MailDetail, MailSend,TagList,EditMailTag


app_name = 'mail'

urlpatterns = [
    #path("mails/", MailList.as_view(), name="api_mail_list"),
    path("mails/<str:mailbox_name>/", MailList.as_view(), name="mailbox_by_type" ),
    path("mail/<int:pk>/", MailDetail.as_view(), name="api_mail_detail"),
    path("send/", MailSend.as_view(), name="api_mail_send"),
    path("tags/",TagList.as_view(),name="api_tag_list"),
    path("edit_mail_tag/",EditMailTag.as_view(),name="api_edit_mail_tag")
]

