from django.shortcuts import render, get_object_or_404, redirect
from . models import Post, Comment
from django.utils import timezone

# Create your views here.
def index(request):
    posts = Post.objects.all
    return render(request, 'index.html', {'posts' : posts})

def detail(request, post_id):
    postdetail = get_object_or_404(Post, pk = post_id)
    return render(request, 'detail.html', {'posts' : postdetail})   

#글쓰기 페이지 보여주는 함수
def write(request):
    return render(request, 'write.html')

# 쓴 글을 데이터베이스에 넣어주는 함수
def create(request):
    post = Post() #Post라는 class로 부터 post라는 객체를 생성
    post.title = request.GET['title']
    post.body = request.GET['fulltext']
    post.pub_date = timezone.datetime.now()
    post.save()
    return redirect('/detail/' + str(post.id))     # 20번째 줄에서의 post를 가져와서 post.id 해준것

# # def commentCreate(request,post_pk):
#     post = get_object_or_404(Post, pk=post_pk)
#     content = request.POST.get('content')
#     CommentNLike.objects.create(post = post, comment = content)
#     return redirect('postView') #

#댓글쓰기
def commentCreate(request, post_pk):
    postdetail = get_object_or_404(Post, pk = post_pk)  #부모의 모델이랑 부모 id 값 을 가져온다. 부모의 pk값을 comment에 저장 각 본문에 댓글을 달아줘야하기 때문
    commentbody = request.POST.get('content')     # commentbody는 아무 변수나 가능, 37번줄의 우변이랑 같아야함/ 저장해주는것일뿐 create에서 쓴 post.title = request.GET이랑은 다름
    Comment.objects.create(post=postdetail, commentbody=commentbody)
    return redirect('/detail/' + str(postdetail.id))    #본문 url 로
    #좌변의 테이블(models.py에서 만들어준 테이블이름) 을 만들어주기도 하고 우변것을 저장
    # comment = Comment()
    # comment.commentdate = timezone.datetime.now()
    # comment.save()
    # return redirect('/commentCreate/' + str(post.pk))  #원래 글 페이지로 
