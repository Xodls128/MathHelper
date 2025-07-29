from django.urls import path
from solutions.views import SolutionCreateView, MySolutionListView

urlpatterns = [
    path('', SolutionCreateView.as_view(), name='solution-create'),
    path('mine/', MySolutionListView.as_view(), name='solution-my-list'),
]
