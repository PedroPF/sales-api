# Build Angular
to build Angular into Django static folder use 

```
ng build --prod --output-path ..\backend\server\static\ang\ --watch --output-hashing none
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
	'agent_id': <agent_id>
	'volume': <volume>
	'period': <period>(optional)
}
```
will create a Report linked to the supplied Agent for the given month, if the month is not given it will fill with current month.

The period has to be in the 'YYYY, MMMM' format, where MMMM is the full month name