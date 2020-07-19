from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import views
from server.sales.models import Agent, Report
from server.sales.serializers import AgentSerializer, ReportSerializer
from datetime import datetime


# Create your views here.


class AgentView(views.APIView):
    def post(self, request):
        try:
            new_agent = Agent()
            new_agent.name = request.data['name']
            new_agent.city = request.data['city']
            new_agent.hire_date = request.data.get('hire_date', datetime.today())
            new_agent.birthday = request.data['birthday']
            new_agent.save()
            return JsonResponse({}, status=201)
        except Exception as e:
            return JsonResponse({}, status=503)


    def get(self, request):
        data = AgentSerializer(Agent.objects.all(), many=True).data
        return JsonResponse(data, safe=False, status=200)


class ReportView(views.APIView):
    def post(selfs, request):
        try:
            new_report = Report(agent=Agent.objects.get(id=request.data['agent_id']))
            new_report.volume = request.data['volume']
            new_report.period = datetime.strptime(request.data['period'], '%Y, %B').date()
            new_report.save()
            return JsonResponse({}, status=201)
        except Exception as e:
            return JsonResponse({}, status=503)

    def get(self, request):
        agent_id = request.query_params.get('agent_id')
        agent_name = request.query_params.get('agent_name')
        if agent_id:
            data = ReportSerializer(Report.objects.filter(agent=agent_id), many=True).data
        elif agent_name:
            data = ReportSerializer(Report.objects.filter(agent__name=agent_name), many=True).data
        else:
            data = ReportSerializer(Report.objects.all(), many=True).data
        return JsonResponse(data, safe=False, status=200)
