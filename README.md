# zabbix-keepalived
ZABBIX script to monitor [keepalived](https://github.com/acassen/keepalived) instances through [keepalived-wrapper](https://github.com/nser77/keepalived-wrapper).

## Notes
In this article [```Command execution appendix```](https://www.zabbix.com/documentation/current/en/manual/appendix/command_execution) are detailed a lot of interesting informations about ZABBIX remote command execution (output, remote commands).

There a lot of choices to run remote commands with ZABBIX Agent:
 - [User parameters](https://www.zabbix.com/documentation/current/en/manual/config/items/userparameters)
 - [system.run](https://www.zabbix.com/documentation/current/en/manual/config/items/itemtypes/zabbix_agent#system.runcommandmode)

## Installation

```
root@ubuntu:/opt# git clone https://github.com/nser77/zabbix-keepalived.git
root@ubuntu:/opt# cd zabbix-keepalived/
root@ubuntu:/opt# virtualenv ./virtualenv
root@ubuntu:/opt# source ./virtualenv/bin/activate
(virtualenv) root@ubuntu:/opt# pip install -r requirements.txt
(virtualenv) root@ubuntu:/opt# deactivate
root@ubuntu:/opt# chmod +x entrypoint.py
```
