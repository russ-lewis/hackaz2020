from time import sleep
import curses, curses.panel

def make_panel(h,l, y,x, str):
   win = curses.newwin(h,l, y,x)
   win.erase()
   win.box()
   win.addstr(2, 2, str)

   panel = curses.panel.new_panel(win)
   return win, panel

def test(stdscr):
   curses.curs_set(0)
   stdscr.box()
   stdscr.addstr(2, 2, "panels everywhere")
   win1, panel1 = make_panel(10,12, 5,5, "Panel 1")
   win2, panel2 = make_panel(10,12, 8,8, "Panel 2")
   curses.panel.update_panels(); stdscr.refresh()
   sleep(1)

   panel1.top(); curses.panel.update_panels(); stdscr.refresh()
   sleep(1)

   for i in range(20):
      panel2.move(8, 8+i)
      curses.panel.update_panels(); stdscr.refresh()
      sleep(0.1)

   sleep(1)

if __name__ == '__main__':
   curses.wrapper(test)
