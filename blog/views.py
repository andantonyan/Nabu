# -*- coding: utf-8 -*-
from django.shortcuts import render
from utils.functions import check_user
from .models import Article, Comment
from account.models import User
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.core.exceptions import ObjectDoesNotExist


from django.views.decorators.csrf import csrf_exempt
comments_limit = 5
articles_limit = 10

def index(request):

	user_id = check_user(request)
	article_error = False
	article_success = False
	comment_error = False
	articles = Article.objects.all()[:10]

	if request.method == 'POST':

		if 'add_article' in request.POST:

			article_post = request.POST['add_article']
			if len(article_post)>0:
				Article.objects.create(
					author = User.objects.get(id=user_id),
					body = article_post
				)
				# article_success = u'Թեման հաջողությամբ ավելացված է'
				return HttpResponseRedirect('/blog')
			else:
				article_error = u'Լրացրեք դաշտը'
				return render(request, 'blog/index.html', 
					{
						'article_error':article_error, 
						'article_success':article_success,
						'articles':articles,
						'comment_error':comment_error
					})


		elif 'add_comment' in request.POST:
			add_comment = request.POST['add_comment']
			article_id = request.POST['article_id']
			try:
				article = Article.objects.get(id=article_id)
			except Exception, e:
				return HttpResponseRedirect('/blog')

			if len(add_comment)>0:
				Comment.objects.create(
					author = User.objects.get(id=user_id),
					article = article,
					body = add_comment
				)
				# comment_success = u'Թեման հաջողությամբ ավելացված է'
				return HttpResponseRedirect('/blog')

			else:
				# comment_error = u'Լրացրեք դաշտը'	
				return render(request, 'blog/index.html', 
					{
						'article_error':article_error, 
						'article_success':article_success,
						'articles':articles,
						'comment_error':comment_error
					})


	else:

		return render(request, 'blog/index.html', 
			{
				'article_error':article_error, 
				'article_success':article_success,
				'articles':articles,
				'comment_error':comment_error
			})

@csrf_exempt
def article_update(request):
	if request.is_ajax():

		if 'articles_count' in request.POST:
			articles_count = request.POST['articles_count']
			articles_count = int(articles_count)
			start = articles_count
			end = articles_count + articles_limit
			articles = Article.objects.all()[start : end]
			return (render(request, 'blog/aticle_update.html', {'articles':articles}))

		else:
			return HttpResponse()

	else:
		raise Http404


@csrf_exempt
def comment_update(request):
	if request.is_ajax():

		if 'comments_count' in request.POST:

			comments_count = request.POST['comments_count']

			article = request.POST['article']
			comments_count = int(comments_count)
			start = comments_count
			end = comments_count + comments_limit
			comments = Comment.objects.filter(article=article)[start : end]
			# return HttpResponse(comments)
			return (render(request, 'blog/comment_update.html', {'comments':comments}))

		else:
			return HttpResponse()

	else:
		raise Http404


@csrf_exempt
def article_remove(request):
	user_id = check_user(request)
	# user_id = decrypt(user_id)
	if request.is_ajax():

		if 'article' in request.POST:

			article_id = request.POST['article']
			article_id = int(article_id)

			try:
				article = Article.objects.get(id = article_id)
			except ObjectDoesNotExist:
				return HttpResponse('false')
			
			if article.author.id == user_id:
				article.delete()
				return HttpResponse('true')
			else:
				return HttpResponse('false')

		else:
			return HttpResponse('false')

	else:
		raise Http404



@csrf_exempt
def comment_remove(request):
	user_id = check_user(request)
	if request.is_ajax():

		if 'comment' in request.POST:

			comment_id = request.POST['comment']
			comment_id = int(comment_id)

			try:
				comment = Comment.objects.get(id = comment_id)
			except ObjectDoesNotExist:
				return HttpResponse('false')
			
			if comment.author.id == user_id:
				comment.delete()
				return HttpResponse('true')
			else:
				return HttpResponse('false')

		else:
			return HttpResponse('false')

	else:
		raise Http404