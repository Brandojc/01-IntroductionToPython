"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and James Brandon.
"""
###############################################################################
# Done: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
###############################################################################

###############################################################################
# Done: 2.
#   You should have RUN the  m4e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
###############################################################################
import rosegraphics as rg

window = rg.TurtleWindow()

jon = rg.SimpleTurtle('turtle')
jon.pen = rg.Pen('red',15)
jon.speed = 15

lily = rg.SimpleTurtle()
lily.pen = rg.Pen('blue',10)
lily.speed = 20
size = 350
size2 = 315
for n in range(20):

    jon.draw_square(size)

    jon.pen_up()
    jon.right(90)
    jon.forward(10)
    jon.pen_down()
    size = size - 20

    lily.draw_square(size2)
    lily.pen_up()
    lily.right(90)
    lily.forward(10)
    lily.pen_down()
    size2 = size2 - 20

window.close_on_mouse_click()
