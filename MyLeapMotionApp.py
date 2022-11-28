import sys, Leap, time
import pygame
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture

#Visualize parameters

WIDTH=800
HEIGHT=600
fps = 60
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


#Normalizing the Leap coordinates



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
        
        time.sleep(1)
        frame = controller.frame()
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


def main():
    # Create a sample listener and controller
    listener = MyListener()
    controller = Leap.Controller()

            
    # Have the sample listener receive events from the controller
    controller.add_listener(listener)
    
    # Keep this process running until Enter is pressed
    print("Press Enter to quit...")
    try:
        #Launch pygame for visualization
        pygame.init()
        run=True
        while run :
            clock.tick(fps)
            #get hand position from frame
            x=listener.get_frame(controller).hands[0].palm_position[0]
            y=listener.get_frame(controller).hands[0].palm_position[1]
            pygame.draw.circle(screen, (255, 0, 0), (x, y), 20)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    continue
            try :   #if pygame is launched, update the frame
                pygame.display.flip()
            except :
                pass

        #and not (sys.stdin.readline())
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally :
        # Remove the sample listener when done
        controller.remove_listener(listener)
        pygame.quit()


if __name__ == "__main__":
    main()
    