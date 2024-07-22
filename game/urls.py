from django.urls import path
from .views import index, login_view, interrogation_view, witness_suspects

urlpatterns = [
    path('', index, name='index'),
    path('login/', login_view, name='login'),
    path('interrogation/', interrogation_view, name='interrogation'),
    path('witness_suspects/', witness_suspects, name='witness_suspects'),
]