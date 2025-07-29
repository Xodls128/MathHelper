from rest_framework import generics, permissions
from solutions.models import Solution
from solutions.serializers.solution import SolutionSerializer

class SolutionCreateView(generics.CreateAPIView):
    serializer_class = SolutionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class MySolutionListView(generics.ListAPIView):
    serializer_class = SolutionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Solution.objects.filter(user=self.request.user)

class ProblemSolutionListView(generics.ListAPIView):
    serializer_class = SolutionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        problem_id = self.kwargs['problem_id']
        return Solution.objects.filter(problem__id=problem_id)
