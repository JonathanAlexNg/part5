import rospy

# Testing module
def say_it_works():
    rospy.loginfo("Success! You just have imported a Python module in another package.")


# Module to use in a node in another pkg
def add(x, y):
    return x + y