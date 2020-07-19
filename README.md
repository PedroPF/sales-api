# Build Angular
to build Angular into Django static folder use 

```
ng build --prod --output-path ..\backend\server\static\ang\ --watch --output-hashing none
```

# API

## GETs

'agent/' will return a list of all registered Sales Agents

'report/' will return a list of all registered Sales Reports