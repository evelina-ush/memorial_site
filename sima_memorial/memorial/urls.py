from django.urls import path
from memorial.views import (index, about_page, articles, redirect_to_story_1,
                            redirect_to_story_2, redirect_to_story_3, redirect_to_story_4)
urlpatterns = [
    path('', index),
    path('about/', about_page),
    path('article/<int:number>', articles),
    path('redirect-to-story-1/', redirect_to_story_1, name='redirect_to_story_1'),
    path('redirect-to-story-2/', redirect_to_story_2, name='redirect_to_story_2'),
    path('redirect-to-story-3/', redirect_to_story_3, name='redirect_to_story_3'),
    path('redirect-to-story-4/', redirect_to_story_4, name='redirect_to_story_4')
]