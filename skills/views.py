from django.http import JsonResponse
from django.views import View
from .models import Skills


class SkillList(View):
    def get(self, request):
        skills = Skills.objects.all()
        data = [skill.to_json() for skill in skills]
        return JsonResponse(data, safe=False)
