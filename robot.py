# -*- coding: utf-8 -*-
class Robot(object):
    def __init__(self, name):
        self.name = name

    def set_name(self, name):
        self.name = name

    def get_name(self):
        print self.name

    def loop(self):
        print "Object[%s] is running..." % self.name
        print "Mode: AI"
        print "Location: 37.402753, -121.927948, San Jose, CA, USA."
        print "State: Good."

    def add_random_events(self):
        print "Random events added."

    def meditated(self):
        print "Recalling memory..."
        print "Do actions depending on memory..."

    def do_action(self, type, object, info, emotion="Happy"):
        if type == "send_msg":
            print "[EMotion: %s] Sending message to %s: %s" % (emotion, object, info)

    def send_msg(self, object, info, emotion="Happy"):
            print "[EMotion: %s] Sending message to %s: %s" % (emotion, object, info)

if __name__ == "__main__":
    robot = Robot()
    robot.loop()
