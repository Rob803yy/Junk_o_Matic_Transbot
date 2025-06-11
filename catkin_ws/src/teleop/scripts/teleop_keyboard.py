#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
import sys, select, termios, tty

msg = """
Reading from the keyboard and Publishing to Twist!
---------------------------
Use WASD keys to control the robot
CTRL-C to quit
"""
moveBindings = {
    'w':(1,0),
    's':(-1,0),
    'a':(0,1),
    'd':(0,-1),
}

def getKey():
    tty.setraw(sys.stdin.fileno())
    rlist, _, _ = select.select([sys.stdin], [], [], 0.1)
    if rlist:
        key = sys.stdin.read(1)
    else:
        key = ''
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key

if __name__ == '__main__':
    settings = termios.tcgetattr(sys.stdin)
    rospy.init_node('teleop_keyboard')
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)
    speed = rospy.get_param("~speed", 0.2)
    turn = rospy.get_param("~turn", 1.0)
    try:
        print(msg)
        while not rospy.is_shutdown():
            key = getKey()
            if key in moveBindings:
                x, th = moveBindings[key]
            elif key == '\x03':
                break
            else:
                x = 0
                th = 0
            twist = Twist()
            twist.linear.x = x * speed
            twist.angular.z = th * turn
            pub.publish(twist)
    except rospy.ROSInterruptException:
        pass
    finally:
        twist = Twist()
        pub.publish(twist)
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
