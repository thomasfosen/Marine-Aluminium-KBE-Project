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


from Optimizer import Optimizer
#setup json for commmand-handling?



#displayPart = theSession.Parts.Display

def load(name, c):
    theSession  = NXOpen.Session.GetSession()
    workPart = theSession.Parts.Work
    workPart.RuleManager.CreateDynamicRule("root:", name, "Child", "{\n Class, " + c + "; \n}", None)


def delete(name):
    theSession  = NXOpen.Session.GetSession()
    workPart = theSession.Parts.Work
    workPart.RuleManager.DeleteDynamicRule("root:", name)


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
    elif message[:4] == 'load':
        cmd = message.split(' ')
        load(cmd[1], cmd[2])
    elif message == 'refresh':

        #theSession  = NXOpen.Session.GetSession()
        #workPart = theSession.Parts.Work
        theSession  = NXOpen.Session.GetSession()
        workPart = theSession.Parts.Work

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

    elif message == 'stop':



        asyncio.get_event_loop().stop()
        #websockets.close()
        #need to implement graceful shutdown
        await websocketswait_closed()
    #await

    #asyncio.get_event_loop().stop()
    elif message == 'capture':
        img_name = "preview.png"
        img_save_path = "C:\\Users\\tuanat\\Desktop\\KBE Course\\dfa_server\\static\\" + img_name
        img_save_path = "C:\\Users\\Tuan\\meta\\KBEChairProject\\web_server\\static\\" + img_name
        theUI = NXOpen.UI.GetUI()
        imageExportBuilder1 = theUI.CreateImageExportBuilder()
        imageExportBuilder1.FileName = img_save_path

        #final saving code
        nXObject1 = imageExportBuilder1.Commit()

    #command anatomy: "optimize 10000 20000"
    elif message[:8] == 'optimize':
        cmd = message.split(' ')
        force = cmd[1]
        torque = cmd[2]

        AA5086_yield = 215 #MPa
        safety_factor = 1.4

        target_stress = AA5086_yield / safety_factor

        optimizer = Optimizer('model1', 'C:/Users/tuanat/Desktop/The loop')

        optimizer.go_to_sim()
        optimizer.update_force(30000)
        optimizer.update_torque(50000)

        optimizer.optimize(target_stress)

#port stuff checkme
start_server = websockets.serve(response, 'localhost', 1234)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
