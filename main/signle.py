from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.contrib.auth.models import Group 
from main.models import Post
from guardian.shortcuts import assign_perm

@receiver(post_save,sender = User)
def give_defulte_user_role(sender,instance ,**kwargs):
    user = instance
    defult_group = Group.objects.get(name='defult')
    user.groups.add(defult_group)

    
@receiver(post_save,sender=Post)
def allow_post_owner_edit_post(sender , instance ,**kwargs):
    post = instance
    user=post.author
    assign_perm('change_post', user, post)
