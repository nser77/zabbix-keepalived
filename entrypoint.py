#!/usr/bin/env python3

import sys

from keepalived.wrapper import KeepalivedInterface
from zabbix import ZabbixInterface

def cli(listput):
    if not type(listput) == list:
        raise Exception("Cli accepts only <list> type as input")

    for file in listput:
        with open(file) as f:
            print(f.read())

try:
    instance = sys.argv[1]
    arg = sys.argv[2]
except:
    cli(["LICENSE", "HELP"])
    exit()
    sys.exit()

for k in KeepalivedInterface.getVrrp():
    if k.iname == instance:
        # data
        if     arg == '--iname':                ZabbixInterface.output(k.iname)
        elif   arg == '--dont-track-primary':   ZabbixInterface.output(ZabbixInterface.intToString(k.dont_track_primary))
        elif   arg == '--skip-check-adv-addr':  ZabbixInterface.output(ZabbixInterface.intToString(k.skip_check_adv_addr))
        elif   arg == '--strict-mode':          ZabbixInterface.output(ZabbixInterface.intToString(k.strict_mode))
        elif   arg == '--vmac-ifname':          ZabbixInterface.output(k.vmac_ifname)
        elif   arg == '--ifp-ifname':           ZabbixInterface.output(k.ifp_ifname)
        elif   arg == '--master-priority':      ZabbixInterface.output(ZabbixInterface.intToString(k.master_priority))
        elif   arg == '--last-transition':      ZabbixInterface.output(k.last_transition)
        # elif <garps>
        elif   arg == '--lower-prio-no-advert': ZabbixInterface.output(ZabbixInterface.intToString(k.lower_prio_no_advert))

        # stats
        elif   arg == '--become-master':        ZabbixInterface.output(ZabbixInterface.intToString(k.become_master))

        # helps
        elif   arg == '--bool-example':         ZabbixInterface.output(ZabbixInterface.intToString(ZabbixInterface.boolToInt(True)))
        elif   arg == '--license':              cli(["LICENSE"])
        elif   arg == '--help':                 cli(["LICENSE", "HELP"])
        else:                                   cli(["LICENSE", "HELP"])

exit()
sys.exit()
