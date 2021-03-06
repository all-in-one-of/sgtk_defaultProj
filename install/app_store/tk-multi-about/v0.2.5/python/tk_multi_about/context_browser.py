# Copyright (c) 2013 Shotgun Software Inc.
# 
# CONFIDENTIAL AND PROPRIETARY
# 
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit 
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your 
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights 
# not expressly granted therein are reserved by Shotgun Software Inc.

import tank
import os
import sys
import datetime
import threading 


from tank.platform.qt import QtCore, QtGui

browser_widget = tank.platform.import_framework("tk-framework-widget", "browser_widget")


class ContextBrowserWidget(browser_widget.BrowserWidget):

    
    def __init__(self, parent=None):
        browser_widget.BrowserWidget.__init__(self, parent)
    
    def get_data(self, data):
    
        data = {}
        
        ctx = self._app.context

        if ctx.project:
            # get project data
            data["project"] = self._app.shotgun.find_one("Project", 
                                                         [ ["id", "is", ctx.project["id"]] ], 
                                                         ["name", "sg_description", "image"])
            
        if ctx.entity:
            # get entity data
            data["entity"] = self._app.shotgun.find_one(ctx.entity["type"], 
                                                        [ ["id", "is", ctx.entity["id"]] ], 
                                                        ["code", "description", "image"])
            
        if ctx.step:
            # get step data
            data["step"] = self._app.shotgun.find_one("Step", 
                                                      [ ["id", "is", ctx.step["id"]] ], 
                                                      ["code", "description"])

            
        if ctx.task:
            # get task data
            data["task"] = self._app.shotgun.find_one("Task", 
                                                      [ ["id", "is", ctx.task["id"]] ], 
                                                      ["content", "image", "task_assignees", "sg_status_list"])


        data["additional"] = []            
        for ae in ctx.additional_entities:
            # additional entity data
            d = self._app.shotgun.find_one(ae["type"], 
                                           [ ["id", "is", ae["id"]] ], 
                                           ["code", "description", "image"])
            data["additional"].append(d)
            
    
        return data
            

    def process_result(self, result):

        if result.get("project"):
            d = result["project"]
            
            i = self.add_item(browser_widget.ListItem)
            details = []
            details.append("<b>Project %s</b>" % d.get("name"))
            details.append( d.get("sg_description") if d.get("sg_description") else "No Description" )            
            i.set_details("<br>".join(details))
            i.sg_data = d
            i.setToolTip("Double click to see more details in Shotgun.")
            
            if d.get("image"):
                i.set_thumbnail(d.get("image"))

        if result.get("entity"):
            d = result["entity"]
            
            i = self.add_item(browser_widget.ListItem)
            details = []
            nice_name = tank.util.get_entity_type_display_name(self._app.tank, d.get("type"))
            details.append("<b>%s %s</b>" % (nice_name, d.get("code")))
            details.append( d.get("description") if d.get("description") else "No Description" )         
            i.set_details("<br>".join(details))
            i.sg_data = d
            i.setToolTip("Double click to see more details in Shotgun.")
            
            if d.get("image"):
                i.set_thumbnail(d.get("image"))
        
        for d in result["additional"]:
            
            i = self.add_item(browser_widget.ListItem)
            details = []
            nice_name = tank.util.get_entity_type_display_name(self._app.tank, d.get("type"))
            details.append("<b>%s %s</b>" % (nice_name, d.get("code")))
            details.append( d.get("description") if d.get("description") else "No Description" )    
            i.set_details("<br>".join(details))
            i.sg_data = d
            i.setToolTip("Double click to see more details in Shotgun.")
            
            if d.get("image"):
                i.set_thumbnail(d.get("image"))

        if result.get("step"):
            d = result["step"]
            
            i = self.add_item(browser_widget.ListItem)
            details = []
            details.append("<b>Pipeline Step %s</b>" % d.get("code", ""))
            details.append( d.get("description") if d.get("description") else "No Description" )      
            i.set_details("<br>".join(details))
            i.sg_data = d
            i.setToolTip("Double click to see more details in Shotgun.")
            i.set_thumbnail(":/res/pipeline_step.png")
        
        if result.get("task"):
            d = result["task"]
            
            i = self.add_item(browser_widget.ListItem)
            details = []
            details.append("<b>Task %s</b>" % d.get("content"))
            details.append("Status: %s" % d.get("sg_status_list"))
    
            names = [ x.get("name") for x in d.get("task_assignees", []) ]
            names_str = ", ".join(names)
            details.append("Assigned to: %s" % names_str)
      
            i.set_details("<br>".join(details))
            i.sg_data = d
            i.setToolTip("Double click to see more details in Shotgun.")
            
            if d.get("image"):
                i.set_thumbnail(d.get("image"))
        