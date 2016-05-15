'''
The MIT License (MIT)
Copyright (c) 2016 Antal Janos Monori.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''

###########
# Imports #
###########

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import simpleplot

#############
# Variables #
#############

# define global variables
tick = 0
tries = 0
win = 0
stopped = True

####################
# Helper functions #
####################

# define helper function format that converts integer
# counting tenths of seconds into formatted string A:BC.D
def format(t):
    min_tick = t / 600
    sec_tick = (min_tick - int(min_tick)) * 60
    mil_tick = (sec_tick - int(sec_tick)) * 10
    A = str(int(min_tick))
    BC = (str(int(sec_tick)) if sec_tick >= 10 else str(0)+str(int(sec_tick)))
    D = str(int(mil_tick))
    outcome = A+":"+BC+"."+D
    return outcome

# the game part of the project
def reflex():
    global tries, win
    if (format(tick)[5:] == "0"):
        win += 1
        tries += 1
    else: tries += 1

############
# Handlers #
############

# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global stopped
    timer.start()
    stopped = False

def stop():
    global stopped
    timer.stop()
    if (stopped == False): reflex()
    stopped = True

def reset():
    global tick, tries, win, stopped
    timer.stop()
    stopped = True
    tick = 0
    tries = 0
    win = 0

# define event handler for timer
def update():
    global tick
    tick += 1
    print tick

# draw handler
def draw(canvas):
    global tick, tries, win
    timer = format(tick)
    score = str(win)+" / "+str(tries)
    canvas.draw_text(timer,[70, 70], 18, "White")
    canvas.draw_text(score, [145, 15], 14, "Green")

######
# UI #
######

# create frame
frame = simplegui.create_frame("Stopwatch: The Game", 200, 120)

# register event handlers
timer = simplegui.create_timer(100, update)
start = frame.add_button("Start", start, 50)
stop = frame.add_button("Stop", stop, 50)
reset = frame.add_button("Reset", reset, 50)
frame.set_draw_handler(draw)

########
# Main #
########

# start timer and frame
frame.start()

#########
# Tests #
#########

#print "Some tests:"
#print "Outcome  |  Expected"
#print "  "+format(0)+" = 0:00.0"
#print "  "+format(11)+" = 0:01.1"
#print "  "+format(321)+" = 0:32.1"
#print "  "+format(613)+" = 1:01.3"
