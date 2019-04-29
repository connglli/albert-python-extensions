# -*- coding: utf-8 -*-

"""Control network proxy status.
Usage: proxy <status>
Example: proxy manual"""

from albertv0 import *

__iid__ = "PythonInterface/v0.1"
__prettyname__ = "Set Network Proxy"
__version__ = "1.0"
__trigger__ = "proxy "
__author__ = "Simon Lee"
__dependencies__ = []


def handleQuery(query):
    STATUS_NONE = "none"
    STATUS_NONE_SHORT = "n"
    STATUS_NONE_COMMAND = ["gsettings", "set", "org.gnome.system.proxy", "mode", STATUS_NONE]
    STATUS_AUTO = "auto"
    STATUS_AUTO_SHORT = "a"
    STATUS_AUTO_COMMAND = ["gsettings", "set", "org.gnome.system.proxy", "mode", STATUS_AUTO]
    STATUS_MANUAL = "manual"
    STATUS_MANUAL_SHORT = "m"
    STATUS_MANUAL_COMMAND = ["gsettings", "set", "org.gnome.system.proxy", "mode", STATUS_MANUAL]

    if query.isTriggered:
        fields = query.string.split()
        item = Item(id=__prettyname__, completion=query.rawString)
        if len(fields) == 1:
            try:
                status = fields[0].lower()
                if status == STATUS_NONE_SHORT or STATUS_NONE.startswith(status):
                    item.text = "Set Network Proxy: None"
                    item.subtext = "press enter or click to set"
                    item.addAction(TermAction("None", STATUS_NONE_COMMAND))
                elif status == STATUS_AUTO_SHORT or STATUS_AUTO.startswith(status):
                    item.text = "Set Network Proxy: Auto"
                    item.subtext = "press enter or click to set"
                    item.addAction(TermAction("Auto", STATUS_AUTO_COMMAND))
                elif status == STATUS_MANUAL_SHORT or STATUS_MANUAL.startswith(status):
                    item.text = "Set Network Proxy: Manual"
                    item.subtext = "press enter or click to set"
                    item.addAction(TermAction("Manual", STATUS_MANUAL_COMMAND))
                else:
                    item.text = __prettyname__
                    item.subtext = "Valid status are: %s, %s, and %s" % (STATUS_NONE, STATUS_AUTO, STATUS_MANUAL)
            except Exception as e:
                item.text = e.__class__.__name__
                item.subtext = str(e)
            return item
        else:
            item.text = __prettyname__
            item.subtext = "Valid status are: %s, %s, and %s" % (STATUS_NONE, STATUS_AUTO, STATUS_MANUAL)
            return item
