from rest_framework import serializers
from server.sales.models import Agent, Report


class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = ('name', 'city', 'birthday', 'hire_date')
