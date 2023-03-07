#!/usr/bin/env python3

import sys

from keepalived.wrapper import KeepalivedInterface
from zabbix import ZabbixInterface

def help(listput):
    if not type(listput) == list:
        raise Exception("Cli accepts only <list> type as input")
    for file in listput:
        with open(file) as f:
            print(f.read())

try:
    arg=sys.argv[1]
except:
    help(["LICENSE", "HELP"])
    exit()
    sys.exit()

commands=[
    "--iname", "--dont-track-primary", '--skip-check-adv-addr',
    "--become-master", "--last-transition",
    "--bool-example",
    "--help", "--license"
]

if not arg in commands:
    help(["LICENSE", "HELP"])
    exit()
    sys.exit()

# this should be a cli param
instance="VI_1"

for k in KeepalivedInterface.getVrrp():
    if k.iname == instance:
        if     arg == '--iname':               ZabbixInterface.output(k.iname)
        elif   arg == '--dont-track-primary':  ZabbixInterface.output(ZabbixInterface.intToString(k.dont_track_primary))
        elif   arg == '--skip-check-adv-addr': ZabbixInterface.output(ZabbixInterface.intToString(k.skip_check_adv_addr))
        elif   arg == '--strict-mode':         ZabbixInterface.output(ZabbixInterface.intToString(k.strict_mode))
        elif   arg == '--become-master':       ZabbixInterface.output(ZabbixInterface.intToString(k.become_master))
        elif   arg == '--last-transition':     ZabbixInterface.output(k.last_transition)
        elif   arg == '--bool-example':        ZabbixInterface.output(ZabbixInterface.intToString(ZabbixInterface.boolToInt(True)))
        elif   arg == '--license':             help(["LICENSE"])
        elif   arg == '--help':                help(["LICENSE", "HELP"])

exit()
sys.exit()
