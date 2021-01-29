#!/usr/bin/env python

import rospy
from first_pkg.my_lib import say_it_works
from first_pkg.my_lib import add

if __name__ == '__main__':
    rospy.init_node('test_node')
    say_it_works()

print('Testing add(10,3) gives us: ', add(10, 3))
