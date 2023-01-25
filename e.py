from tkinter import *
root = Tk()
clicks = 0
coins = 0
mult = 1
price = 25 * mult
dark = False
cheatused = False
cheat2used = False
cheat3used = False
cheat4used = False
cheat5used = False

root.title('GooseClicker')
root.geometry('760x490')
# root.iconbitmap('forg.ico')
root.configure(background='#eeeeff')
root.resizable(False, False)

def click():
    global clicks, coins
    clicks += 1
    coins += 1 * mult
    click_text.config(text=f"Total clicks : {clicks}")
    coin_text.config(text=f"Coins : {coins}")

spacer_text = Label(root, text="              ", font=('Comic Sans MS', 14), bg='#eeeeff', fg='#eeeeff')
spacer_text.grid(row=1, column=7)
spacer2_text = Label(root, text="              ", font=('Comic Sans MS', 14), bg='#eeeeff', fg='#eeeeff')
spacer2_text.grid(row=2, column=7)
spacer3_text = Label(root, text="  ", font=('Comic Sans MS', 14), bg='#eeeeff', fg='#eeeeff')
spacer3_text.grid(row=0, column=6)
spacer4_text = Label(root, text="              ", font=('Comic Sans MS', 14), bg='#eeeeff', fg='#eeeeff')
spacer4_text.grid(row=0, column=5)
spacer5_text = Label(root, text="              ", font=('Comic Sans MS', 14), bg='#eeeeff', fg='#eeeeff')
spacer5_text.grid(row=0, column=4)
spacer6_text = Label(root, text="              ", font=('Comic Sans MS', 14), bg='#eeeeff', fg='#eeeeff')
spacer6_text.grid(row=0, column=3)
spacer7_text = Label(root, text="                               ", font=('Comic Sans MS', 14), bg='#eeeeff', fg='#eeeeff')
spacer7_text.grid(row=5, column=0)
spacer8_text = Label(root, text="                                     ", font=('Comic Sans MS', 14), bg='#eeeeff', fg= '#eeeeff')
spacer8_text.grid(row=0, column=10)
spacer9_text = Label(root, text="                                     ", font=('Comic Sans MS', 14), bg='#eeeeff', fg= '#eeeeff')
spacer9_text.grid(row=0, column=7)
click_text = Label(root, text="Total clicks : 0", font=('Comic Sans MS', 14), bg='#eeeeff')
click_text.grid(row=0, column=0)
coin_text = LabelFrame(root, text="Coins : 0", font=('Comic Sans MS', 18), bg='#eeeeff', padx=32, pady=16,labelanchor='n')
coin_text.grid(row=4, column=4)
mult_frame = LabelFrame(root, text="Click multiplier : 1", font=('Comic Sans MS', 13), labelanchor='n', bg='#eeeeff',padx=8, pady=10)
mult_frame.grid(row=3, column=7)
main_button = Button(coin_text, text="Click",font=('Comic Sans MS', 18),bg='#8888ff',fg='white',anchor='center',command=click,activebackground='#eeeeff',highlightbackground='#eeeeff')
main_button.pack(anchor='n')
no_money_text = Label(root, text=f"Not enough money , need : {price}", font=('Comic Sans MS', 12), fg='red',bg='#eeeeff')

def mult_buy():
    global coins, mult, price
    if coins >= price:
        coins -= price
        mult += 1
        price = 25 * mult
        coin_text.config(text=f"Coins : {coins}")
        mult_frame.config(text=f"Click multiplier : {mult}")
        mult_button.config(text=f'Buy Multiplier : {price}')
    else:
        if dark is True:
            no_money_text.config(text=f"Not enough money , need : {price}", bg='#333344')
            no_money_text.grid(row=6, column=7)
        else:
            no_money_text.config(text=f"Not enough money , need : {price}", bg='#eeeeff')
            no_money_text.grid(row=6, column=7)
mult_button = Button(mult_frame, text=f'Buy Multiplier : {price}',font=('Comic Sans MS', 14),bg='#8888ff',fg='white',command=mult_buy,activebackground='#eeeeff',highlightbackground='#eeeeff')
mult_button.pack()
no_money_geese = Label(root, text="Not enough money , need : 50", font=('Comic Sans MS', 12), fg='red', bg='#eeeeff')

def geese_buy():
    global coins, geese
    if coins >= 50:
        coins -= 50
        geese += 1
        coin_text.config(text=f"Coins : {coins}")
    else:
        if dark is True:
            no_money_geese.config(text="Not enough money , need : 100", font=('Comic Sans MS', 12), fg='red',
                                  bg='#333344')
            no_money_geese.grid(row=7, column=7)
        else:
            no_money_geese.config(text="Not enough money , need : 100", font=('Comic Sans MS', 12), fg='red',
                                  bg='#eeeeff')
            no_money_geese.grid(row=7, column=7)

exit_button = Button(root, text="Exit Game",font=('Comic Sans MS', 12),bg='#111133',fg='#ffffff',command=exit,activebackground='#eeeeff',highlightbackground='#eeeeff')
exit_button.grid(row=1, column=7)

def light_mode():
    global dark
    root.configure(background='#eeeeff')
    darkmode.config(text='Dark mode : Off', command=dark_mode, padx=1)
    spacer_text.config(bg='#eeeeff', fg='#eeeeff')
    spacer2_text.config(bg='#eeeeff', fg='#eeeeff')
    spacer3_text.config(bg='#eeeeff', fg='#eeeeff')
    spacer4_text.config(bg='#eeeeff', fg='#eeeeff')
    spacer5_text.config(bg='#eeeeff', fg='#eeeeff')
    spacer6_text.config(bg='#eeeeff', fg='#eeeeff')
    spacer7_text.config(bg='#eeeeff', fg='#eeeeff')
    spacer8_text.config(bg='#eeeeff', fg='#eeeeff')
    spacer9_text.config(bg='#eeeeff', fg='#eeeeff')
    click_text.config(bg='#eeeeff', fg='#333344')
    coin_text.config(bg='#eeeeff', fg='#333344')
    mult_frame.config(bg='#eeeeff', fg='#333344')
    no_money_text.config(fg='red', bg='#eeeeff')
    no_money_geese.config(fg='red', bg='#eeeeff')
    clearerrors.config(padx=7)
    cleardata.config(padx=6)
    dark = False

def dark_mode():
    global dark
    root.configure(background='#333344')
    darkmode.config(text='Dark mode : On ', command=light_mode, padx=2)
    spacer_text.config(bg='#333344', fg='#333344')
    spacer2_text.config(bg='#333344', fg='#333344')
    spacer3_text.config(bg='#333344', fg='#333344')
    spacer4_text.config(bg='#333344', fg='#333344')
    spacer5_text.config(bg='#333344', fg='#333344')
    spacer6_text.config(bg='#333344', fg='#333344')
    spacer7_text.config(bg='#333344', fg='#333344')
    spacer8_text.config(bg='#333344', fg='#333344')
    spacer9_text.config(bg='#333344', fg='#333344')
    click_text.config(bg='#333344', fg='#ffffff')
    coin_text.config(bg='#333344', fg='#ffffff')
    mult_frame.config(bg='#333344', fg='#ffffff')
    no_money_geese.config(fg='red', bg='#333344')
    no_money_text.config(fg='red', bg='#333344')
    clearerrors.config(padx=6)
    cleardata.config(padx=5)
    dark = True

darkmode = Button(root, text='Dark mode : Off',font=('Comic Sans MS', 12),command=dark_mode,bg='#111133',fg='#ffffff',activebackground='#eeeeff',highlightbackground='#eeeeff',padx=1,pady=6)

def clear_errors():
    no_money_text.config(text=' ')
    no_money_geese.config(text=' ')

clearerrors = Button(root, text='Clear Errors',font=('Comic Sans MS', 14),command=clear_errors,bg='#111133',fg='#ffffff',activebackground='#eeeeff',padx=7,pady=5)

def clear_data():
    global clicks, coins, mult, geese, cheatused, cheat2used, cheat3used
    clicks = 0
    coins = 0
    mult = 1
    geese = 0
    click_text.config(text=f"Total clicks : {clicks}")
    coin_text.config(text=f"Coins : {coins}")
    mult_frame.config(text=f"Click multiplier : {mult}")
    mult_button.config(text=f'Buy Multiplier : {price}')
    cheatused = False
    cheat2used = False
    cheat3used = False

cleardata = Button(root, text=" Clear  Data ",font=('Comic Sans MS', 14),bg='#111133',fg='#ffffff',command=clear_data,activebackground='#eeeeff',highlightbackground='#eeeeff',padx=6,pady=0)

def settingsoff():
    settingsbutton.config(text='Settings', font=('Comic Sans MS', 12), command=settingson)
    cleardata.grid(row=7, column=11)
    clearerrors.grid(row=6, column=11)
    darkmode.grid(row=5, column=11)

def settingson():
    settingsbutton.config(text='Settings', font=('Comic Sans MS', 12), command=settingsoff)
    cleardata.grid(row=7, column=0)
    clearerrors.grid(row=6, column=0)
    darkmode.grid(row=5, column=0)
settingsbutton = Button(root, text='Settings',font=('Comic Sans MS', 12),command=settingson,bg='#111133',fg='#ffffff',activebackground='#eeeeff',highlightbackground='#eeeeff')
settingsbutton.grid(row=4, column=0)
cleardata.grid(row=7, column=11)
clearerrors.grid(row=6, column=11)
darkmode.grid(row=5, column=11)

# cheat codurile 

def cheats():
    global coins, cheatused, cheat2used, cheat3used, cheat4used, cheat5used, mult, price
    if code.get() == 'egg':
        if cheatused is False:
            mult += 1
            cheatused = True
            code.insert(0, "Code Redeemed : ")
        else:
            code.insert(0, 'Already used : ')
    elif code.get() == '10mult':
        if cheat2used is False:
            coins += 10
            mult += 10
            price = 25 * mult
            cheat2used = True
            coin_text.config(text=f"Coins : {coins}")
            mult_frame.config(text=f"Click multiplier : {mult}")
            mult_button.config(text=f'Buy Multiplier : {price}')
            code.insert(0, "Code Redeemed : ")
        else:
            code.insert(0, 'Already used : ')
    elif code.get() == 'money':
        if cheat3used is False:
            coins += 100
            cheat3used = True
            coin_text.config(text=f"Coins : {coins}")
            code.insert(0, "Code Redeemed : ")
        else:
            code.insert(0, 'Already used : ')
    elif code.get() == 'Incorrect Code : Incorrect Code : Incorrect Code : Incorrect Code : Incorrect Code : Incorrect Code : Incorrect Code : Incorrect Code : Incorrect Code : Incorrect Code : Incorrect Code : Incorrect Code : Incorrect Code : Incorrect Code : Incorrect Code : Incorrect Code : Incorrect Code : ' :
        if cheat4used is False:
            coins += 69420
            cheat4used = True
            coin_text.config(text=f"Coins : {coins}")
            code.insert(0, "Code Redeemed : ")
        else:
            code.insert(0, 'Already used : ')
    elif code.get() == 'nemo' or code.get() == 'NEMO':
        if cheat5used is False:
            coins += 1000
            mult += 10
            price = 25 * mult
            cheat5used = True
            coin_text.config(text=f"Coins : {coins}")
            mult_frame.config(text=f"Click multiplier : {mult}")
            mult_button.config(text=f'Buy Multiplier : {price}')
            code.insert(0, "omg nemo Code Redeemed : ")
        else:
            code.insert(0, 'Already used : ')
    else:
        code.insert(0, 'Incorrect Code : ')

code = Entry(width=22)
code.insert(0, 'Enter Cheat Code')
code.grid(row=6, column=4)
code_button = Button(root, text="Enter Code",font=('Comic Sans MS', 12),bg='#8888ff',fg='white',command=cheats,activebackground='#eeeeff',highlightbackground='#eeeeff',pady=2,padx=4)
code_button.grid(row=7, column=4)


root.mainloop()