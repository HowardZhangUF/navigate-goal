import rospy 
from std_msg.msg import String

def talker ():
	pub = ros.Publisher(“chatter”,String, queue_size= 10) 
    # create a ros pub object. (topic name,msg type(string is define in std_msg, not in python),buffer for sub to wait(number of msg for buffer to sotre is 10))
	rospy.init_node(‘talker’, anonmous=True)
    # init_node (name of node,auot create a ID for talker to figure out which talker)
	rate=  rospy.Rate(1)  #1hz
	i = 0
	while not rospy.is_shutdown():
        #while rospy is alive
        hello_str = "hello world %s" % i
        # to add a counter %s
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        #pub is the obj we have create. use the publish( msg to be published) command 
        rate.sleep()
        #use with rospy.Rate . here will sleep for 1 sec
        i=i+1
        
if __name__ == '__main__':
    try:
        talker()
        except rospy.ROSInterruptException:
            pass

