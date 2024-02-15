from rest_framework.test import APITestCase
from rest_framework import status
from accounts.models import User

# Create your tests here.

class AccountsAPITest(APITestCase):
    def setUp(self):
        user = User.objects.create_user(first_name='shehbaaz',last_name='shaikh',password='Shaikh123',\
                                        email='shehbaaz@gmail.com',mobile_no=9323797979,pincode=400043)

    def test_register_user_pass(self):
        url = '/api/accounts/register/'
        data = {
            'first_name':'Shehbaaz',
            'last_name':'Shaikh',
            'email':'shehbaazwebdev@gmail.com',
            'password':'Shaikh123456',
            'password2':'Shaikh123456',
            'mobile_no':9323791010,
            'pincode':400004
        }
        
        response = self.client.post(url,data=data)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)

    def test_register_user_fail_password(self):
        url = '/api/accounts/register/'
        data = [{
                'first_name':'Shehbaaz',
                'last_name':'Shaikh',
                'email':'shehbaazwebdev@gmail.com',
                'password':'shaikh123',
                'password2':'shaikh12',
                'mobile_no':9323791010,
                'pincode':400004
            },
            {
                'first_name':'Shehbaaz',
                'last_name':'Shaikh',
                'email':'shehbaazwebdev@gmail.com',
                'password':'SHAIKH12',
                'password2':'SHAIKH12',
                'mobile_no':9323791010,
                'pincode':400004
            },
            {
                'first_name':'Shehbaaz',
                'last_name':'Shaikh',
                'email':'shehbaazwebdev@gmail.com',
                'password':'Shaikh',
                'password2':'Shaikh',
                'mobile_no':9323791010,
                'pincode':400004
            },
            {
                'first_name':'Shehbaaz',
                'last_name':'Shaikh',
                'email':'shehbaazwebdev@gmail.com',
                'password':'Shaikh12',
                'password2':'Shaikh12',
                'mobile_no':93237910,
                'pincode':400004
            },
            {
                'first_name':'Shehbaaz',
                'last_name':'Shaikh',
                'email':'shehbaazwebdev@gmail.com',
                'password':'Shaikh12',
                'password2':'Shaikh12',
                'mobile_no':9323791010,
                'pincode':40004
            }
        ]
        
        for payload in data:
            response = self.client.post(url,data=payload)
            self.assertEquals(response.status_code,status.HTTP_400_BAD_REQUEST)

    def test_user_login(self):

        url='/api/accounts/login/'
        data={
            'email':'shehbaaz@gmail.com',
            'password':'Shaikh123'
        }

        response = self.client.post(url,data=data)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertIn('access',response.json())
        self.assertIn('refresh',response.json())

