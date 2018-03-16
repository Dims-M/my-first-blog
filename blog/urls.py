from django.conf.urls import url
from . import views #  импортируем файл с логикой

urlpatterns = [
	# регулярное выражение. При в воде пустого значения срабатывает метод описанный в файле views 
    url(r'^$', views.post_list, name='post_list'),
    
]
