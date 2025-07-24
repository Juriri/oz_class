"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse, Http404

movie_list = [
    {'title': '기생충', 'director': '봉준호', 'index': 4},
    {'title': '범죄도시 2', 'director': '이상용', 'index': 2},
    {'title': '극한직업', 'director': '이병헌', 'index': 1},
    {'title': '서울의 봄', 'director': '김성수', 'index': 3},
]

def movies(request):
    sorted_movies = sorted(movie_list, key=lambda x: x['index'])
    movie_infos = [
        f"순위 {movie['index']}. {movie['title']} - {movie['director']}"
        for i, movie in enumerate(sorted_movies)
    ]
    response_text = "<br>".join(movie_infos)
    return HttpResponse(response_text)


def movies_detail(request, index):
    try:
        movie = movie_list[index]
        response_text = f"{index}. {movie['title']} - {movie['director']} (index: {movie['index']})"
        return HttpResponse(response_text)
    except IndexError:
        raise Http404("해당 인덱스의 영화가 없습니다.")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/', movies),
    path('movies/<int:index>/', movies_detail),
]
