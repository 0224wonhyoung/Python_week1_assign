# 2020.09.13 이원형

# 20200224 이원형
# 3주차퀴즈

from bangtal import *

#첫번째방 오브젝트
scene1 = Scene('룸1', 'Images/배경-1.png')

door1 = Object('Images/문-오른쪽-닫힘.png')
door1.locate(scene1, 800, 270)
door1.show()
door1.closed = True

door5 = Object('Images/문-왼쪽-열림.png')
door5.locate(scene1, 200, 280)

hint1 = Object('Images/hint1.png')
hint1.locate(scene1, 340, 500)
hint1.show()

bookshelf = Object('Images/책장.png')
bookshelf.locate(scene1, 310, 250)
bookshelf.show()
bookshelf.pos = 2

keypad = Object('Images/키패드.png')
keypad.setScale(3)
keypad.locate(scene1, 750, 410)
keypad.show()



#두번쨰방 오브젝트
scene2 = Scene('룸2', 'Images/배경-2.png')

door2 = Object('Images/문-왼쪽-열림.png')
door2.locate(scene2, 320, 270)
door2.show()

door3 = Object('Images/문-오른쪽-닫힘.png')
door3.locate(scene2, 910, 270)
door3.show()
door3.closed = True 

hint2 = Object('Images/힌트2.jpg')
hint2.setScale(0.8)
hint2.locate(scene2, 510, 400)
hint2.show()

camera = Object('Images/카메라.png')
camera.setScale(0.05)
camera.locate(scene2, 600, 310)
camera.show()

seat1 = Object('Images/자리.png')
seat1.locate(scene2, 500, 120)
seat1.show()
seat1.chessNum = 0

seat2 = Object('Images/자리.png')
seat2.locate(scene2, 600, 120)
seat2.show()
seat2.chessNum = 0

seat3 = Object('Images/자리.png')
seat3.locate(scene2, 700, 120)
seat3.show()
seat3.chessNum = 0

chess1 = Object('Images/체스1.png')
chess1.locate(scene2, 220, 170)
chess1.show()

chess2 = Object('Images/체스2.png')
chess2.locate(scene2, 220, 120)
chess2.show()

chess3 = Object('Images/체스3.png')
chess3.locate(scene2, 170, 170)
chess3.show()



#세번째방 오브젝트
scene3 = Scene('룸3', 'Images/배경-2.png')

door4 = Object('Images/문-왼쪽-열림.png')
door4.locate(scene3, 320, 270)
door4.show()

machine = Object('Images/기계.png')
machine.locate(scene3, 680, 180)
machine.show()

switch1 = Object('Images/스위치.png')
switch1.locate(scene3, 730, 260)
switch1.show()
switch1.on = False

switch2 = Object('Images/스위치.png')
switch2.locate(scene3, 785, 253)
switch2.show()
switch2.on = False

switch3 = Object('Images/스위치.png')
switch3.locate(scene3, 840, 246)
switch3.show()
switch3.on = False

switch4 = Object('Images/스위치.png')
switch4.locate(scene3, 895, 239)
switch4.show()
switch4.on = False

switch5 = Object('Images/스위치.png')
switch5.locate(scene3, 950, 232)
switch5.show()
switch5.on = False

switch6 = Object('Images/스위치.png')
switch6.locate(scene3, 1005, 225)
switch6.show()
switch6.on = False

light1 = Object('Images/전구-꺼짐.png')
light1.locate(scene3, 730, 310)
light1.show()

light2 = Object('Images/전구-꺼짐.png')
light2.locate(scene3, 785, 303)
light2.show()

light3 = Object('Images/전구-꺼짐.png')
light3.locate(scene3, 840, 296)
light3.show()

light4 = Object('Images/전구-꺼짐.png')
light4.locate(scene3, 895, 289)
light4.show()

light5 = Object('Images/전구-꺼짐.png')
light5.locate(scene3, 950, 282)
light5.show()

light6 = Object('Images/전구-꺼짐.png')
light6.locate(scene3, 1005, 275)
light6.show()



#첫번째방
def bookshelf_onMouseAction(x, y, action):
    if action == MouseAction.DRAG_LEFT and bookshelf.pos > 0:
        bookshelf.pos -=1
        bookshelf.locate(scene1, 170 + 70*bookshelf.pos, 224+ 13*bookshelf.pos)
    elif action == MouseAction.DRAG_RIGHT and bookshelf.pos < 2:
        bookshelf.pos +=1
        bookshelf.locate(scene1, 170 + 70*bookshelf.pos, 224+ 13*bookshelf.pos)
bookshelf.onMouseAction = bookshelf_onMouseAction

def keypad_onMouseAction(x, y, action):
    showKeypad('recover',door1) 
keypad.onMouseAction = keypad_onMouseAction

def door1_onKeypad():
    door1.closed = False
    door1.setImage('Images/문-오른쪽-열림.png')
    showMessage('문이 열렸다!')
door1.onKeypad = door1_onKeypad

def door_onMouseAction(x, y, action):  
    if door1.closed :
        showMessage('잠겨있어')
    else:
        scene2.enter()
door1.onMouseAction = door_onMouseAction

def door5_onMouseAction(x, y, action): 
    endGame()    
door5.onMouseAction = door5_onMouseAction


#두번쨰방
def door2_onMouseAction(x, y, action):  
    scene1.enter()
door2.onMouseAction = door2_onMouseAction

def door3_onMouseAction(x, y, action):  
    if door3.closed :
        showMessage('잠겨있어')
    else:
        scene3.enter()
door3.onMouseAction = door3_onMouseAction


def chess1_onMouseAction(x, y, action):
    if seat1.chessNum == 1:
        seat1.chessNum = 0
    elif seat2.chessNum == 1:
        seat2.chessNum = 0
    elif seat3.chessNum == 1:
        seat3.chessNum = 0
    chess1.pick()
chess1.onMouseAction = chess1_onMouseAction

def chess2_onMouseAction(x, y, action):
    if seat1.chessNum == 2:
        seat1.chessNum = 0
    elif seat2.chessNum == 2:
        seat2.chessNum = 0
    elif seat3.chessNum == 2:
        seat3.chessNum = 0
    chess2.pick()
chess2.onMouseAction = chess2_onMouseAction

def chess3_onMouseAction(x, y, action):
    if seat1.chessNum == 3:
        seat1.chessNum = 0
    elif seat2.chessNum == 3:
        seat2.chessNum = 0
    elif seat3.chessNum == 3:
        seat3.chessNum = 0
    chess3.pick()
chess3.onMouseAction = chess3_onMouseAction

def check_inHand():
    if(chess1.inHand()):
        return chess1
    elif(chess2.inHand()):
        return chess2
    elif(chess3.inHand()):
        return chess3
    else:
        return 0

def check_Num():
    if(chess1.inHand()):
        return 1
    elif(chess2.inHand()):
        return 2
    elif(chess3.inHand()):
        return 3
    else:
        return 0

def check_clear2():
    if (seat1.chessNum == 2) and (seat2.chessNum == 1) and (seat3.chessNum == 3):
        door3.setImage('Images/문-오른쪽-열림.png')
        door3.closed = False
        showMessage('문이열렸다!')

def seat1_onMouseAction(x, y, action):
    if not seat1.chessNum :
        chess = check_inHand()
        num = check_Num()
        if chess :
            chess.drop()
            chess.locate(scene2, 505, 130)
            seat1.chessNum = num
            check_clear2()
seat1.onMouseAction = seat1_onMouseAction

def seat2_onMouseAction(x, y, action):
    if not seat2.chessNum :
        chess = check_inHand()
        num = check_Num()
        if chess :
            chess.drop()
            chess.locate(scene2, 605, 130)
            seat2.chessNum = num
            check_clear2()
seat2.onMouseAction = seat2_onMouseAction

def seat3_onMouseAction(x, y, action):
    if not seat3.chessNum :
        chess = check_inHand()
        num = check_Num()
        if chess :
            chess.drop()
            chess.locate(scene2, 705, 130)
            seat3.chessNum = num
            check_clear2()
seat3.onMouseAction = seat3_onMouseAction

#세번째방
def door4_onMouseAction(x, y, action):  
    scene2.enter()
door4.onMouseAction = door4_onMouseAction

def check_clear():
    if switch1.on and (not switch2.on) and switch3.on and switch4.on and switch5.on and (not switch6.on) :
        door5.show()
        showMessage("첫번째방에서 소리가난다!")

def switch1_onMouseAction(x, y, action):
    if switch1.on:
        light1.setImage('Images/전구-꺼짐.png')
    else :
        light1.setImage('Images/전구-켜짐.png')
    switch1.on = not switch1.on
    check_clear()
switch1.onMouseAction = switch1_onMouseAction

def switch2_onMouseAction(x, y, action):
    if switch2.on:
        light2.setImage('Images/전구-꺼짐.png')
    else :
        light2.setImage('Images/전구-켜짐.png')
    switch2.on = not switch2.on
    check_clear()
switch2.onMouseAction = switch2_onMouseAction

def switch3_onMouseAction(x, y, action):
    if switch3.on:
        light3.setImage('Images/전구-꺼짐.png')
    else :
        light3.setImage('Images/전구-켜짐.png')
    switch3.on = not switch3.on
    check_clear()
switch3.onMouseAction = switch3_onMouseAction

def switch4_onMouseAction(x, y, action):
    if switch4.on:
        light4.setImage('Images/전구-꺼짐.png')
    else :
        light4.setImage('Images/전구-켜짐.png')
    switch4.on = not switch4.on
    check_clear()
switch4.onMouseAction = switch4_onMouseAction

def switch5_onMouseAction(x, y, action):
    if switch5.on:
        light5.setImage('Images/전구-꺼짐.png')
    else :
        light5.setImage('Images/전구-켜짐.png')
    switch5.on = not switch5.on
    check_clear()
switch5.onMouseAction = switch5_onMouseAction

def switch6_onMouseAction(x, y, action):
    if switch6.on:
        light6.setImage('Images/전구-꺼짐.png')
    else :
        light6.setImage('Images/전구-켜짐.png')
    switch6.on = not switch6.on
    check_clear()
switch6.onMouseAction = switch6_onMouseAction


startGame(scene1)


