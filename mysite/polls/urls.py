from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]

"""
[path関数]
第1引数(route引数): URL
第2引数(view引数): URLに対応するview関数を呼び出す。その際HttpRequestオブジェを第一引数に
                　キーワード引数としてrouteからキャプチャされた値を呼び出す。
(クラスベースの場合、viewクラス名でas_viewメソッドを呼び出す)
name引数: テンプレート内で指定するURLの名称
        　名前を付けておけばDjangoのどこからでも参照でき、テンプレートの中で特に有効
(省略するとview関数の名前がそのまま利用される)

"""