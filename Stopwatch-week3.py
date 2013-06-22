# template for "Stopwatch: The Game"
import simpleguitk as simplegui
import simpleplot

# define global variables
tick = 0
tries = 0
win = 0
stopped = True

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

# create frame
frame = simplegui.create_frame("Stopwatch: The Game", 200, 120)

# register event handlers
timer = simplegui.create_timer(100, update)
start = frame.add_button("Start", start, 50)
stop = frame.add_button("Stop", stop, 50)
reset = frame.add_button("Reset", reset, 50)
frame.set_draw_handler(draw)

# start timer and frame
frame.start()

# remember to review the grading rubric
#print "Some tests:"
#print "Outcome  |  Expected"
#print "  "+format(0)+" = 0:00.0"
#print "  "+format(11)+" = 0:01.1"
#print "  "+format(321)+" = 0:32.1"
#print "  "+format(613)+" = 1:01.3"
