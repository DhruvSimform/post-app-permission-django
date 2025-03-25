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
        self.defult_group = Group.objects.create(name='defult')
        self.ban_group = Group.objects.create(name='ban')
        self.mod_group = Group.objects.create(name='mod')

        self.add_post_permission = Permission.objects.get(codename='add_post')
        self.delete_post_permission = Permission.objects.get(codename='delete_post')
        self.update_post_permission = Permission.objects.get(codename='change_post')
        # self.user.user_permissions.add(permission)

        self.defult_group.permissions.add(self.add_post_permission)
        self.mod_group.permissions.add(self.add_post_permission , self.delete_post_permission)
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

    


    def test_create_post__Super_user_mod_defult_POST(self):
        login = self.client.login(username='user1' , password='password')

        data = {
            'title':'Test Post',
            'description':'Test description'
            }

        response = self.client.post(reverse('create-post') , data)
        self.assertEquals(Post.objects.get(title = 'Test Post' , description='Test description').title , 'Test Post')

        self.assertRedirects(response , reverse('home'))


    def test_create_post__ban_user_POST(self):
        login = self.client.login(username='user1' , password='password')
        user = User.objects.get(username = 'user1' )
        user.groups.clear()
        user.groups.add(self.ban_group)

        data = {
            'title':'Test Post',
            'description':'Test description'
            }

        response = self.client.post(reverse('create-post') , data)
        # print(response)
        # Assert that the response returns a 403 Forbidden
        self.assertEqual(response.status_code, 403)  # Ensure permission is denied

        # If the response redirects to login then , check if it's a 302
        # self.assertEqual(response.status_code, 302)


    def test_create_post_as_super_user_GET(self):
        #first login as super user
        login = self.client.login(username='root' , password='root')
        self.assertTrue(login)


        response = self.client.get(reverse('create-post'))
        self.assertEqual(response.status_code, 200)  # Page should load successfully
        self.assertTemplateUsed(response, 'main/create-form.html')  # Ensure correct template is used
        

class TestPostDelete(TestCase):

    def setUp(self):
        self.client = Client()
        self.defult_group = Group.objects.create(name='defult')
        self.ban_group = Group.objects.create(name='ban')
        self.mod_group = Group.objects.create(name='mod')

        self.add_post_permission = Permission.objects.get(codename='add_post')
        self.delete_post_permission = Permission.objects.get(codename='delete_post')
        self.update_post_permission = Permission.objects.get(codename='change_post')
        # self.user.user_permissions.add(permission)

        self.defult_group.permissions.add(self.add_post_permission)
        self.mod_group.permissions.add(self.add_post_permission , self.delete_post_permission)
        #to create normal user
        user1 = User.objects.create_user(username='user1' , password='password')
        user2 = User.objects.create_user(username='user2' , password='password')
        user3 = User.objects.create_user(username='user3' , password='password')

        #to create super user
        super_user = User.objects.create_superuser(username='root' , password='root')
        self.login = self.client.login(username='user1' , password='password')
        data = {
            'title':'Test Post',
            'description':'Test description'
            }

        user1.groups.clear()
        user1.groups.add(self.mod_group)
        self.client.post(reverse('create-post') , data)
        user2.groups.clear()
        user2.groups.add(self.defult_group)
        user3.groups.clear()
        user3.groups.add(self.ban_group)



    def test_delete_post_by_mod_root_user(self):
        post = Post.objects.filter(title = 'Test Post' ,description = 'Test description').first()
        post_id = post.id
        self.assertTrue(Post.objects.filter(id=post_id).exists())
        response = self.client.post( reverse('home') ,{'post-id':post_id})
        self.assertFalse(Post.objects.filter(id=post_id).exists())

    def test_delete_post_by_deful_ban_owner(self):
        self.client.logout()
        self.client.login(username='user2' , password='password')
        post = Post.objects.filter(title = 'Test Post' ,description = 'Test description').first()
        post_id = post.id
        self.assertTrue(Post.objects.filter(id=post_id).exists())
        response = self.client.post( reverse('home') ,{'post-id':post_id})
        self.assertTrue(Post.objects.filter(id=post_id).exists())   

    def test_delete_post_by_deful_ban_owner(self):
        self.client.logout()
        self.client.login(username='user3' , password='password')
        post = Post.objects.filter(title = 'Test Post' ,description = 'Test description').first()
        post_id = post.id
        self.assertTrue(Post.objects.filter(id=post_id).exists())
        response = self.client.post( reverse('home') ,{'post-id':post_id})
        self.assertTrue(Post.objects.filter(id=post_id).exists()) 




        
