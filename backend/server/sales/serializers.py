from rest_framework import serializers
from server.sales.models import Agent, Report


class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = ('name', 'city', 'birthday', 'hire_date')


class ReportSerializer(serializers.ModelSerializer):
    agent_name = serializers.SerializerMethodField('get_agent_name')

    def get_agent_name(self, obj):
        return obj.agent.name

    class Meta:
        model = Report
        fields = ('agent_name', 'period', 'volume')
