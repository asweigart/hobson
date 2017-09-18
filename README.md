# Hobson

**NOTE: Hobson is still very much under development and still in the brainstorming phase. Send ideas to @AlSweigart or al@inventwithpython.com**

A GUI toolkit with simple features, take it or leave it. Cross-platform, text-based, pure Python 3.

"Simple is better than complex. Ugly is better than beautiful."

> I needed a way for beginner programmers to make programs that had graphical user interfaces, not just programs that used print() and input(). But I wanted it to be simple enough that they could get started right away. Making offfline browser apps with Flask is okay, but it still requires teaching HTML, teaching Flask, and dabbling a bit in CSS and JavaScript and maybe Bootstrap. That's way too much runway that needs to be cleared.

> Those old DOS programs were ugly, but their coordinate system was dead simple. It was easy to count the size of things by character boxes. I just needed a GUI for a small program without diving into the documentation of a real GUI toolkit likt tkinter or wxPython. So I designed Hobson after Hobson's Choice: "Take it or leave it." Hobson is very limited in its options and it's ugly, but the ugliness works in its favor: it sets expectations that this is a throwaway program.

> Hobson's primary benefit is that it is easy to learn.


TODO - It's designed to support Unicode, so you can use unicode characters so it won't be as bad as DOS. Monospace width only.

TODO - Errors are mostly silenced. Overlapping widget rule.

# Install Hobson

`pip install hobson`

You can also simply copy `hobson.py` to your program's folder and import it. Hobson is designed to be in a single file so including it with your programs is easy.

# Quickstart Example

Let's create a fahrenheit and celsius temperature converter. It'll have two text boxes for entering and displaying the temperature in F and C, as well as two buttons to convert both ways. It'll look like this:


![Screenshot of Temp Convert program](https://github.com/asweigart/hobson/blob/master/tempconvert.png "Temp Convert Program")

The GUI uses "DOS box drawing" characters:

    ╔═F°═════╗╔═C°═════╗
    ║72      ║║22.22222║
    ╚════════╝╚════════╝
    ┌───────┐ ┌───────┐
    │Convert│█│Convert│█
    │ to C° │█│ to F° │█
    └───────┘█└───────┘█
     █████████ █████████

Import Hobson at the top of your program:

    import hobson

Create a window, specifying the width, height, and optionally the window title:

    win = hobson.Window(80, 25, 'Temp Convert')

The `win` global variable contains a "god object" for our app. This is a programming anti-pattern, but Hobson is made for quick and dirty apps.

Next, we'll create the text boxes:

    win.textbox(0, 0, 10, 3, 'F°', name='fbox')
    win.textbox(10, 0, 10, 3, 'C°', name='cbox')

The first four numbers are the topleft x and y coordinates, width, and height. Like all Hobson widgets, the width and height include the borders, so the smallest size is 3x3. Notice that unlike DOS, we can use any unicode character we want including the degree symbol. We give the widgets the names `'fbox'` and `'cbox'` so that we can refer to it later.

Next, we need some functions that the buttons will call which will calculate the temperature and output it to the text box:

    def convertFtoC(fdegrees):
        win.cbox.text = fdegrees - 32 / 1.8

    def convertCtoF(cdegrees):
        win.fbox.text = cdegrees * 1.8 + 32

Note that the `fbox` attribute is created when the `textbox` widget was added. Also, it's `text` attribute automatically casts to strings and any characters that don't fit into the text box are silently truncated. The user can always right-click any text box widget and hit "select all" to copy the full text from it.

Next, we'll create the buttons:

    win.button(0, 3, 10, 5, 'Convert\nto C°', click=convertFtoC)
    win.button(0, 3, 10, 5, 'Convert\nto F°', click=convertCtoF)

Notice that the text in the buttons is automatically centered, and that the width and height includes the button's border and shadow, making the smallest possible button 4x4. There is also a callback function for the click event.

We already have the minimize and close buttons added for free from tkinter. (Hobson windows cannot be resized.) Hobson uses tkinter's own menus, but it adds a nicer API. The menu has to be created before the window, so let's put this code at the top:

    def resetTemp():
        win.cbox.text = 0
        win.fbox.text = 32

    def showAbout():
        # Create a Hobson window that just says "Programmed by Al"
        aboutWin = hobson.Window(16, 1, 'About')
        aboutWin.write(0, 0, 'Programmed by Al')

    menu = ([
               {'_File': [
                             ['_Reset', resetTemp],
                             ['E_xit', root.destroy, 'Ctrl+Q']
                         ]
               },
               ['_About', showAbout]
           ])

    win = hobson.Window(80, 25, 'Hello, world!', menu=menu)

The `Menu` object accepts a list of menu items. Each menu item is a list of a label string (with `_` before a letter to make it a menu hotkey), a function to call, and optionally another string detailing the keyboard shortcut. If you want submenus under the menu item, use a dictionary where the key is the label and the value is a list of these menu item lists.


This is the entire program:

    import hobson

    def resetTemp():
        win.cbox.text = 0
        win.fbox.text = 32

    def showAbout():
        # Create a Hobson window that just says "Programmed by Al"
        aboutWin = hobson.Window(16, 1, 'About')
        aboutWin.write(0, 0, 'Programmed by Al')

    menu = ([
               {'_File': [
                             ['_Reset', resetTemp],
                             ['E_xit', root.destroy, 'Ctrl+Q']
                         ]
               },
               ['_About', showAbout]
           ])

    win = hobson.Window(80, 25, 'Hello, world!', menu=menu)

    win.textbox(0, 0, 10, 3, 'F°', name='fbox')
    win.textbox(10, 0, 10, 3, 'C°', name='cbox')

    def convertFtoC(fdegrees):
        win.cbox.text = fdegrees - 32 / 1.8

    def convertCtoF(cdegrees):
        win.fbox.text = cdegrees * (9/5) + 32

    win.button(0, 3, 10, 5, 'Convert\nto C°', click=convertFtoC)
    win.button(0, 3, 10, 5, 'Convert\nto F°', click=convertCtoF)
