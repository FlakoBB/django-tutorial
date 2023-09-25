from django.urls import path
from . import views

# * Configuracion de URL para las vistas
app_name = 'polls'
urlpatterns = [
  # polls/
  path('', views.index, name = 'index'),
  # polls/30/
  path('specifics/<int:question_id>/', views.detail, name='detail'),
  # polls/30/results/
  path('<int:question_id>/results/', views.results, name='results'),
  # polls/30/vote/
  path('<int:question_id>/vote/', views.vote, name='vote'),
]