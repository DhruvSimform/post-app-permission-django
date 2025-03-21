from django.shortcuts import render , HttpResponse , redirect ,get_object_or_404 
from django.http import HttpResponseForbidden
from .form import RegistrationForm , PostForm
from django.contrib.auth import login , logout , authenticate 
from django.contrib.auth.decorators import login_required ,permission_required
from .models import Post 
from django.contrib.auth.models import User , Group , Permission 

# Create your views here.


@login_required()
def home(request):

    if request.method == "POST":

        post_id = request.POST.get('post-id')
        user_id = request.POST.get('user-id')
        print(user_id)
        

        if post_id:
            post= get_object_or_404(Post,id=post_id)
            if (request.user == post.author) or request.user.has_perm("main.delete_post"):
                post.delete()
            else:
                return HttpResponseForbidden("You can  Only delete your post . <br> don't try to bee over smart by deleting other post")
            
        if user_id and request.user.is_staff :
            user = User.objects.filter(id=user_id).first()

            try:
                # defult_group = Group.objects.get(name='defult')
                user.groups.clear()
            except:
                pass

            try:
                ban_group = Group.objects.get(name='ban')
                user.groups.add(ban_group)
            except:
                pass
    

    posts = Post.objects.all()
    context = {
        'posts':posts
    }
    return render(request , 'main/home.html',context)


@login_required()
@permission_required('main.add_post' , raise_exception=True)
def create_post(request):

    if request.method == "POST":
        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()

            return redirect('home')
    else: 
        form = PostForm()

    context = {
        'form':form
    }
    return render(request , 'main/create-form.html',context )




def sign_up(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request , user)
            return redirect('home')
        
    else:
        form=RegistrationForm()

    context = {
        'form':form
    }
    return render(request , 'registration/sign_up.html',context)


@login_required()
def all_user(request):

    if request.method=="POST":
        user_id = request.POST.get("user-id")
        group_name= request.POST.get('group')

        try:
            user = User.objects.filter(id=user_id).first()
            user.groups.clear()
            group = Group.objects.get(name=group_name)
            user.groups.add(group)

            return redirect('users')
        except:
                pass

    if request.user.is_staff:
        users = User.objects.all()
        context={
            'users':users
        }
        return render(request,'main/users.html',context)
    
    else:
        return HttpResponseForbidden("You are not super user")