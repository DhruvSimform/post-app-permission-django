# from django.test import SimpleTestCase
# from django.urls import reverse , resolve
# from main.views import home , create_post ,sign_up , all_user , update_post , share_edit_permition
# from django.contrib.auth.views import LoginView

# class TestUrls(SimpleTestCase):

#     def test_home_url_is_resolved(self):
#         url = reverse('home')
#         # print(resolve(url))

#         # Test case to check for correct view function executing with url name
#         self.assertEquals(resolve(url).func  , home)


#     def test_create_post_url_is_resolved_1(self):
#         url = reverse('create-post')
#         print(resolve(url))

#         # Test case to check for correct view function executing with url name
#         self.assertEquals(resolve(url).func  , create_post)

#     #for class based views we have to use func.view_class

#     def test_create_post_url_is_resolved_1(self):
#         url = reverse('sign-up')
#         # print(resolve(url))

#         # Test case to check for correct view function executing with url name
#         self.assertEquals(resolve(url).func  , sign_up)
    
#     def test_users_url_is_resolved(self):
#         url = reverse('users')
#         # print(resolve(url))

#         # Test case to check for correct view function executing with url name
#         self.assertEquals(resolve(url).func  , all_user)

        
    
#     def test_update_post_url_is_resolved(self):
#         url = reverse('update-post' , kwargs={'post_id':5})
#         # print(resolve(url))

#         # Test case to check for correct view function executing with url name
#         self.assertEquals(resolve(url).func  , update_post)

#     def test_share_post_url_is_resolved(self):
#         url = reverse('share' )
#         # print(resolve(url))

#         # Test case to check for correct view function executing with url name
#         self.assertEquals(resolve(url).func  , share_edit_permition)

#     def test_login_post_url_is_resolved(self):
#         url = reverse('login' )
#         # print(resolve(url))

#         # Test case to check for correct view function executing with url name
#         self.assertEquals(resolve(url).func.view_class  , LoginView)