'''
Example: Given a time, calculate the angle between the hour and minute hands.

Approach: Start with an example like 3:27. We can draw a picture of a clock by selecting
where the 3 hour hand is and where the 27 minute hand is.

'''
import sys

if len(sys.argv) < 3: sys.exit("Missing parameters - hours and minutes, e.g. clock_angles_between_hands.py 12 30")

hours = int(sys.argv[1])
minutes = int(sys.argv[2])

minute_angle = (360. / 60) * minutes
hour_angle = (360. / 12) * (hours % 12) + minute_angle * (1. / 12)

if hour_angle > minute_angle:
  angle_between = hour_angle - minute_angle
else:
  angle_between = minute_angle - hour_angle

print "The angle between the hands at %s:%s is %s degrees" % (hours,minutes,angle_between)