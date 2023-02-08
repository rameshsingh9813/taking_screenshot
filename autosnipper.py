from tkinter import *
import pyperclip
import pyautogui as pag
import time
import os



ws = Tk()

t_n = "Autosnipper"  # title name
s_a = '300x420'  # canvas size of application
bg_c = '#F1F1F5'  # background color of application
fg_c_f = '#C8C7C7'  # foreground color of footer_w
fg_c_l = '#373737'  # foreground color of label
fg_c_e = '#9D9B9B'  # foreground color of entry
i_l = 'C:/Users/hp/Desktop/code_practise/day_17 screenshot taker  modification/modification of screenshot ' \
      'taker/icon_7.png'  # icon link

ws.minsize(300, 420)
ws.maxsize(300,420)
ws.title(t_n)
ws.geometry(s_a)
ws['bg'] = bg_c
p1 = PhotoImage(file=i_l)
ws.iconphoto(False, p1)  # setting of icon
pasted = pyperclip.paste()
h_of_sc = pag.size().height
if h_of_sc > 800:
    pasted = '345, 85, 1200, 750'
else:
    pasted='345, 85, 855, 535'


def all_in_one(loc,cordinate):
    # variable declaration
    ss_location = loc
    ss_coordinate = cordinate
    sleep_time = 0.2
    ss_t_c = (10, 50)  # screenshot taking coordinate
    p_t_c = (0, 10)  # program terminate coordinate
    os.chdir(ss_location)


    # screenshot taker function
    def take_ss(count):
        ss = pag.screenshot(region=ss_coordinate)
        ss.save(rf'screenshot{count}.png')
        print(rf'screenshot{count}.png')


    # time decider for the different action
    def time_definer_for_screenshot():
        updator = 0
        insideif = 0
        insideelif_2 = 0
        while True:
            time.sleep(sleep_time)
            x, y = pag.position()
            if x < ss_t_c[0] and y > ss_t_c[1]:
                insideif += 1
                if insideif < 2:
                    take_ss(updator)
                    updator += 1

            elif y < p_t_c[1]:
                return False

            else:
                insideif = 0
                insideelif_2 += 0


    time_definer_for_screenshot()





def two_in_one():
    x = file_path.get()
    k = im_size.get()
    k_tup = tuple(map(int, k.split(', ')))
    all_in_one(x, k_tup)
    print(x, k_tup)
    print(type(x), type(k_tup))

Label(ws,
      text="Path *",
      fg=fg_c_l,
      # bg=fg_c_l,
      font=('Times', 15),
      height=2,
      width=25,
      # relief="solid",
      bd=1,
      anchor="sw",
      justify=LEFT).pack()

file_path = Entry(ws,
                  width=33,
                  fg=fg_c_l,
                  font='Arial 11'
                  )

file_path.insert(0,'')
file_path.pack(ipadx=5, ipady=5)
print(file_path.get())

Label(ws,
      text="Size",
      fg=fg_c_l,
      # bg=fg_c_l,
      font=('Times', 15),
      height=2,
      width=25,
      # relief="solid",
      bd=1,
      anchor="sw",
      justify=LEFT).pack()

im_size = Entry(ws,
                  width=33,
                  fg=fg_c_e,
                  font='Arial 11'
                  )
im_size.insert(0, pasted)
im_size.pack(ipadx=5, ipady=5)
print(im_size.get())

Button(ws,
       text="Start",
       width=20,
       command=two_in_one
       ).pack(pady=10, padx=10, ipady=5)

Label(ws,
      text="@C2023 Developed by ramesh kr. mahato \n         rameshsingh9813@gmail.com",
      fg=fg_c_f,
      bg=bg_c,
      # font=('Times', 15),
      height=13,
      width=40,
      # relief="solid",
      bd=1,
      anchor="s",
      justify=LEFT).pack()
ws.mainloop()
