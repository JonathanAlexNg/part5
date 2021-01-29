
#!/usr/bin/env python

import rospy
from first_pkg.my_lib import add    # Imported module from pkg 1

gain = rospy.get_param('/gain')      # Get param value


# Service 1

def service_1():

    x = int(input('Input value of x: '))
    y = int(input('Input value of y: '))

    calc = add(x, y)
    ans = gain*calc
    
    print('Value of param (gain) is: ', gain)
    print('\nANS is: {} x {} = {}\n'.format(gain, calc, ans))

    return ans


# Service 2

from std_msgs.msg import String

def talker():
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(100)                               # 100hz
    while not rospy.is_shutdown():
        hello_str = "hello world %s" % rospy.get_time()
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()


# Start of program

while True:

    choice = input('Which service to call? Enter 1 or 2: ')

    if choice == '1':
        service_1()
    elif choice == '2':
        try:
            talker()
        except rospy.ROSInterruptException:
            pass
    else:
        break
