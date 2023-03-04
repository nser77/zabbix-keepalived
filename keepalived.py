import subprocess
from subprocess import Popen, PIPE

from datetime import datetime

from json import load

class KeepalivedBase(object):
    errors = []
    human_data_convertion = '%Y-%m-%d %H:%M:%S'

    def timestampToHuman(self, timestamp):
        human = datetime.fromtimestamp(timestamp).strftime(self.human_data_convertion)
        return human

class KeepalivedData(KeepalivedBase):
    """
    Implement here your KeepalivedData methos.
    """
    def data(self, data):
        self.iname =                   data['iname']
        self.dont_track_primary =      data['dont_track_primary']
        self.skip_check_adv_addr =     data['skip_check_adv_addr']
        self.strict_mode =             data['strict_mode']
        self.vmac_ifname =             data['vmac_ifname']
        self.ifp_ifname =              data['ifp_ifname']
        self.master_priority =         data['master_priority']
        self.setLastTransition(        data['last_transition'])
        self.garp_delay =              data['garp_delay']
        self.garp_refresh =            data['garp_refresh']
        self.garp_rep =                data['garp_rep']
        self.garp_refresh_rep =        data['garp_refresh_rep']
        self.garp_lower_prio_delay =   data['garp_refresh_rep']
        self.garp_lower_prio_rep =     data['garp_lower_prio_rep']
        self.lower_prio_no_advert =    data['lower_prio_no_advert']
        self.higher_prio_send_advert = data['higher_prio_send_advert']
        self.vrid =                    data['vrid']
        self.base_priority =           data['base_priority']
        self.effective_priority =      data['effective_priority']
        self.vipset =                  data['vipset']
        self.promote_secondaries =     data['promote_secondaries']
        self.adver_int =               data['adver_int']
        self.master_adver_int =        data['master_adver_int']
        self.setAccept(                data['accept'])

    def setLastTransition(self, last_transition):
        self.last_transition = self.timestampToHuman(last_transition)

    def setAccept(self, accept):
        if self.strict_mode:
            if self.strict_mode == 1 and self.accept == 0
                # you may experience some issues
                self.errors.append("self.strict_mode == 1 and self.accept == 0")
        self.accept = accept

class KeepalivedStats(KeepalivedBase):
    """
    Implement here your KeepalivedStats methos.
    """
    def stats(self, stats):
        self.advert_rcvd =            stats['advert_rcvd']
        self.become_master =          stats['become_master']

class Keepalived(KeepalivedData, KeepalivedStats):
    def __init__(self, json):
        self.data(json[0]['data'])
        self.stats(json[0]['stats'])

class KeepalivedInterface():
    pid = '/run/keepalived/keepalived.pid'

    @staticmethod
    def _readSubprocess(command):
        with Popen(command, shell=True, stdout=PIPE) as p:
            p.wait()
            return p.communicate()[0]

    @staticmethod
    def _runSubprocess(command):
        with Popen(command, shell=True) as p:
            p.wait()
            return p

    @staticmethod
    def getSigfunc():
        command='kill -s $(keepalived --signum=JSON) $(cat {pid})'.format(pid=KeepalivedInterface.pid)
        return command

    @staticmethod
    def getTmpFile():
        p = KeepalivedInterface._readSubprocess('ls /tmp | grep -i keepalived | grep -iv /').split(b"\n")
        return "/tmp/{}/tmp/keepalived.json".format(p[0].decode("utf-8"))

    @staticmethod
    def getKeepalived():
        if not KeepalivedInterface._runSubprocess(KeepalivedInterface.getSigfunc()):
            raise Except("Subprocess error")
        with open(KeepalivedInterface.getTmpFile()) as json:
            j=load(json)
            return Keepalived(j)
