from rest_framework.test import APITestCase
from rest_framework import status
from accounts.models import User,USER_ROLES
from rest_framework_simplejwt.tokens import AccessToken
from contents.models import Content,ContentCategory
# Create your tests here.

class ContentListCreateAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(first_name='shehbaaz',last_name='shaikh',password='Shaikh123',\
                                        email='shehbaaz@gmail.com',mobile_no=9323797979,pincode=400043)
        token = AccessToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        self.content_category = ContentCategory.objects.create(name='Adventure')
        file = open('apps/contents/test_document.pdf','rb')
        data = [{'title':f"title{i}",'body':f'body{i}','summary':f'summary{i}','author':self.user,'category':self.content_category.id,'documents':file} 
                for i in range(1,4)]
        for payload in data:
            response = self.client.post('/api/contents/',payload,format='multipart')


    def test_list_content(self):
        url = '/api/contents/'
        contents_count = Content.objects.all().count()
        response = self.client.get(url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(len(response.json()),contents_count)
        
    def test_create_content(self):
        url = '/api/contents/'
        file = open('apps/contents/test_document.pdf','rb')
        data = {
            'title':"title 10",'body':'body 10','summary':'summary 10','author': self.user,\
                'documents':file,'category':self.content_category.id
            } 
        response = self.client.post(url,data)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)

class ContentUpdateRetrieveDeleteAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(first_name='shehbaaz',last_name='shaikh',password='Shaikh123',\
                                        email='shehbaaz@gmail.com',mobile_no=9323797979,pincode=400043)
        token = AccessToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        self.content_category = ContentCategory.objects.create(name='Adventure')
        file = open('apps/contents/test_document.pdf','rb')
        data = [{'title':f"title{i}",'body':f'body{i}','summary':f'summary{i}','author':self.user,'category':self.content_category.id,'documents':file} 
                for i in range(1,6)]
        for payload in data:
            response = self.client.post('/api/contents/',payload,format='multipart')


    def test_retrieve_content(self):
        pk = Content.objects.all().first()
        url = '/api/contents/'
        response = self.client.get(f'{url}{pk.id}/')
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(response.data[0]['id'],pk.id)

    def test_edit_content(self):
        pk = Content.objects.all().first()
        url = '/api/contents/'
        data = {
            'title': 'title  (edited)',
            'body': 'body  (edited)'
        }
        response = self.client.patch(f'{url}{pk.id}/',data)
        self.assertEqual(response.status_code,status.HTTP_202_ACCEPTED)
        self.assertEqual(response.data['title'],data['title'])
        
    def test_delete_content(self):
        pk=Content.objects.all().first()
        url='/api/contents/'
        response = self.client.delete(f'{url}{pk.id}/')
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)

class ContentAdminUpdateRetrievDeleteAPITest(APITestCase):
    def setUp(self):
        self.content_category = ContentCategory.objects.create(name='Adventure')
        file = open('apps/contents/test_document.pdf','rb')
        author = User.objects.create_user(first_name='shehbaaz',last_name='shaikh',password='Shaikh123',\
                                        email='shehbaaz@gmail.com',mobile_no=9323797979,pincode=400043)
        author_token = AccessToken.for_user(author)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {author_token}')
        data = [{'title':f"title{i}",'body':f'body{i}','summary':f'summary{i}','author':author,'category':self.content_category.id,'documents':file} 
                for i in range(1,6)]
        for payload in data:
            response = self.client.post('/api/contents/',payload,format='multipart')
        self.user = User.objects.create_user(first_name='shehbaaz',last_name='shaikh',password='Shaikh123',\
                                        email='shehbaazadmin@gmail.com',mobile_no=9323797970,pincode=400043,user_role=USER_ROLES.ADMIN)
        token = AccessToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')


    def test_retrieve_content(self):
        pk = Content.objects.all().first()
        url = '/api/contents/'
        response = self.client.get(f'{url}{pk.id}/')
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(response.data[0]['id'],pk.id)

    def test_edit_content(self):
        pk = Content.objects.all().first()
        url = '/api/contents/'
        data = {
            'title': 'title  (edited)',
            'body': 'body  (edited)'
        }
        response = self.client.patch(f'{url}{pk.id}/',data)
        self.assertEqual(response.status_code,status.HTTP_202_ACCEPTED)
        self.assertEqual(response.data['title'],data['title'])
        
    def test_delete_content(self):
        pk=Content.objects.all().first()
        url='/api/contents/'
        response = self.client.delete(f'{url}{pk.id}/')
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)