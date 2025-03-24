from django.contrib.auth.models import User, Group ,Permission
from django.test import TestCase, Client
from django.urls import reverse
from main.models import Post



class TestLogin(TestCase):

    def setUp(self):
        self.client = Client()
        Group.objects.create(name='defult')
        Group.objects.create(name='ban')
        Group.objects.create(name='mod')

        user = User.objects.create_user(username = 'User' , password = 'password@123')

    def test_login_user(self):
        login = self.client.login(username = 'User' , password = 'password@123')
        self.assertTrue(login)

    def test_logout_user(self):
        logout = self.client.logout()
        



class TestViewsForSuper(TestCase):

    def setUp(self):
        self.client = Client()
        Group.objects.create(name='defult')
        Group.objects.create(name='ban')
        Group.objects.create(name='mod')

        permission = Permission.objects.get(codename='add_post')
        self.user.user_permissions.add(permission)

        #to create normal user
        user1 = User.objects.create_user(username='user1' , password='password')
        user2 = User.objects.create_user(username='user2' , password='password')
        user3 = User.objects.create_user(username='user3' , password='password')

        #to create super user
        super_user = User.objects.create_superuser(username='root' , password='root')

    def test_get_all_post_list_GET (self):
        login = self.client.login(username='user1' , password='password')
        self.assertTrue(login)

        response = self.client.get(reverse('home'))

        self.assertEqual(response.status_code , 200)
        self.assertTemplateUsed(response , template_name='main/home.html')
    
    # def test_create_post_POST (self):
    #     login = self.client.login(username='user1' , password='password')
    #     self.assertTrue(login)

    #     data = {
    #         'title':'Test Post',
    #         'description':'Test description'
    #     }
    #     response = self.client.post(reverse('create-post'),data)
    #     self.assertRedirects(response, reverse('home'))

    #     # print(response.status_code) 



    # def create_post_as_super_user_GET(self):
    #     #first login as super user
    #     login = self.client.login(username='root' , password='root')
    #     self.assertTrue(login)


    #     response = self.client.get(reverse('create-post'))
    #     self.assertEqual(response.status_code, 200)  # Page should load successfully
    #     self.assertTemplateUsed(response, 'main/create-form.html')  # Ensure correct template is used







        
