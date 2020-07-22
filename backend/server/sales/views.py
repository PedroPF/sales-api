from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import views
from server.sales.models import Agent, Report
from server.sales.serializers import AgentSerializer, ReportSerializer
from datetime import datetime, timedelta


# Create your views here.


class AgentView(views.APIView):
    authentication_classes = []

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
            return JsonResponse({}, status=400)


    def get(self, request):
        data = AgentSerializer(Agent.objects.all(), many=True).data
        return JsonResponse(data, safe=False, status=200)


class ReportView(views.APIView):
    authentication_classes = []

    def post(selfs, request):
        try:
            agent = Agent.objects.get(name=request.data['agent_name'])
            new_report = Report(agent=agent)
            new_report.volume = request.data['volume']

            period = request.data.get('period', False)
            if period:
                period = datetime.strptime(request.data['period'], '%Y, %m').date()
                if period > datetime.today().date():
                    return JsonResponse({'reason': 'Future date'}, status=400)
            else:
                period = datetime.today().date().replace(day=1)

            if period.year < agent.hire_date.year or\
                    (period.month < agent.hire_date.month and period.year == agent.hire_date.year):
                return JsonResponse({'reason': 'Report before hiring'}, status=400)

            new_report.period = period
            new_report.save()
            return JsonResponse({}, status=201)
        except Exception as e:
            return JsonResponse({'reason': 'Repeated date'}, status=400)

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
