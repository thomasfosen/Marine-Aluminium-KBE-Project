#Written for NX 12.0.2.9
import math
import NXOpen
import time
import sys

#nx has its own local library located in: #C:\Program Files\Siemens\NX 12.0\NXBIN\python
#to add additional libraries, manipulate the python36.zip file
import asyncio
import signal
import websockets

import time

#setup json for commmand-handling?


theSession  = NXOpen.Session.GetSession()
workPart = theSession.Parts.Work
#displayPart = theSession.Parts.Display

def load(name, c):
    #check if the markId1 functions are necessary
    markId1 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Add New Child Rule")
    workPart.RuleManager.CreateDynamicRule("root:", name, "Child", "{\n Class, " + c + "; \n}", None)
    nErrs1 = workPart.RuleManager.DoKfUpdate(markId1)

def delete(name):
    markId2 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Delete Rules")
    workPart.RuleManager.DeleteDynamicRule("root:", name)
    nErrs2 = workPart.RuleManager.DoKfUpdate(markId2)

def capture():
    pass

theNxMessageBox = NXOpen.UI.GetUI().NXMessageBox
async def response(websocket, path):
    message = await websocket.recv()
    #print(f"We got the message from the client: {message}")
    # 	theNxMessageBox.Show("test", NXOpen.NXMessageBoxDialogType.Information, message)
    await websocket.send("Message received! - " + message)
    #theNxMessageBox.Show("test", NXOpen.NXMessageBoxDialogType.Information, message)

    #theNxMessageBox.Show("test", NXOpen.NXMessageBoxDialogType.Information, message)
    if message[:6] == 'delete':
        cmd = message.split(' ')
        delete(cmd[1])
        #theNxMessageBox.Show("test", NXOpen.NXMessageBoxDialogType.Information, message)
    if message[:4] == 'load':
        cmd = message.split(' ')
        load(cmd[1], cmd[2])
    if message == 'refresh':

        #theSession  = NXOpen.Session.GetSession()
        #workPart = theSession.Parts.Work

        workPart.RuleManager.Reload(True)
        workPart.RuleManager.RegenerateAll()
        workPart.ModelingViews.WorkView.Fit()
        #message = 'capture'


        img_name = "preview.png"
        #test server
        img_save_path = "C:\\Users\\tuanat\\Desktop\\KBE_project\\dfa_server\\static\\" + img_name

        #home server
        img_save_path = "C:\\Users\\Tuan\\meta\\KBEChairProject\\web_server\\static\\" + img_name

        theUI = NXOpen.UI.GetUI()
        imageExportBuilder1 = theUI.CreateImageExportBuilder()
        imageExportBuilder1.FileName = img_save_path

        #final saving code
        nXObject1 = imageExportBuilder1.Commit()

    if message == 'stop':



        asyncio.get_event_loop().stop()
        #websockets.close()
        #need to implement graceful shutdown
        await websocketswait_closed()
    #await

    #asyncio.get_event_loop().stop()
    if message == 'capture':
        img_name = "preview.png"
        img_save_path = "C:\\Users\\tuanat\\Desktop\\KBE Course\\dfa_server\\static\\" + img_name
        img_save_path = "C:\\Users\\Tuan\\meta\\KBEChairProject\\web_server\\static\\" + img_name
        theUI = NXOpen.UI.GetUI()
        imageExportBuilder1 = theUI.CreateImageExportBuilder()
        imageExportBuilder1.FileName = img_save_path

        #final saving code
        nXObject1 = imageExportBuilder1.Commit()

#port stuff checkme
start_server = websockets.serve(response, 'localhost', 1234)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
