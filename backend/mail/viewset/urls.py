from rest_framework.routers import DefaultRouter
from django.urls import path,include

from mail.viewset.viewset_views import  TagViewSet, EmailViewSet

router = DefaultRouter()
router.register("tags", TagViewSet)
router.register("emails", EmailViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path(
        "mailbox/<str:mailbox_name>/",
        EmailViewSet.as_view({"get": "list"}),
        name="by-mailbox",
    ),
]


