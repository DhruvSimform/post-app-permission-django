# class TestPostDelete(TestCase):
#     #  by this we can disconnect signle and connect them for test
#     # @classmethod
#     # def setUpClass(cls):
#     #     super().setUpClass()
#     #     post_save.disconnect(receiver=allow_post_owner_edit_post, sender=Post)  # Disable signal

#     # @classmethod
#     # def tearDownClass(cls):
#     #     post_save.connect(receiver=allow_post_owner_edit_post, sender=Post)  # Re-enable signal
#     #     super().tearDownClass()   

#     def setUp(self):
#         self.client = Client()

#         # Create groups
#         self.default_group = Group.objects.create(name='default')
#         self.ban_group = Group.objects.create(name='ban')
#         self.mod_group = Group.objects.create(name='mod')

#         # Create permissions
#         self.delete_post_permission = Permission.objects.get(codename='delete_post')

#         # Create users
#         self.owner_user = User.objects.create_user(username='owner', password='password')
#         self.other_user = User.objects.create_user(username='other', password='password')
#         self.moderator_user = User.objects.create_user(username='moderator', password='password')
#         self.admin_user = User.objects.create_superuser(username='admin', password='admin')

#         # Assign delete permission to moderator
#         self.mod_group.permissions.add(self.delete_post_permission)
#         self.moderator_user.groups.add(self.mod_group)

        
#         # Create a post by owner
#         login = self.client.login(username='other' , password='password')
#         self.post = Post.objects.create(title='Test Post', description='Test description', author=self.owner_user)

#     def test_moderator_can_delete_any_post(self):
#         """Moderator with delete permissions should be able to delete any post."""
#         self.client.login(username='moderator', password='password')

#         response = self.client.post(reverse('home'), {'post-id': self.post.id})
#         self.assertEqual(response.status_code, 302)  # Redirects after delete

#         self.assertFalse(Post.objects.filter(id=self.post.id).exists()) 

#     # def test_delete_post_by_post_owner(self):
#     #     post = Post.objects.filter(title = 'Test Post' ,description = 'Test description').first()
#     #     popt = Post.objects.all().first()
#     #     print(post.author)
#     #     print(post.id)
#     #     post_id = post.id

#     #     self.assertTrue(Post.objects.filter(id=post_id).exists())
#     #     response = self.client.post( reverse('home') , kwargs ={'post_id':post_id})
#     #     print(response)
#     #     self.assertFalse(Post.objects.filter(id=post_id).exists())