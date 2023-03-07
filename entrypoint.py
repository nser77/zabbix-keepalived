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
        if     arg == '--iname':                    ZabbixInterface.output(k.iname)
        elif   arg == '--dont-track-primary':       ZabbixInterface.output(ZabbixInterface.intToString(k.dont_track_primary))
        elif   arg == '--skip-check-adv-addr':      ZabbixInterface.output(ZabbixInterface.intToString(k.skip_check_adv_addr))
        elif   arg == '--strict-mode':              ZabbixInterface.output(ZabbixInterface.intToString(k.strict_mode))
        elif   arg == '--vmac-ifname':              ZabbixInterface.output(k.vmac_ifname)
        elif   arg == '--ifp-ifname':               ZabbixInterface.output(k.ifp_ifname)
        elif   arg == '--master-priority':          ZabbixInterface.output(ZabbixInterface.intToString(k.master_priority))
        elif   arg == '--last-transition':          ZabbixInterface.output(k.last_transition)
        # <garps>
        elif   arg == '--lower-prio-no-advert':     ZabbixInterface.output(ZabbixInterface.intToString(k.lower_prio_no_advert))
        elif   arg == '--higher-prio-send-advert':  ZabbixInterface.output(ZabbixInterface.intToString(k.higher_prio_send_advert))
        elif   arg == '--vrid':                     ZabbixInterface.output(ZabbixInterface.intToString(k.vrid))
        elif   arg == '--base-priority':            ZabbixInterface.output(ZabbixInterface.intToString(k.base_priority))
        elif   arg == '--effective-priority':       ZabbixInterface.output(ZabbixInterface.intToString(k.effective_priority))
        elif   arg == '--vipset':                   ZabbixInterface.output(ZabbixInterface.intToString(ZabbixInterface.boolToInt(k.vipset)))
        elif   arg == '--promote-secondaries':      ZabbixInterface.output(ZabbixInterface.intToString(ZabbixInterface.boolToInt(k.promote_secondaries)))
        elif   arg == '--adver-int':                ZabbixInterface.output(ZabbixInterface.intToString(k.adver_int))
        elif   arg == '--master-adver-int':         ZabbixInterface.output(ZabbixInterface.intToString(k.master_adver_int))
        elif   arg == '--accept':                   ZabbixInterface.output(ZabbixInterface.intToString(k.accept))
        elif   arg == '--nopreempt':                ZabbixInterface.output(ZabbixInterface.intToString(ZabbixInterface.boolToInt(k.nopreempt)))
        elif   arg == '--preempt-delay':            ZabbixInterface.output(ZabbixInterface.intToString(k.preempt_delay))
        elif   arg == '--state':                    ZabbixInterface.output(ZabbixInterface.intToString(k.state))
        elif   arg == '--wantstate':                ZabbixInterface.output(ZabbixInterface.intToString(k.wantstate))
        elif   arg == '--version':                  ZabbixInterface.output(ZabbixInterface.intToString(k.version))
        elif   arg == '--smtp-alert':               ZabbixInterface.output(ZabbixInterface.intToString(ZabbixInterface.boolToInt(k.smtp_alert)))
        elif   arg == '--notify-deleted':           ZabbixInterface.output(ZabbixInterface.intToString(ZabbixInterface.boolToInt(k.notify_deleted)))
        # stats
        elif   arg == '--become-master':            ZabbixInterface.output(ZabbixInterface.intToString(k.become_master))
        # help
        else:                                       cli(["LICENSE", "HELP"])

exit()
sys.exit()
