# coding=utf-8

#from django.shortcuts import render
from django.views.generic import ListView, TemplateView

from reblog.settings import redis_con


class HomeView(TemplateView):
    template_name = 'main/home.html'

    def get_context_data(self, **kwargs):
        ctx = super(HomeView, self).get_context_data(**kwargs)

        # post:(id) - 使用HASH存储博客的各个字段信息
        # posts:counter - 自增计数器
        # posts:list - ID列表，主要用于分页
        if redis_con.exists('posts:list'):
            post_id_list = redis_con.lrange('posts:list', 0, 10)

            if post_id_list:
                post_list = [{'title': redis_con.hget('post:%s' % post_id, 'title'), 'id': post_id} for post_id in post_id_list]
                ctx['post_list'] = post_list

        return ctx


class PostView(TemplateView):
    template_name = 'main/post.html'

    def get_context_data(self, **kwargs):
        ctx = super(PostView, self).get_context_data(**kwargs)
