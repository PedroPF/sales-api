from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import views
from server.sales.models import Agent, Report
from server.sales.serializers import AgentSerializer, ReportSerializer


# Create your views here.


class AgentView(views.APIView):
    def post(self):
        return JsonResponse(status=500)


    def get(self, request):
        data = AgentSerializer(Agent.objects.all(), many=True).data
        return JsonResponse(data, safe=False, status=200)


class ReportView(views.APIView):
    def get(self, request):
        data = ReportSerializer(Report.objects.all(), many=True).data
        return JsonResponse(data, safe=False, status=200)
