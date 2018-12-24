# Getting Started

To use SQL Dashboard, there are a few things necessary to be done. In this getting started document,
I hope to cover the things that you need to do.

## Installing Python

The very first thing to do in the server where you plan to run SQL Dashboard is install Python 3.6.
To do this, go to the [Python.org](http://www.python.org) page and click on downloads page.

The web page detects the operating system of your server or laptop and will let you download the right Python installation for your OS, but you can still download to other Operating Systems as well.

SQL Dashborad runs on Windows Server, so I just go and download Python for Windows.

After the downloaded has completed, proceed to install Python in your environment.

## Clonning the project

Decide where in the file system you wish to place SQL Dashboard and clone the project by executing the code below in the command prompt.

```git clone https://github.com/marcosfreccia/SQLDashboard.git ```

If you don't have in your laptop or server the github cli, you can just download the zip file.

## Creating the virtual environment

Virtual Environments helps you to isolate your Python applications. When you have multiple Python projects running in the same server, the virtual environment helps to keep everything isolated and also helps when certain projects has package version dependencies. I've written the below blog post to explain how to create a new virtual environment.

[https://marcosfreccia.com/2017/12/21/python-virtual-environments-be-safe/](https://marcosfreccia.com/2017/12/21/python-virtual-environments-be-safe/)

## Enabling Social Authentication

Django supports several authentication back-ends.  At this moment, SQL Dashboard is enabled to use the following authentication back-ends: Github and Google. If you want to use any of those methods, please follow the below article to setup for your environment.

[https://fosstack.com/how-to-add-google-authentication-in-django/](https://fosstack.com/how-to-add-google-authentication-in-django/)

## Creating the settings.cfg

In the settings.cfg we store environment variables such as: database hosts and credentials, django secret keys, etc..

Create a new txt file and put the content on it.

```
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
The file should be placed in the root folder of SQL Dashboard. Being simple, it should be in the same folder where the file manage.py is contained. 