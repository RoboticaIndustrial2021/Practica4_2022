from robodk.robolink import *
from robodk.robomath import *
from time import sleep
RDK= Robolink() 
RDK.RunProgram('P2')
robot = RDK.Item('',ITEM_TYPE_ROBOT) 


#Declarar los grippers
ToolGO=RDK.Item('Open')
ToolGC=RDK.Item('Close')


ToolGO.setVisible(True)
ToolGC.setVisible(False)
robot.setTool(ToolGO)

#Definir Frame
cajas=RDK.Item("frcaja")
frame1= RDK.Item("fr1",ITEM_TYPE_FRAME) 
robot.setPoseFrame(cajas)

#Definir Target
Pick_Place=RDK.Item("box").Pose()*rotx(pi)
aproxx= Pick_Place*transl(0,0,-100)


#Movimiento

robot.MoveJ(aproxx)
robot.MoveJ(Pick_Place)
ToolGO.setVisible(False)
ToolGC.setVisible(True)
robot.setTool(ToolGC)
ToolGC.AttachClosest()
sleep(1)

robot.MoveJ(aproxx)
robot.setPoseFrame(frame1)
robot.MoveJ(aproxx)
robot.MoveJ(Pick_Place)
ToolGO.setVisible(True)
ToolGC.setVisible(False)
ToolGC.DetachAll(frame1)
robot.setTool(ToolGO)
sleep(1)

robot.MoveJ(aproxx)
robot.setPoseFrame(cajas)
robot.MoveJ(aproxx)
