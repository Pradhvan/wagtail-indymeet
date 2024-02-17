#!/bin/sh
# This file is configured to be used within the environment variables
# in the App Service under Configuration > General Settings > Startup Command

# Start supervisord
supervisord -c supervisord.conf

# This is the existing file that's generated by Oryx and how Azure
# wants to start up our App Service. It ends in a gunicorn command
/opt/startup/startup.sh
