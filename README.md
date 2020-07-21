# Installation

## Backend

Built with python 3.8.4.

0. Go to '/sales-api/backend' folder

1. Run 'pip install -r requirements.txt' to install pip dependencies

2. Run 'python manage.py migrate' to build SQLite database

3. Run 'python manage.py createsuperuser' to create a super user to access /admin/ path

4. Run 'python manage.py runserver' to start the server

## Frontend

Built with Angular 10.0.4/Angular CLI 10.0.3, installation instructions can be found here https://angular.io/guide/setup-local

0. Go to '/sales-api/frontend' folder

1. Run 'npm install'

2. Run 'ng build --prod'

The website should now be up and running on 127.0.0.1:8000

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