from django.urls import path
from problems.views import ProblemListView, ProblemRetrieveView, ProblemCreateView
from solutions.views import ProblemSolutionListView

urlpatterns = [
    path('', ProblemListView.as_view(), name='problem-list'),
    path('<int:pk>/', ProblemRetrieveView.as_view(), name='problem-detail'),
    path('create/', ProblemCreateView.as_view(), name='problem-create'),
    path('<int:problem_id>/solutions/', ProblemSolutionListView.as_view(), name='problem-solutions'),
]
