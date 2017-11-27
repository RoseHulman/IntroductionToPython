"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Abbie Peterson.
"""
########################################################################
# Done: 1.
# On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# Done: 2.
#
#  You should have RUN the PREVIOUS module and READ its code.
#  (Do so now if you have not already done so.)
#
#  Below this comment, add ANY CODE THAT YOUR WANT, as long as:
#    1. You construct at least 2 rg.SimpleTurtle objects.
#    2. Each rg.SimpleTurtle object draws something
#         (by moving, using its rg.Pen).  ANYTHING is fine!
#    3. Each rg.SimpleTurtle moves inside a LOOP.
#
#  Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#  If you make syntax (notational) errors, no worries -- get help
#  fixing them at either this session OR at the NEXT session.
#
#  Don't forget to COMMIT your work by using  VCS ~ Commit and Push.
########################################################################
import rosegraphics as rg

window = rg.TurtleWindow()

Jake = rg.SimpleTurtle('turtle')
Jake.pen = rg.Pen('blue', 2)
Jake.speed = 10

AJ = rg.SimpleTurtle('turtle')
AJ.pen = rg.Pen('Silver', 2)
AJ.speed = 10

length = 10

for k in range(8):
    Jake.draw_circle(80)
    Jake.pen_up()
    Jake.forward(50)
    Jake.right(45)
    Jake.pen_down()
    length = length + (-2) ^ k
    AJ.backward(30)
    AJ.draw_regular_polygon(6, 90)
    AJ.pen_up()
    AJ.forward(20)
    AJ.right(45)
    AJ.pen_down()
window.close_on_mouse_click()
