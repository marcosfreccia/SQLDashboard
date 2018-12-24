# SQL Dashboard

The tool is an attempt to deliver SQL Server tasks via a self-service portal. The tool is written in
Python and Django and uses SQL Server as the database backend.


## Enabling Social Authentication

As of now, SQL Dashboard is enabled to use the following authentication backends: Github and Google.
If you want to use any of those methods, please follow the below article to setup for your
environment.

https://fosstack.com/how-to-add-google-authentication-in-django/

## Settings.cfg

SQL Dashboard uses a configuration file to store some confidential information such as: Django
Secret Key, Database credentials, Github and Google Keys for the authentication backend.

```[django_secret_key]
secret_key_value: DjangoKeyHere

[sqlserver_default]
host: server_name
database: database_name
username: YourUser
password: YourPassword


[LOGGING_SETTINGS] 
log_path: LoggingFolder

[active_directory_servers]
dc_server_01: ServerName
dc_server_02: ServerName


[github_auth]
SOCIAL_AUTH_GITHUB_KEY: YourKey
SOCIAL_AUTH_GITHUB_SECRET: YourSecret

[google_auth]
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY: YourKey
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET: YourSecret
```
