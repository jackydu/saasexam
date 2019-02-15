# -*- coding: utf-8 -*-

from django.conf.urls import patterns

urlpatterns = patterns(
    'saas_exam_jacky.views',
    (r'^test/$', 'api_test'),
)