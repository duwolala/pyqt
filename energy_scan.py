__version__ = "Version 201611.22"
import sys
#==============================================================================
# from PIL import Image, ImageFont, ImageDraw
#==============================================================================

#==============================================================================
# from PyQt5.QtWidgets import QApplication
#==============================================================================
#==============================================================================
# import getopt, sys, os, datetime, stat
#==============================================================================
#==============================================================================
# from PIL import Image, ImageFont, ImageDraw
#==============================================================================
from PyQt5.QtWidgets import QApplication, QMainWindow,QFileDialog
from ui_energy import Ui_MainWindow
from epics import caget,caput,PV
import os,sys,math
import numpy as np
import time
import _thread
import csv

def inputtool():
    try :
        Gstatus['edge']=float(MainWin.edt_edge.text())
    except ValueError:
            MainWin.statusbar.showMessage("edge wrong formate")
            return False
    try :
        step[0]=float(MainWin.edt_step1.text())
    except ValueError:
            MainWin.statusbar.showMessage("step1 wrong formate")
            return False
    try :
        step[1]=float(MainWin.edt_step2.text())
    except ValueError:
            MainWin.statusbar.showMessage("step2 wrong formate")
            return False
    try :
        step[2]=float(MainWin.edt_step3.text())
    except ValueError:
            MainWin.statusbar.showMessage("step3 wrong formate")
            return False
    try :
        step[3]=float(MainWin.edt_step4.text())
    except ValueError:
            MainWin.statusbar.showMessage("step4 wrong formate")
            return False
    try :
        step[4]=float(MainWin.edt_step5.text())
    except ValueError:
            MainWin.statusbar.showMessage("step5 wrong formate")
            return False
    try :
        step[5]=float(MainWin.edt_step6.text())
    except ValueError:
            MainWin.statusbar.showMessage("step6 wrong formate")
            return False
    try :
        step[6]=float(MainWin.edt_step7.text())
    except ValueError:
            MainWin.statusbar.showMessage("step7 wrong formate")
            return False
    try :
        energy[0]=float(MainWin.edt_energy1.text())
    except ValueError:
            MainWin.statusbar.showMessage("energy1 wrong formate")
            return False
    try :
        energy[1]=float(MainWin.edt_energy2.text())
    except ValueError:
            MainWin.statusbar.showMessage("energy2 wrong formate")
            return False
    try :
        energy[2]=float(MainWin.edt_energy3.text())
    except ValueError:
            MainWin.statusbar.showMessage("energy3 wrong formate")
            return False
    try :
        energy[3]=float(MainWin.edt_energy4.text())
    except ValueError:
            MainWin.statusbar.showMessage("energy4 wrong formate")
            return False
    try :
        energy[4]=float(MainWin.edt_energy5.text())
    except ValueError:
            MainWin.statusbar.showMessage("energy5 wrong formate")
            return False
    try :
        energy[5]=float(MainWin.edt_energy6.text())
    except ValueError:
            MainWin.statusbar.showMessage("energy6 wrong formate")
            return False
    try :
        energy[6]=float(MainWin.edt_energy7.text())
    except ValueError:
            MainWin.statusbar.showMessage("energy7 wrong formate")
            return False
    try :
        energy[7]=float(MainWin.edt_energy8.text())
    except ValueError:
            MainWin.statusbar.showMessage("energy8 wrong formate")
            return False
    for chk in range(0,8):
        if (Gstatus['edge']+energy[chk])<5000 or (Gstatus['edge']+energy[chk])>25000:
            MainWin.statusbar.showMessage("Energy Out of range!")
            return False
            
    try :
        timeTable[0]=float(MainWin.edt_time1.text())
    except ValueError:
            MainWin.statusbar.showMessage("time1 wrong formate")
            return False
    try :
        timeTable[1]=float(MainWin.edt_time2.text())
    except ValueError:
            MainWin.statusbar.showMessage("time2 wrong formate")
            return False
    try :
        timeTable[2]=float(MainWin.edt_time3.text())
    except ValueError:
            MainWin.statusbar.showMessage("time3 wrong formate")
            return False
    try :
        timeTable[3]=float(MainWin.edt_time4.text())
    except ValueError:
            MainWin.statusbar.showMessage("time4 wrong formate")
            return False
    try :
        timeTable[4]=float(MainWin.edt_time5.text())
    except ValueError:
            MainWin.statusbar.showMessage("stime5 wrong formate")
            return False
    try :
        timeTable[5]=float(MainWin.edt_time6.text())
    except ValueError:
            MainWin.statusbar.showMessage("time6 wrong formate")
            return False
    try :
        timeTable[6]=float(MainWin.edt_time7.text())
    except ValueError:
            MainWin.statusbar.showMessage("time7 wrong formate")
            return False
    MainWin.statusbar.showMessage("read1!")
    PVname['Denergy']=MainWin.edt_drv_energy.text()
    PVname['Dgap']=MainWin.edt_drv_gap.text()
    PVname['Read']=MainWin.edt_ion.text()
    MainWin.btn_check.setEnabled(False)
    MainWin.statusbar.showMessage("Connecting to epics...")
    try:
        for nameKey in PVname:
            conn=PV(PVname[nameKey]).connect()
            print(conn)
            if conn!=True:
                MainWin.statusbar.showMessage("Epics PV %s wrong or unconnected!" % PVname[nameKey])
                MainWin.btn_check.setEnabled(True)
                return False
            time.sleep(0.1)
    except :
        MainWin.statusbar.showMessage("Epics PV wrong or unconnected!")
        MainWin.btn_check.setEnabled(True)
        return False
    MainWin.statusbar.showMessage("Conneced to Epics PV!")
    MainWin.btn_check.setEnabled(True)
    for i in range(0,7):
        if step[i]==0:
            MainWin.statusbar.showMessage("step%s wrong format" % str(i+1))
            return False
        else:
            n[i]=round((energy[i+1]-energy[i])/step[i])
            energy[i+1]=energy[i]+n[i]*step[i]
            gapTable[i]=gapcal(((energy[i]+energy[i+1])/2+Gstatus['edge']))
#==============================================================================
#             print(i)
#==============================================================================
#==============================================================================
#         print(energy[i+1])
#==============================================================================
    MainWin.statusbar.showMessage("calc!")
    MainWin.edt_energy2.setText("%.2f" % energy[1])
    MainWin.edt_energy3.setText("%.2f" % energy[2])
    MainWin.edt_energy4.setText("%.2f" % energy[3])
    MainWin.edt_energy5.setText("%.2f" % energy[4])
    MainWin.edt_energy6.setText("%.2f" % energy[5])
    MainWin.edt_energy7.setText("%.2f" % energy[6])
    MainWin.edt_energy8.setText("%.2f" % energy[7])
    
    MainWin.lbl_Gap1.setText("%.2f" % gapTable[0])
    MainWin.lbl_Gap2.setText("%.2f" % gapTable[1])
    MainWin.lbl_Gap3.setText("%.2f" % gapTable[2])
    MainWin.lbl_Gap4.setText("%.2f" % gapTable[3])
    MainWin.lbl_Gap5.setText("%.2f" % gapTable[4])
    MainWin.lbl_Gap6.setText("%.2f" % gapTable[5])
    MainWin.lbl_Gap7.setText("%.2f" % gapTable[6])
    
    MainWin.btn_start.setEnabled(True)
    Gstatus['STOP']=False
    MainWin.statusbar.showMessage("Check done!"+ str(n)+"points!")
def abort():
    Gstatus['STOP']=True
    Myenable(True)
    MainWin.prgBar.setValue(0)
def getDirectoryPath(self):
    direc=QFileDialog.getExistingDirectory()
    MainWin.edt_path.setText(direc)
    
    
def edgeValue():
    MainWin.edt_edge.setText(str(MainWin.cmb_edge.currentData()))
def gapcal(en):
    if 5000<en and en<=8000:
       return ((en+2652.6)/973.94137)
    if 8000<en and en <=11000:
       return ((en+4444.5906)/1498*0.921)
    if 11000<en and en<=14000:
        return ((en+6194.682)/2095*0.921)
    if 14000<en and en<=25000:
        return ((en+7615.8313)/1848*0.641)
    if en<5000 or en>25000:
        MainWin.statusbar.showMessage("Energy Out of range!")
        return False
#==============================================================================
#     if { 5<$energy && $energy<=8.0} {
#         return [expr round(10000*($energy+2.6526)/0.97394137)/10000.0]
#         }
#         if { 8.0<$energy && $energy<=11} {
#         return [expr round(10000*($energy+4.4445906)/1.498*0.921)/10000.0]
#         }
#         if { 11<$energy && $energy<=14} {
#         return [expr round(10000*($energy+6.194682)/2.095*0.921)/10000.0]
#         }
#         if { 14<$energy && $energy<=25} {
#         return [expr round(10000*($energy+7.6158313)/1.848*0.641)/10000.0]
#         }
#         if { $energy < 5 || $energy > 25} {
#         log_error "Out of range!"
#         }
#==============================================================================
def Myenable(isenable):
    if isenable==False:
        MainWin.btn_start.setEnabled(isenable)
    MainWin.btn_check.setEnabled(isenable)
    MainWin.cmb_edge.setEnabled(isenable)
    MainWin.edt_drv_energy.setEnabled(isenable)
    MainWin.edt_drv_gap.setEnabled(isenable)
    MainWin.edt_edge.setEnabled(isenable)
    MainWin.edt_energy1.setEnabled(isenable)
    MainWin.edt_energy2.setEnabled(isenable)
    MainWin.edt_energy3.setEnabled(isenable)
    MainWin.edt_energy4.setEnabled(isenable)
    MainWin.edt_energy5.setEnabled(isenable)
    MainWin.edt_energy6.setEnabled(isenable)
    MainWin.edt_energy7.setEnabled(isenable)
    MainWin.edt_energy8.setEnabled(isenable)
    MainWin.edt_ion.setEnabled(isenable)
    MainWin.edt_step1.setEnabled(isenable)
    MainWin.edt_step2.setEnabled(isenable)
    MainWin.edt_step3.setEnabled(isenable)
    MainWin.edt_step4.setEnabled(isenable)
    MainWin.edt_step5.setEnabled(isenable)
    MainWin.edt_step6.setEnabled(isenable)
    MainWin.edt_step7.setEnabled(isenable)
    MainWin.edt_time1.setEnabled(isenable)
    MainWin.edt_time2.setEnabled(isenable)
    MainWin.edt_time3.setEnabled(isenable)
    MainWin.edt_time4.setEnabled(isenable)
    MainWin.edt_time5.setEnabled(isenable)
    MainWin.edt_time6.setEnabled(isenable)
    MainWin.edt_time7.setEnabled(isenable)

def scan_thread():
    pvDenergy=PV(PVname['Denergy'])
    pvDgap=PV(PVname['Dgap'])
    pvRead=PV(PVname['Read'])
    pvDgapCMD=PV(PVname['DgapCMD'])
    
    direc=MainWin.edt_path.text()
    print (direc)
    save_time_D=time.strftime('/%Y%m%d')
    save_time_T=time.strftime('/%H%M%S')
    if not os.path.isdir(direc+save_time_D):
        os.makedirs(direc+save_time_D)
    full_path=direc+save_time_D+save_time_T+'.csv'
    print(full_path)
    fileSave=open(full_path, 'a',newline='')
    writer = csv.writer(fileSave)
    writer.writerow(['Time',PVname['Dgap'],PVname['Denergy'],PVname['Read']])
#==============================================================================
#     fileSave.close()
#==============================================================================
    
    totalP=sum(n.values())
    curP=1
    for st in range(0,7):
        meanenergy=Gstatus['edge']+(energy[st]+energy[st+1])/2
        Gstatus['gap']=gapcal(meanenergy)
        if Gstatus['gap']==False:
            return False
        print("gap %f" % Gstatus['gap'])
        print("Dgap%d" % pvDgap.put(Gstatus['gap']))
        time.sleep(0.5)
        print("sleep")
        print("DgapCMD%d" % pvDgapCMD.put(1))
        time.sleep(3)
        print("DgapCMD%d" % pvDgapCMD.put(0))
        for point in range(0,n[st]):
            if Gstatus['STOP']==True:
                fileSave.close()
                MainWin.statusbar.showMessage("Abort!")
                return
            curenergy=(Gstatus['edge']+energy[st]+point*step[st])/1000
            print("set current energy %f kev" % curenergy)
            print(pvDenergy.put(curenergy))
            readList=[]
            for geti in range(0,round(timeTable[st]/0.1)):
                readList.append(pvRead.get())
                time.sleep(0.1)
            print(readList)
            ReadSave='%.4f' % (sum(readList)/round(timeTable[st]/0.1))
            print(ReadSave)
            writer.writerow([time.strftime('%H:%M:%S'),pvDgap.get(),pvDenergy.get(),pvRead.get()])
#==============================================================================
#             time.sleep(timeTable[st]+0.1)
#==============================================================================
            MainWin.prgBar.setValue(curP/totalP*100)
            curP=curP+1
    fileSave.close()
    Myenable(True)
            
            
#==============================================================================
#             MainWin.lbl_energy_rb.setText(caget(PVname['Denergy'],as_string=True))
#             MainWin.lbl_gap_rb.setText(caget(PVname['Dgap'],as_string=True))
#             MainWin.lbl_ion_rb.setText(caget(PVname['Read'],as_string=True))
#==============================================================================
  
    
def scan():
    err=inputtool()
    if err==False:
        return False
    
    Gstatus['STOP']=False
    Myenable(False)
    _thread.start_new_thread(scan_thread,())
      
#==============================================================================
#==============================================================================
#         step1
#==============================================================================


if __name__ == '__main__':
    app = QApplication(sys.argv)    
    qWin=QMainWindow()
    MainWin=Ui_MainWindow()
    MainWin.setupUi(qWin)
    energy={}
    step={}
    gapTable={}
    n={}
    timeTable={}
    edgeTable={'si':12665,'fe':12666} 
    Gstatus={'STOP':False,'edge':0,'gap':0}
    PVname={'Denergy':'','Dgap':'','DgapCMD':'SR-ID:H17IVU27:CmdStart_Gap','Read':''}
    for edgeKey in edgeTable:
        MainWin.cmb_edge.addItem(edgeKey,edgeTable[edgeKey])
#==============================================================================
#     inputtool()
#==============================================================================
    MainWin.edt_edge.setText(str(MainWin.cmb_edge.currentData()))
    MainWin.cmb_edge.currentIndexChanged.connect(edgeValue)
    MainWin.btn_check.clicked.connect(inputtool)
    MainWin.btn_abort.clicked.connect(abort)
    MainWin.btn_start.clicked.connect(scan)
    MainWin.btn_path.clicked.connect(getDirectoryPath)
    
    qWin.show()
    sys.exit( app.exec_() )
    
 
#==============================================================================
#     MainWin.btn_start.clicked.connect(scan)
#==============================================================================
#==============================================================================
#     MainWin.edt_wait1.textChanged.connect(datachange())
#==============================================================================
   
     
     
     
     
     
    
     
    
    
