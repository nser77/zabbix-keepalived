# zabbix-keepalived
ZABBIX script to monitor [keepalived](https://github.com/acassen/keepalived) instances through [keepalived-wrapper](https://github.com/nser77/keepalived-wrapper).

## Installation
Installation steps:
```
root@ubuntu:/opt# git clone https://github.com/nser77/zabbix-keepalived.git
root@ubuntu:/opt# cd zabbix-keepalived/
root@ubuntu:/opt/zabbix-keepalived# virtualenv ./virtualenv
root@ubuntu:/opt/zabbix-keepalived# source ./virtualenv/bin/activate
(virtualenv) root@ubuntu:/opt/zabbix-keepalived# pip install -r requirements.txt
(virtualenv) root@ubuntu:/opt/zabbix-keepalived# deactivate
```

## Usage
For more information see the [```HELP```](HELP) file.
```
root@ubuntu:/opt/zabbix-keepalived# ./virtualenv/bin/python entrypoint.py VI_2 --vrid
98
root@ubuntu:/opt/zabbix-keepalived# ./virtualenv/bin/python entrypoint.py VI_1 --vrid
99
```

## Permissions
You may want to set the correct permissions and ownerships for the ```zabbix-keepalived``` source files.

## Documentation
In this article [Command execution appendix](https://www.zabbix.com/documentation/current/en/manual/appendix/command_execution) are detailed a lot of interesting informations about ZABBIX remote command execution (output, remote commands).

There a lot of choices to run remote commands with ZABBIX agent:
 - [User parameters](https://www.zabbix.com/documentation/current/en/manual/config/items/userparameters)
 - [system.run](https://www.zabbix.com/documentation/current/en/manual/config/items/itemtypes/zabbix_agent#system.runcommandmode)
