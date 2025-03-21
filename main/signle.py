from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.contrib.auth.models import Group 


@receiver(post_save,sender = User)
def give_defulte_user_role(sender,instance ,**kwargs):
    user = instance
    defult_group = Group.objects.get(name='defult')
    user.groups.add(defult_group)

    

