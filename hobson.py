# -*- coding: utf-8 -*-
# HobsonPy - A GUI toolkit with simple features, take it or leave it. Cross-platform, text-based, built on tkinter, pure Python 3.
# "Simple is better than complex. Ugly is better than beautiful."

import tkinter as tk
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)

__version__ = '0.0.1'


# constants for widget orientation
HORIZONTAL = 'horizontal'
VERTICAL = 'vertical'

# constants for box-drawing border
SINGLE = 'single' # uses box-drawing characters like ┴└├┌
DOUBLE = 'double' # uses box-drawing characters like ╗╔╚╠


# default for Window objects
DEFAULT_FG = '#FFFFFF'
DEFAULT_BG = '#272822'


# Based off of the CSS3 standard names. Data from James Bennett's webcolors module: https://github.com/ubernostrum/webcolors
COLOR_NAMES_TO_HEX = {'aliceblue': '#f0f8ff','antiquewhite': '#faebd7','aqua': '#00ffff','aquamarine': '#7fffd4','azure': '#f0ffff','beige': '#f5f5dc','bisque': '#ffe4c4','black': '#000000','blanchedalmond': '#ffebcd','blue': '#0000ff','blueviolet': '#8a2be2','brown': '#a52a2a','burlywood': '#deb887','cadetblue': '#5f9ea0','chartreuse': '#7fff00','chocolate': '#d2691e','coral': '#ff7f50','cornflowerblue': '#6495ed','cornsilk': '#fff8dc','crimson': '#dc143c','cyan': '#00ffff','darkblue': '#00008b','darkcyan': '#008b8b','darkgoldenrod': '#b8860b','darkgray': '#a9a9a9','darkgrey': '#a9a9a9','darkgreen': '#006400','darkkhaki': '#bdb76b','darkmagenta': '#8b008b','darkolivegreen': '#556b2f','darkorange': '#ff8c00','darkorchid': '#9932cc','darkred': '#8b0000','darksalmon': '#e9967a','darkseagreen': '#8fbc8f','darkslateblue': '#483d8b','darkslategray': '#2f4f4f','darkslategrey': '#2f4f4f','darkturquoise': '#00ced1','darkviolet': '#9400d3','deeppink': '#ff1493','deepskyblue': '#00bfff','dimgray': '#696969','dimgrey': '#696969','dodgerblue': '#1e90ff','firebrick': '#b22222','floralwhite': '#fffaf0','forestgreen': '#228b22','fuchsia': '#ff00ff','gainsboro': '#dcdcdc','ghostwhite': '#f8f8ff','gold': '#ffd700','goldenrod': '#daa520','gray': '#808080','grey': '#808080','green': '#008000','greenyellow': '#adff2f','honeydew': '#f0fff0','hotpink': '#ff69b4','indianred': '#cd5c5c','indigo': '#4b0082','ivory': '#fffff0','khaki': '#f0e68c','lavender': '#e6e6fa','lavenderblush': '#fff0f5','lawngreen': '#7cfc00','lemonchiffon': '#fffacd','lightblue': '#add8e6','lightcoral': '#f08080','lightcyan': '#e0ffff','lightgoldenrodyellow': '#fafad2','lightgray': '#d3d3d3','lightgrey': '#d3d3d3','lightgreen': '#90ee90','lightpink': '#ffb6c1','lightsalmon': '#ffa07a','lightseagreen': '#20b2aa','lightskyblue': '#87cefa','lightslategray': '#778899','lightslategrey': '#778899','lightsteelblue': '#b0c4de','lightyellow': '#ffffe0','lime': '#00ff00','limegreen': '#32cd32','linen': '#faf0e6','magenta': '#ff00ff','maroon': '#800000','mediumaquamarine': '#66cdaa','mediumblue': '#0000cd','mediumorchid': '#ba55d3','mediumpurple': '#9370db','mediumseagreen': '#3cb371','mediumslateblue': '#7b68ee','mediumspringgreen': '#00fa9a','mediumturquoise': '#48d1cc','mediumvioletred': '#c71585','midnightblue': '#191970','mintcream': '#f5fffa','mistyrose': '#ffe4e1','moccasin': '#ffe4b5','navajowhite': '#ffdead','navy': '#000080','oldlace': '#fdf5e6','olive': '#808000','olivedrab': '#6b8e23','orange': '#ffa500','orangered': '#ff4500','orchid': '#da70d6','palegoldenrod': '#eee8aa','palegreen': '#98fb98','paleturquoise': '#afeeee','palevioletred': '#db7093','papayawhip': '#ffefd5','peachpuff': '#ffdab9','per': '#cd853f','pink': '#ffc0cb','plum': '#dda0dd','powderblue': '#b0e0e6','purple': '#800080','red': '#ff0000','rosybrown': '#bc8f8f','royalblue': '#4169e1','saddlebrown': '#8b4513','salmon': '#fa8072','sandybrown': '#f4a460','seagreen': '#2e8b57','seashell': '#fff5ee','sienna': '#a0522d','silver': '#c0c0c0','skyblue': '#87ceeb','slateblue': '#6a5acd','slategray': '#708090','slategrey': '#708090','snow': '#fffafa','springgreen': '#00ff7f','steelblue': '#4682b4','tan': '#d2b48c','teal': '#008080','thistle': '#d8bfd8','tomato': '#ff6347','turquoise': '#40e0d0','violet': '#ee82ee','wheat': '#f5deb3','white': '#ffffff','whitesmoke': '#f5f5f5','yellow': '#ffff00','yellowgreen': '#9acd32',}

# The root tkinter window object
_root_win = None


def hex_color(color):
    """
    Converts the `color` parameter to a standard '#ffffff' color string of a # followed by six hexadecimal digits. The `color` parameter can formatted as a CSS3 name, #ffffff, ffffff, #fff, or fff.

    TODO: Expand to include rgb triplet integers, and three percentages?

    >>> hex_color('white')
    '#ffffff'
    >>> hex_color('#ffffff')
    '#ffffff'
    >>> hex_color('#fff')
    '#ffffff'
    >>> hex_color('ffffff')
    '#ffffff'
    >>> hex_color('fff')
    '#ffffff'
    >>> hex_color('#abc')
    '#aabbcc'
    """
    if type(color) != str:
        raise TypeError('Parameter `color` must be of type str, not %s.' % (type(color)))

    color = color.lower() # normalize to lowercase

    if color in COLOR_NAMES_TO_HEX:
        return COLOR_NAMES_TO_HEX[color]

    if color.startswith('#'):
        color = color[1:] # remove the leading #

    try:
        int(color, 16) # check that it's a hexadecimal number
        if len(color) == 3:
            return '#' + color[0] + color[0] + color[1] + color[1] + color[2] + color[2] # normalize to '#ffffff' format
        elif len(color) == 6:
            return '#' + color
        else:
            raise ValueError('Parameter `color` must be a hexadecimal number or valid color name.')
    except ValueError:
        raise ValueError('Parameter `color` must be a hexadecimal number, not %s.' % (type(color)))


# from http://www.roguebasin.com/index.php?title=Bresenham%27s_Line_Algorithm#Python
def get_line_points(x1, y1, x2, y2):
    """Returns a list of (x, y) tuples of every point on a line between
    (x1, y1) and (x2, y2). The x and y values inside the tuple are integers.

    Line generated with the Bresenham algorithm.

    Args:
      x1 (int, float): The x coordinate of the line's start point.
      y1 (int, float): The y coordinate of the line's start point.
      x2 (int, float): The x coordinate of the line's end point.
      y2 (int, float): The y coordiante of the line's end point.

    Returns:
      [(x1, y1), (x2, y2), (x3, y3), ...]

    Example:
    >>> getLine(0, 0, 6, 6)
    [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)]
    >>> getLine(0, 0, 3, 6)
    [(0, 0), (0, 1), (1, 2), (1, 3), (2, 4), (2, 5), (3, 6)]
    >>> getLine(3, 3, -3, -3)
    [(3, 3), (2, 2), (1, 1), (0, 0), (-1, -1), (-2, -2), (-3, -3)]
    """
    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
    points = []
    issteep = abs(y2-y1) > abs(x2-x1)
    if issteep:
        x1, y1 = y1, x1
        x2, y2 = y2, x2
    rev = False
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
        rev = True
    deltax = x2 - x1
    deltay = abs(y2-y1)
    error = int(deltax / 2)
    y = y1
    ystep = None
    if y1 < y2:
        ystep = 1
    else:
        ystep = -1
    for x in range(x1, x2 + 1):
        if issteep:
            points.append((y, x))
        else:
            points.append((x, y))
        error -= deltay
        if error < 0:
            y += ystep
            error += deltax
    # Reverse the list if the coordinates were reversed
    if rev:
        points.reverse()
    return points


class Window:
    """
    A single tkinter window that contains HobsonPy UI widgets such as buttons,
    text boxes, and a general surface to draw text characters on.

    The first window created is the "root" window. The mainloop() method must be
     called on it before it will appear. Subsequent Window objects will appear
     as soon as they are created.

     Menus must be supplied at constructor call time, however their contents can
     change afterwards.


    FAQ:

    The GUIs that HobsonPy creates are really ugly. Is there a way to make them look better or more professional?
    No. HobsonPy is specifically for quick, ugly, non-professional GUI apps. Use a real GUI toolkit if you want better looking software.

    Note: A "keyboard shortcut" is a keyboard combination such as Ctrl+C or Alt+F4. A "hotkey" is a single letter you press to select a menu item, such as the "F" in _F_ile.

    FAQ:

    Can I resize the HobsonPy window after creating it?
    No. This is so that the widgets don't have to be responsive to window resizes.

    Can I resize the font after creating the window?
    No. Al Sweigart could be persuaded to add this as a feature, but he can't think of a good use case for it.

    Is there support for variable-width fonts like Helvetica?
    No.

    Can I use a custom font?
    No. Courier (Tkinter's default monospace) is used for maximum unicode compatibility and because it is monospaced.

    Can widgets overlap and have parent-child relationships, like a textbox that contains a button?
    No. Flat is better than nested.

    What if I have too many GUI widgets for the window's size? Can I scroll inside the window?
    No. If you need more widgets than the size of the window, your app is too complicated.

    What about systems that have a small screen resolution? Shouldn't windows be scrollable for them?
    No.

    Is there a menu widget?
    No. Use the actual tkinter menu instead.

    Are there themes for the fg and bg colors?
    No.

    Will the answer to these FAQs ever be anything besides "no"?
    No. Although sometimes there will additional information following the "no".

    Are there drawing functions for circles, ellipses, and arcs?
    No. Only for lines. HobsonPy is primarily about making simple GUIs, which usually only have lines and rectangles.

    Is there a flood fill drawing function?
    No.

    Is there a drawing function for a filled in polygon?
    No.
    """
    def __init__(self, width=80, height=25, title='', fg=DEFAULT_FG, bg=DEFAULT_BG, font_size=10, menu=None):
        """

        """

        global _root_win

        # TODO type checks

        # Validate parameters.
        if type(width) != int:
            raise TypeError('Parameter `width` must be of type int, not %s.' % (type(width)))
        if width < 1:
            raise ValueError('Parameter `width` must be greater than 0.')
        if type(height) != int:
            raise TypeError('Parameter `height` must be of type int, not %s.' % (type(height)))
        if height < 1:
            raise ValueError('Parameter `height` must be greater than 0.')

        self.win_width = width # width is in number of cells, not pixels
        self.win_height = height # height is in number of cells, not pixels

        self.title = str(title)

        self.fg = hex_color(fg)
        self.bg = hex_color(bg)

        if type(font_size) != int:
            raise TypeError('Parameter `font_size` must be of type int, not %s.' % (type(font_size)))
        if font_size <= 0:
            raise ValueError('Parameter `font_size` must be greater than 0, not %s.' % (font_size))

        if menu is not None:
            pass # TODO - create the menu

        self.font_size = font_size

        # Create the tkinter window and tk Text widget.
        self._tk_win = tk.Tk()
        self._tk_win.title(self.title)
        self._tk_win.resizable(False, False) # disable resizing of the window

        self._tk_text = tk.Text(self._tk_win, height=self.win_height, width=self.win_width, font=('Courier', self.font_size))
        self._tk_text.pack()
        self._tk_text.configure(state='disabled') # make the tk text widget read-only

        # If this is the first Hobson window created, set _root_win to it.
        if _root_win is None:
            _root_win = self._tk_win
            self._is_root = True

        # Populate the cells of this window.
        self._widgets = {} # contains all the widgets added to the Window. This is used to check for overlapping widgets.
        self._char_cells = {} # keys are (x, y) tuples, values are single char strings
        self._fg_cells = {} # keys are (x, y) tuples, values are '#ffffff' strings
        self._bg_cells = {} # keys are (x, y) tuples, values are '#ffffff' strings
        # Note: event handler assignments are assigned to rectangles since widgets are what handle events

        for x in range(self.win_width):
            for y in range(self.win_height):
                self._char_cells[x, y] = '.'
                self._fg_cells[x, y] = DEFAULT_FG
                self._bg_cells[x, y] = DEFAULT_BG
        self.redraw()

    def redraw(self):
        self._tk_text.configure(state='normal') # make the tk text widget editable

        self._tk_text.delete('1.0', '%s.%s' % (self.win_height + 1, self.win_width + 1)) # +1 to height because it is 1-based, +1 to width because we need to select the index after the last character
        self._tk_text.insert('1.0', self.screenshot()) # write out the text

        # Remove all the tags for this tkinter text box widget.
        for tag in self._tk_text.tag_names():
            self._tk_text.tag_delete(tag)

        # Note about the variable names here. I use "x" and "y" as 0-based coordinates for the indexes for self._*_cells.
        # However, "row" and "col" refer to indexes in the tkinter text widget, where rows are 1-based (though columns are 0-based).
        # Keep this in mind when using row/col for self._*_cells or x/y for the text widget's indexes.
        '''
        # NOTE: THE RUN-PAINTING CODE IS KIND OF BUGGY FOR NOW
        for row in range(1, self.win_height + 1): # +1 because the row numbers are 1-based
            start_run_index = 0 # since it's faster to change the fg/bg of a contiguous run of characters with the same fg/bg, we need to track the "runs"
            # Note that runs are always limited to one row. Runs do not span across rows.
            run_fg = self._fg_cells[start_run_index, row - 1]
            run_bg = self._bg_cells[start_run_index, row - 1]
            end_run_index = start_run_index
            for col in range(self.win_width):
                if self._fg_cells[col, row - 1] == run_fg and self._bg_cells[col, row - 1] == run_bg:
                    end_run_index = col
                else:
                    # fg or bg has changed, so the run has ended. Let's paint the run.
                    tag_name = 'r%sc%s' % (row, col) # Really, the tag name only has to be unique, it doesn't matter what it is.
                    tag_start_index = '%s.%s' % (row, start_run_index)
                    tag_end_index = '%s.%s' % (row, end_run_index + 1) # +1 to end_run_index because we need to use the index one past the index we want to repaint
                    self._tk_text.tag_add(tag_name, tag_start_index, tag_end_index)

                    self._tk_text.tag_config(tag_name, background=run_bg, foreground=run_fg ) # set the fg and bg colors
                    start_run_index = col + 1 # next run begins on the next index
                    run_fg = self._fg_cells[start_run_index, row - 1]
                    run_bg = self._bg_cells[start_run_index, row - 1]
                    end_run_index = start_run_index
        '''

        self._tk_text.configure(state='disabled') # make the tk text widget read-only

    def mainloop(self):
        if self._is_root:
            _root_win.mainloop()


    def __getattr__(self, name):

        # Search through self._widgets
        if name in self._widgets:
            return self._widgets[name]

        raise AttributeError("AttributeError: '%s' object has no attribute '%s'" % (type(self).__name__, name))


    def normalize_fg_bg(self, fg, bg):
        """

        """

        if fg is None:
            fg = self.fg # use the window's default foreground color
        if bg is None:
            bg = self.bg # use the window's default background color

        fg = hex_color(fg)
        bg = hex_color(bg)

        return fg, bg


    def screenshot(self):
        # TODO - have some way of extracting the color information. Maybe html?
        lines = []
        for y in range(self.win_height):
            line = []
            for x in range(self.win_width):
                line.append(self._char_cells[x, y])
            lines.append(''.join(line))
        return '\n'.join(lines)


    def draw_line(self, startx, starty, endx, endy, char='*', fg=None, bg=None, _viewport=None):
        """
        Note that the draw_*() functions only draw to the screen once and will not automatically redraw themselves later.

        FAQ:

        Can the drawing functions draw lines with thicknesses greater than 1 cell?
        No.
        """

        # Validate all the parameters:
        if type(startx) != int:
            raise TypeError('Parameter `startx` must be an int, not %s.' % (type(startx)))
        if type(starty) != int:
            raise TypeError('Parameter `starty` must be an int, not %s.' % (type(starty)))

        if type(endx) != int:
            raise TypeError('Parameter `endx` must be an int, not %s.' % (type(endx)))
        if type(endy) != int:
            raise TypeError('Parameter `endy` must be an int, not %s.' % (type(endy)))

        # Note: The X and Y positions for drawing functions can be beyond the window's coordinates.

        if type(char) != str :
            raise TypeError('Parameter `char` must be a str, not a %s.' % (type(char)))
        if len(char) != 1:
            raise ValueError('Parameter `char` must be a single character string.')

        # The viewport is a subsection of the window that we are limited to drawing to.
        if _viewport is None:
            left_edge, top_edge, right_edge, bottom_edge = 0, 0, self.win_width - 1, self.win_height - 1
        else:
            left_edge, top_edge, right_edge, bottom_edge = _viewport[0], _viewport[1], _viewport[0] + _viewport[2] - 1, _viewport[1] + _viewport[3] - 1

        fg, bg = self.normalize_fg_bg(fg, bg) # normalize fg and bg

        for x, y in get_line_points(startx, starty, endx, endy):
            if left_edge <= x <= right_edge and top_edge <= y <= bottom_edge:
                # TODO - you should only be able to draw inside the viewport and not overlapping any widgets' areas.
                self._char_cells[x, y] = char
                self._fg_cells[x, y] = fg
                self._bg_cells[x, y] = bg
        self.redraw()


    def draw_rect(self, left, top, width, height, char='*', fg=None, bg=None, filled=False, _viewport=None):
        """
        Note that the draw_*() functions only draw to the screen once and will not automatically redraw themselves later.

        FAQ:

        Can I have the different corners and sides be drawn with different characters?
        No. Use the draw_box() function instead.
        """

        if type(left) != int:
            raise TypeError('Parameter `left` must be an int, not %s.' % (type(left)))
        if type(top) != int:
            raise TypeError('Parameter `top` must be an int, not %s.' % (type(top)))

        if type(width) != int:
            raise TypeError('Parameter `width` must be of type int, not %s.' % (type(width)))
        if width < 1:
            raise ValueError('Parameter `width` must be greater than 0.')
        if type(height) != int:
            raise TypeError('Parameter `height` must be of type int, not %s.' % (type(height)))
        if height < 1:
            raise ValueError('Parameter `height` must be greater than 0.')

        if type(char) != str :
            raise TypeError('Parameter `char` must be a str, not a %s.' % (type(char)))
        if len(char) != 1:
            raise ValueError('Parameter `char` must be a single character string.')

        fg, bg = self.normalize_fg_bg(fg, bg)

        # The viewport is a subsection of the window that we are limited to drawing to.
        if _viewport is None:
            left_edge, top_edge, right_edge, bottom_edge = 0, 0, self.win_width - 1, self.win_height - 1
        else:
            left_edge, top_edge, right_edge, bottom_edge = _viewport[0], _viewport[1], _viewport[0] + _viewport[2] - 1, _viewport[1] + _viewport[3] - 1

        if filled: # draw a filled in rectangle
            for x in range(left, left + width):
                for y in range(top, top + height):
                    self._char_cells[x, y] = char
                    self._fg_cells[x, y] = fg
                    self._bg_cells[x, y] = bg

        else: # draw just the outline of the rectangle
            for x in range(left, left + width):
                if left_edge <= x <= right_edge and top_edge <= top <= bottom_edge:
                    self._char_cells[x, top] = char
                    self._fg_cells[x, top] = fg
                    self._bg_cells[x, top] = bg
                if left_edge <= x <= right_edge and top_edge <= top + height - 1 <= bottom_edge:
                    self._char_cells[x, top + height - 1] = char
                    self._fg_cells[x, top + height - 1] = fg
                    self._bg_cells[x, top + height - 1] = bg

            for y in range(top, top + height):
                if left_edge <= left <= right_edge and top_edge <= y <= bottom_edge:
                    self._char_cells[left, y] = char
                    self._fg_cells[left, y] = fg
                    self._bg_cells[left, y] = bg
                if left_edge <= left + width - 1 <= right_edge and top_edge <= y <= bottom_edge:
                    self._char_cells[left + width - 1, y] = char
                    self._fg_cells[left + width - 1, y] = fg
                    self._bg_cells[left + width - 1, y] = bg

        self.redraw()


    def draw_fill(self, char=' ', fg=None, bg=None, _viewport=None):
        """
        Note that the draw_*() functions only draw to the screen once and will not automatically redraw themselves later.

        FAQ:

        Can I just fill in part of the window?
        No. Use draw_rect() with filled=True to do that.
        """
        self.draw_rect(0, 0, self.win_width, self.win_height, char, fg, bg, True)


    def draw_box(self, left, top, width, height, title='', fg=None, bg=None, border=SINGLE, _viewport=None):
        """Adjusts characters for proper box drawing based on neighboring cells. Can have title.

        Note that draw_box()'s `border` parameter cannot be None.'

        FAQ:

        Can I have the title appear on the bottom or sides instead of the top?
        No.
        Can lines have thicknesses greater than 1 cell?
        No.
        Can I draw a box that's filled in?
        No. Use draw_rect() with filled=True to do that.
        """

        if type(left) != int:
            raise TypeError('Parameter `left` must be an int, not %s.' % (type(left)))
        if type(top) != int:
            raise TypeError('Parameter `top` must be an int, not %s.' % (type(top)))

        if type(width) != int:
            raise TypeError('Parameter `width` must be of type int, not %s.' % (type(width)))
        if width < 1:
            raise ValueError('Parameter `width` must be greater than 0.')
        if type(height) != int:
            raise TypeError('Parameter `height` must be of type int, not %s.' % (type(height)))
        if height < 1:
            raise ValueError('Parameter `height` must be greater than 0.')

        title = str(title)

        if type(border) != str:
            raise TypeError('Parameter `border` must be a str, not %s.' % (type(border)))

        if len(border) != 1 and border not in (SINGLE, DOUBLE):
            raise ValueError('Parameter `border` must be hobson.SINGLE, hobson.DOUBLE, or a single character str.')

        fg, bg = self.normalize_fg_bg(fg, bg)

        pass


    def write(self, left, top, text, fg=None, bg=None, _viewport=None):
        """
        Draws text onto the window. The `text` argument can contain TODOself.cells[left + col_num, top + line_num].char = char
        Note that any newline characters cause the cursor to move back to left position of `left`, not to the left edge of the window. Text does not wrap when it reaches the right edge of the window, but rather is truncated.
        Note that the draw_*() functions only draw to the screen once and will not automatically redraw themselves later.
        """
        if type(left) != int:
            raise TypeError('Parameter `left` must be an int, not %s.' % (type(left)))
        if type(top) != int:
            raise TypeError('Parameter `top` must be an int, not %s.' % (type(top)))

        text = str(text)

        fg, bg = self.normalize_fg_bg(fg, bg)


        # TODO - if we try to write anything on a cell that is covered by a widget, then simply don't write it.

        for line_num, line in enumerate(text.split('\n')):
            if top + line_num < 0 or top + line_num >= self.win_height:
                continue # This line is past the top or bottom edge of the window, so skip it.

            if left < 0:
                line = line[-left:] # If writing is past the left edge, truncate it.
            if len(line) > self.win_width:
                line = line[:self.win_width - len(line)] # If the text goes past the right edge, truncate it.

            for col_num, char in enumerate(line):
                self._char_cells[left + col_num, top + line_num] = char
                self._fg_cells[left + col_num, top + line_num] = fg
                self._bg_cells[left + col_num, top + line_num] = bg



class Widget:
    """

    FAQ:

    Can widgets overlap and have parent-child relationships, like a textbox that contains a button?
    No. Flat is better than nested.

    Can widgets overlap each other?
    No.

    Is there a tabbed interface widget?
    No. And please don't create any as this would violate the "no overlap" rule.

    Is there an accordion or collapsible panel widget?
    No. And please don't create any as this would violate the "no overlap" rule.

    How about if widgets aren't visible? Then can they overlap each other?
    No.

    Is there a modal window widget?
    No. And please don't create any as this would violate the "no overlap" rule. Use the HobsonPy alert(), confirm(), prompt(), or password() functions instead. (These use the PyMsgBox module.)

    Will HobsonPy ever have these widgets or features in the future?
    No.

    Can a widget's tool tip appear anywhere besides the status bar on the bottom row?
    No.

    Are there any layout or geometry managers for HobsonPy?
    No.
    """
    top = 0
    left = 0
    visible = True
    enabled = True
    width = 1
    height = 1
    tooltip = '' # Tool tips only appear in the status bar, and only if a status bar exists.

class Button(Widget):
    """

    FAQ:

    Can the button's text be left- or right-justified instead of centered?
    No.
    """
    def __init__(self, topleft, width, height, text, border):
        pass


class Textbox(Widget):
    """
    TODO - supports highlighting/copy/paste

    FAQ:

    Can a text box contain text of more than one color?
    No.

    Can a text box have just some text that acts as a clickable HTML link, instead of all of it?
    No.

    Can I control the speed that widgets blink?
    No.
    """
    def __init__(self):
        self.blink = False # Mwahahaha! Long live <blink>!
        self.cursor = (0, 0)

    def print(self, *objects, sep=' ', end='\n'):
        pass

    def screenshot(self):
        pass

class Link(Textbox):
    """

    FAQ:

    Can I have just some of the text in the link widget be a link, intead of all of it?
    No.
    """

class Input(Textbox):
    """
    TODO - supports autocomplete and validation and highlighting/copy/paste
    """
    def __init__(self, top, left, width, height, validationFunc, mask=None):
        pass

    def validate(self):
        pass


def Password(mask):
    """
    A wrapper for Input() class that sets the mask character.
    """
    return Input()


class Radio(Widget):
    def __init__(self):
        pass


class Checkbox(Widget):
    def __init__(self):
        pass


class Select(Widget):
    """

    FAQ:

    Is there a combobox widget?
    No.

    Can the select list have its items listed horizontally?
    No.

    Shouldn't the select list widget be prohibited under HobsonPy's "no overlap" rule?
    No. Practicality beats purity.
    """
    def __init__(self):
        pass


class StatusBar(Widget):
    """
    Can a status bar be anywhere besides the bottom row?
    No.

    Can there be more than one status bar in a window?
    No.
    """
    def __init__(self):
        pass


class ScrollBar(Widget):
    def __init__(self):
        pass


class Slider(Widget):
    def __init__(self):
        pass


class ProgressBar(Widget):
    """

    FAQ:

    Can progress bars be thicker than a single character?
    No.

    """
    def __init__(self, x, y, value=0, min=0, max=100, bar_char='#', empty_char='.', orientation=HORIZONTAL, change=None):
        pass


class Spinner(Widget):
    """

    FAQ:

    Can I adjust the speed of the spinner widget animation?
    No.


    """
    def __init__(self, x, y, visible=False, chars=('|', '/', '-', '\\')):
        pass

'''
TODO - These can be implemented in the future.

class Image(Widget):
    def __init__(self):
        pass

class TreeView(Widget):
    def __init__(self):
        pass

class GridView(Widget):
    """
    Can the grid view hold values besides strings?
    No.
    """
    def __init__(self):
        pass


class InteractiveShell(Widget):
    def __init__(self):
        pass

class TimePicker(Widget):
    def __init__(self):
        pass

class DatePicker(Widget):
    """
    Can I change the size of the date picker to something besides 20 x 8?
    No.
    """
    def __init__(self):
        pass

class ColorPicker(Widget):
    pass

class FIGletTextbox(Widget):
    pass

class OpenDialog(Widget):
    pass

class SaveAsDialog(Widget):
    pass
'''

class OverlappedWidgetException(Exception):
    pass

class DuplicateKeyboardShortcutException(Exception):
    pass

