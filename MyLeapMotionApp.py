import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import keyboard
import pyautogui
import sys, Leap, time
import pygame
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture

#different options :
print_frame = False
visualize_xz = False
visualize_xy = False
move_mouse = False
move_mouse_relative = False
#read from communication.txt to know what option to use
f=open("communication.txt","r")
num=f.read()
if '1' in num:
    visualize_xz = True
if '2' in num:
    visualize_xy = True
if '3' in num:
    move_mouse = True
if '4' in num:
    move_mouse_relative = True
if '5' in num:
    print_frame = True
print([visualize_xz, visualize_xy, move_mouse,move_mouse_relative,print_frame])
#Visualize parameters
if visualize_xz :
    WIDTH = 500
    HEIGHT = 500
    screen_xz = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
    clock = pygame.time.Clock()
    fps = 60

#mouse mouvement parameters
if move_mouse or move_mouse_relative:
    pyautogui.FAILSAFE = False
    pyautogui.PAUSE = 0

#Normalizing the Leap coordinates
Leap_start_x=-300
Leap_end_x=300
Leap_start_y=120
Leap_end_y=500
Leap_start_z=-300
Leap_end_z=300
Leap_range_x=Leap_end_x-Leap_start_x
Leap_range_y=Leap_end_y-Leap_start_y
Leap_range_z=Leap_end_z-Leap_start_z
App_start_x=-1
App_end_x=1
App_start_y=0
App_end_y=1
App_start_z=-1
App_end_z=1
App_range_x=App_end_x-App_start_x
App_range_y=App_end_y-App_start_y
App_range_z=App_end_z-App_start_z

def normalize(x_Leap, y_Leap, z_Leap):
    x_App=App_start_x+(x_Leap-Leap_start_x)*App_range_x/Leap_range_x
    y_App=App_start_y+(y_Leap-Leap_start_y)*App_range_y/Leap_range_y
    z_App=App_start_z+(z_Leap-Leap_start_z)*App_range_z/Leap_range_z
    return x_App, y_App, z_App


class MyListener(Leap.Listener):
    finger_names = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']
    bone_names = ['Metacarpal', 'Proximal', 'Intermediate', 'Distal']
    state_names = ['STATE_INVALID', 'STATE_START', 'STATE_UPDATE', 'STATE_END']
    

    def on_init(self, controller):
        print("Initialized")

    def on_connect(self, controller):
        print("Connected")

        # Enable gestures
        controller.enable_gesture(Leap.Gesture.TYPE_CIRCLE);
        controller.enable_gesture(Leap.Gesture.TYPE_KEY_TAP);
        controller.enable_gesture(Leap.Gesture.TYPE_SCREEN_TAP);
        controller.enable_gesture(Leap.Gesture.TYPE_SWIPE);

        controller.config.set("Gesture.ScreenTap.MinForwardVelocity", 3.0)
        controller.config.set("Gesture.ScreenTap.HistorySeconds", .1)
        controller.config.set("Gesture.ScreenTap.MinDistance", 0.2)
        controller.config.save()

        controller.config.set("Gesture.KeyTap.MinDownVelocity", 15.0)
        controller.config.set("Gesture.KeyTap.HistorySeconds", .1)
        controller.config.set("Gesture.KeyTap.MinDistance", 0.05)
        controller.config.save()

        controller.config.set("Gesture.Swipe.MinLength", 4000.0)
        controller.config.set("Gesture.Swipe.MinVelocity", 1500)
        controller.config.save()

    def on_disconnect(self, controller):
        # Note: not dispatched when running in a debugger.
        print("Disconnected")

    def on_exit(self, controller):
        print("Exited")

    def get_frame(self, controller):
        frame = controller.frame()
        return frame
    

    def on_frame(self, controller):
        # Get the most recent frame and report some basic information
        global frame_count
        frame_count+=1
        #time.sleep(0.1)
        frame = controller.frame()
        global print_frame
        #print(print_frame)
        if print_frame:
            print("Frame id: %d, timestamp: %d, hands: %d, fingers: %d, tools: %d, gestures %d" % (
                  frame.id, frame.timestamp, len(frame.hands), len(frame.fingers), len(frame.tools), len(frame.gestures())))
        
        list_of_hand_swiped = []
        for gesture in frame.gestures():
            #if gesture.type == Leap.Gesture.TYPE_SCREEN_TAP:
            #    screen_tap = ScreenTapGesture(gesture)
            #    print("Screen Tap id: %d, %s, position: %s, direction: %s" % (
            #          gesture.id, self.state_names[gesture.state],
            #          screen_tap.position, screen_tap.direction))
            #    #pyautogui.click()
            #    #print("Click")
            if gesture.type == Leap.Gesture.TYPE_KEY_TAP:
                key_tap = KeyTapGesture(gesture)
                print("Key Tap id: %d, %s, position: %s, direction: %s" % (
                      gesture.id, self.state_names[gesture.state],
                      key_tap.position, key_tap.direction))
                if move_mouse or move_mouse_relative:
                     pyautogui.click()
                #print("Click")
            if gesture.type == Leap.Gesture.TYPE_SWIPE :
                swipe = SwipeGesture(gesture)
                hand_swiped = swipe.pointable.hand.id
                if hand_swiped not in list_of_hand_swiped:
                    list_of_hand_swiped.append((hand_swiped, swipe.direction))
                #pyautogui.click()
                #print("Click")
        for hand in list_of_hand_swiped:
            #print("Hand swiped: %d" % hand[0])
            #print("Swipe direction: %s" % hand[1])
            pass
            


def visualize_xz_func(controller,listener):
    global WIDTH , HEIGHT
    global run
    clock.tick(fps)
    screen_xz.fill((0,0,0))
    #get hand position from frame
    for hand in listener.get_frame(controller).hands:
        x=hand.palm_position[0]
        y=hand.palm_position[1]
        z=hand.palm_position[2]
        x,y,z=normalize(x,y,z)
        #print(x,y,z)
        x_display=int((x+1)*WIDTH/2)
        z_display=int((z+1)*HEIGHT/2)
        pygame.draw.circle(screen_xz, (255, 0, 0), (x_display, z_display), 5)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            continue
        if event.type == pygame.VIDEORESIZE:  
            WIDTH = event.w
            HEIGHT = event.h
            pygame.display.update()
    try :   #if pygame is launched, update the frame
        pygame.display.flip()
    except :
        pass


def move_mouse_to(controller,listener):  #On devrait plutot utiliser du move_relative
    #print("Move mouse to")
    global run   
    screenx=pyautogui.size()[0]
    screeny=pyautogui.size()[1]
    if not listener.get_frame(controller).hands:
        pass
    else :
        x=listener.get_frame(controller).hands[0].palm_position[0]
        y=listener.get_frame(controller).hands[0].palm_position[1]
        z=listener.get_frame(controller).hands[0].palm_position[2]
        x,y,z=normalize(x,y,z)
        x_display=int((x+1)*screenx/2)
        y_display=int((1-y)*screeny)
        pyautogui.moveTo(x_display,y_display,duration=0.05)
    if keyboard.is_pressed('Enter'):
        run = False
    

def move_mouse_relative_func(controller,listener):
    #print("move_mouse_relative_func")
    global run   
    screenx=pyautogui.size()[0]
    screeny=pyautogui.size()[1]
    if not listener.get_frame(controller).hands :
        pass
    else :
        for swipe in listener.get_frame(controller).gestures():
            if swipe.type == Leap.Gesture.TYPE_SWIPE :
                swipe = SwipeGesture(swipe)
                x=swipe.direction[0]
                y=swipe.direction[1]
                z=swipe.direction[2]
                #print(x,y,z)
                x_display=x*screenx/800
                y_display=-y*screeny/800
                pyautogui.move(x_display,y_display,duration=0.05)
    if keyboard.is_pressed('Enter'):
        run = False
        
    



run=True
frame_count=0

def main():
    global visualize_xz
    global run
    global frame_count
    # Create a sample listener and controller
    listener = MyListener()
    controller = Leap.Controller()
    
            
    # Have the sample listener receive events from the controller
    controller.add_listener(listener)
    
    # Keep this process running until Enter is pressed
    print("Press Enter to quit...")
    try:
        #print(visualize)
        if visualize_xz:
        #Launch pygame for visualization
            pygame.init()
        printed_frame_count=False
        while run:
            if frame_count%1000==0 and not printed_frame_count:
                printed_frame_count=True
                print("Frame count: %d" % frame_count)
            if frame_count%1000==1 and printed_frame_count:
                printed_frame_count=False
            if visualize_xz:
                visualize_xz_func(controller,listener)
            if move_mouse:
                move_mouse_to(controller,listener)
            if move_mouse_relative:
                move_mouse_relative_func(controller,listener)
            if not True in [visualize_xz,move_mouse,move_mouse_relative]:
                run=False
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally :
        # Remove the sample listener when done
        controller.remove_listener(listener)
        if visualize_xz:
            pygame.quit()


if __name__ == "__main__":
    main()
    