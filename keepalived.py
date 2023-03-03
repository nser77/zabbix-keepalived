import subprocess
from subprocess import Popen, PIPE

from datetime import datetime

from json import load

class Keepalived(object):
    def __init__(self, json):
        self.populateData(json[0]['data'])
        self.populateStats(json[0]['stats'])

    def populateData(self, data):
        # crear clase super
        self.iname =                  data['iname']
        self.dont_track_primary =     data['dont_track_primary']
        self.skip_check_adv_addr =    data['skip_check_adv_addr']
        self.strict_mode =            data['strict_mode']
        self.vmac_ifname =            data['vmac_ifname']
        self.ifp_ifname =             data['ifp_ifname']
        self.master_priority =        data['master_priority']
        self.setLastTransition(       data['last_transition'])
        self.garp_delay =             data['garp_delay']
        self.garp_refresh =           data['garp_refresh']

    def setLastTransition(self, last_transition):
        self.last_transition = datetime.fromtimestamp(last_transition).strftime('%Y-%m-%d %H:%M:%S')
        return None

    def populateStats(self, stats):
        # crear clase super
        self.advert_rcvd              = stats['advert_rcvd']
        self.become_master            = stats['become_master']

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
