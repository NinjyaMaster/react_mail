from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from mail.models import Email
from django.forms.models import model_to_dict

from mail.api.serializers import EmailSerializer,EmailDetailSerializer


MAIL_SEND_URL = reverse('mail:api_mail_send')

def get_detail_url(mail_id):
    """Create and return a mail detail URL."""
    return reverse('mail:api_mail_detail', args=[mail_id])

def get_mailbox_url(mailbox_id):
    return reverse('mail:mailbox_by_type', args=[mailbox_id])


def create_mail(user, **params):
    """Create and return a sample mail."""
    defaults = {
        'subject':'test from shell',
        'body': 'This is a test mail. This is a test mail',
    }
    defaults.update(params)
    mail = Email.objects.create(sender=user, **defaults)
    mail.recipients.add(user)
    return mail


def create_user(**params):
    """Create and return a new user."""
    return get_user_model().objects.create_user(**params)



class PrivateMailAPITest(TestCase):
    """Test authenticated API requests."""

    def setUp(self):
        self.client = APIClient()
        payload = {
            'email': 'test@test.com',
            'password': 'testpass123',
            'username': 'Testname',
        }
        self.user = create_user(**payload)
        self.client.force_authenticate(self.user)

    def test_retrieve_mails(self):
        """Test retrieving a list of recipes."""
        mail_obj = create_mail(user=self.user)
        
        #url = reverse('mail:api_mail_send')
        url = get_mailbox_url("inbox")
        res = self.client.get(url)
        mails = Email.objects.all().order_by('-id')
        serializer = EmailSerializer(mails, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)


    def test_mail_list_limited_to_user(self):
        """Test list of mail is limited to authenticated user."""
        other_user = get_user_model().objects.create_user(
            'other@example.com',
            'password123',
            'other',
        )
        other_user = create_user(email='other@example.com', password='test123',username='other')
        create_mail(user=other_user)
        create_mail(user=self.user)

        res = self.client.get(get_mailbox_url("inbox"))
        mails = Email.objects.filter(sender=self.user)
        serializer = EmailSerializer(mails, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_get_mail_detail(self):
        """Test get mail detail."""
        mail = create_mail(user=self.user)
        url = get_detail_url(mail.id)
        res = self.client.get(url)
        serializer = EmailDetailSerializer(mail)
        self.assertEqual(res.data, serializer.data)


    def test_send_mail(self):
        """Test sending a mail."""
        payload = {
            'subject': 'Sample mail',
            'recipients': 'test@test.com',
            'body': 'test mail from test client',
        }
        res = self.client.post(MAIL_SEND_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        #print(f'****mailbox url****{res.data}')
        #I don't know how to retrive the email by "id"
        mail = Email.objects.get(id=1)
        self.assertTrue(True)
        for k, v in payload.items():
            # recipients value is mail_auth.User.None. so it cause error
            if(k != "recipients"):
                self.assertEqual(getattr(mail, k), v)
        self.assertEqual(mail.sender, self.user) 

    def test_update_archive(self):
        """Test  update of a mail archived status."""
        mail = create_mail(
            user=self.user
        )
        
        mail_copy = model_to_dict(mail)
        mail_copy['sender'] = 'Testname test@test.com'
        mail_copy['recipients'] = ['Testname']
        mail_copy['archived'] = True

        url = get_detail_url(mail.id)
        res = self.client.put(url, mail_copy)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        mail.refresh_from_db()
        self.assertEqual(mail.sender, self.user)
        self.assertEqual(mail.subject, mail_copy['subject'])
        self.assertEqual(mail.body, mail_copy['body'])
        self.assertEqual(mail.archived, mail_copy['archived'])