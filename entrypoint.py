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
        if     arg == '--iname':                    ZabbixInterface.output(k.iname)
        elif   arg == '--dont-track-primary':       ZabbixInterface.output(ZabbixInterface.intToString(k.dont_track_primary))
        elif   arg == '--skip-check-adv-addr':      ZabbixInterface.output(ZabbixInterface.intToString(k.skip_check_adv_addr))
        elif   arg == '--strict-mode':              ZabbixInterface.output(ZabbixInterface.intToString(k.strict_mode))
        elif   arg == '--vmac-ifname':              ZabbixInterface.output(k.vmac_ifname)
        elif   arg == '--ifp-ifname':               ZabbixInterface.output(k.ifp_ifname)
        elif   arg == '--master-priority':          ZabbixInterface.output(ZabbixInterface.intToString(k.master_priority))
        elif   arg == '--last-transition':          ZabbixInterface.output(k.last_transition)
        # elif <garps>
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
        elif   arg == '--script-backup':            ZabbixInterface.output(k.script_backup)
        elif   arg == '--script-master':            ZabbixInterface.output(k.script_master)
        elif   arg == '--script-fault':             ZabbixInterface.output(k.script_fault)
        elif   arg == '--script-stop':              ZabbixInterface.output(k.script_stop)
        # stats
        elif   arg == '--advert-rcvd':              ZabbixInterface.output(ZabbixInterface.intToString(k.advert_rcvd))
        elif   arg == '--advert-sent':              ZabbixInterface.output(ZabbixInterface.intToString(k.advert_sent))
        elif   arg == '--become-master':            ZabbixInterface.output(ZabbixInterface.intToString(k.become_master))
        elif   arg == '--release-master':           ZabbixInterface.output(ZabbixInterface.intToString(k.release_master))
        elif   arg == '--packet-len-err':           ZabbixInterface.output(ZabbixInterface.intToString(k.packet_len_err))
        elif   arg == '--advert-interval-err':      ZabbixInterface.output(ZabbixInterface.intToString(k.advert_interval_err))
        elif   arg == '--ip-ttl-err':               ZabbixInterface.output(ZabbixInterface.intToString(k.ip_ttl_err))
        elif   arg == '--invalid-type-rcvd':        ZabbixInterface.output(ZabbixInterface.intToString(k.invalid_type_rcvd))
        elif   arg == '--addr-list-err':            ZabbixInterface.output(ZabbixInterface.intToString(k.addr_list_err))
        elif   arg == '--invalid-authtype':         ZabbixInterface.output(ZabbixInterface.intToString(k.invalid_authtype))
        elif   arg == '--authtype-mismatch':        ZabbixInterface.output(ZabbixInterface.intToString(k.authtype_mismatch))
        elif   arg == '--auth-failure':             ZabbixInterface.output(ZabbixInterface.intToString(k.auth_failure))
        elif   arg == '--pri-zero-rcvd':            ZabbixInterface.output(ZabbixInterface.intToString(k.pri_zero_rcvd))
        elif   arg == '--pri-zero-sent':            ZabbixInterface.output(ZabbixInterface.intToString(k.pri_zero_sent))
        # help
        else:                                       cli(["LICENSE", "HELP"])

exit()
sys.exit()
