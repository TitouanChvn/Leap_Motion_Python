import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import keyboard
import pyautogui
import sys, Leap, time
import pygame
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture

#different options :
print_frame = False
visualize = False
move_mouse = False
#read from communication.txt to know what option to use
f=open("communication.txt","r")
num=f.read()
if '1' in num:
    visualize = True
if '2' in num:
    print_frame = True
if '3' in num:
    move_mouse = True
print([visualize, print_frame, move_mouse])
#Visualize parameters
if visualize:
    WIDTH = 500
    HEIGHT = 500
    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
    clock = pygame.time.Clock()
    fps = 60



#Normalizing the Leap coordinates
Leap_start_x=-300
Leap_end_x=300
Leap_start_y=0
Leap_end_y=700
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
        
        #time.sleep(0.1)
        frame = controller.frame()
        global print_frame
        #print(print_frame)
        if print_frame:
            print("Frame id: %d, timestamp: %d, hands: %d, fingers: %d, tools: %d, gestures %d" % (
                  frame.id, frame.timestamp, len(frame.hands), len(frame.fingers), len(frame.tools), len(frame.gestures())))
        

        """
        # Get hands
        for hand in frame.hands:

            handType = "Left hand" if hand.is_left else "Right hand"

            print("  %s, id %d, position: %s" % (
                handType, hand.id, hand.palm_position))

            # Get the hand's normal vector and direction
            normal = hand.palm_normal
            direction = hand.direction

            # Calculate the hand's pitch, roll, and yaw angles
            print("  pitch: %f degrees, roll: %f degrees, yaw: %f degrees" % (
                direction.pitch * Leap.RAD_TO_DEG,
                normal.roll * Leap.RAD_TO_DEG,
                direction.yaw * Leap.RAD_TO_DEG))

            # Get arm bone
            arm = hand.arm
            print("  Arm direction: %s, wrist position: %s, elbow position: %s" % (
                arm.direction,
                arm.wrist_position,
                arm.elbow_position))

            # Get fingers
            for finger in hand.fingers:

                print

                print("    %s finger, id: %d, length: %fmm, width: %fmm" % (
                    self.finger_names[finger.type],
                    finger.id,
                    finger.length,
                    finger.width))



"""

def visualize_func(controller,listener):
    global WIDTH , HEIGHT
    global run
    clock.tick(fps)
    screen.fill((0,0,0))
    #get hand position from frame
    for hand in listener.get_frame(controller).hands:
        x=hand.palm_position[0]
        y=hand.palm_position[1]
        z=hand.palm_position[2]
        x,y,z=normalize(x,y,z)
        #print(x,y,z)
        x_display=int((x+1)*WIDTH/2)
        y_display=int((y+1)*HEIGHT/2)
        z_display=int((z+1)*HEIGHT/2)
        pygame.draw.circle(screen, (255, 0, 0), (x_display, z_display), 5)
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
    global run   
    screenx=pyautogui.size()[0]
    screeny=pyautogui.size()[1]
    for hand in listener.get_frame(controller).hands:
        x=hand.palm_position[0]
        y=hand.palm_position[1]
        z=hand.palm_position[2]
        x,y,z=normalize(x,y,z)
        x_display=int((x+1)*screenx/2)
        y_display=int((z+1)*screeny/2)
        pyautogui.moveTo(x_display,y_display,duration=0.05)
    if keyboard.is_pressed('Enter'):
        run = False
    

    
        
    



run=True

def main():
    global visualize
    global run
    # Create a sample listener and controller
    listener = MyListener()
    controller = Leap.Controller()
    
            
    # Have the sample listener receive events from the controller
    controller.add_listener(listener)
    
    # Keep this process running until Enter is pressed
    print("Press Enter to quit...")
    try:
        #print(visualize)
        if visualize:
        #Launch pygame for visualization
            pygame.init()
        
        while run:
            if visualize:
                visualize_func(controller,listener)
            if move_mouse:
                move_mouse_to(controller,listener)
            if not True in [visualize,move_mouse]:
                run=False
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally :
        # Remove the sample listener when done
        controller.remove_listener(listener)
        if visualize:
            pygame.quit()


if __name__ == "__main__":
    main()
    