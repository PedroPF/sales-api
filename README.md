# Build Angular
to build Angular into Django static folder use 

```
ng build
```

# API

## GETs

A get on 'agent/' will return a list of all registered Sales Agents.

A get on 'report/' will return a list of all registered Sales Reports. If used with optional parameters 'agent_name=' or 'agent_id=' will only return reports by the Agent.

## POSTs

A post on 'agent/' with body 
```
{
	'name': <name>
	'city': <city>
	'hire_date': <hire date>(optional)
	'birthday': <birthday>
}
```
will create a new Agent. 'hire_date' is optional and will fill with current date if not given. 

Both dates need to be in the 'YYYY-MM-DD' format


A post on 'report/' with body
```
{
	'agent_name': <agent_name>
	'volume': <volume>
	'period': <period>(optional)
}
```
will create a Report linked to the supplied Agent for the given month, if the month is not given it will fill with current month.

The period has to be in the 'YYYY, MM' format

# Frontend

The frontend is divided in two tabs:
 
## Agent tab

Allows creating new agents and visualizing existing ones in a table

## Reports tab

Allows creating new reports and visualizing existing ones in a table, the visualization can be filtered using the dropdown menu to display only a specific Agent's reports, and the filter can be removed by using the clear button.

When creating a new report, it will give the user the option to choose between existing agents to fill the Agent field, the period field will ignore the day and only use the month and year, this can be solved by using other technologies, but as this is a prototype and bootstrap datepicker doesnt allow this function, I chose to keep it like that.