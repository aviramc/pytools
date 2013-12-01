# TODO: Not cross platform. Maybe use colorama instead.

import sys
import os

foreground_colors = {'black' : 30,
                     'red' : 31,
                     'green' : 32,
                     'yellow' : 33,
                     'blue' : 34,
                     'purple' : 35,
                     'cyan' : 36,
                     'white' : 37,
                     }

background_colors = {'black' : 40,
                     'red' : 41,
                     'green' : 42,
                     'yellow' : 43,
                     'blue' : 44,
                     'purple' : 45,
                     'cyan' : 46,
                     'white' : 47,
                     }

text_styles = {'nothing' : 0,
               'bold' : 1,
               'underline' : 4,
               'blink' : 5,
               'inverse' : 7,
               'hidden' : 8,
               }

def color_write(text, foreground='white', background='black', style='nothing', file_object=None):
    if file_object is None:
        file_object = sys.stdout
    file_object.write(_format_string(text, foreground, background, style))

def color_print(text, foreground='white', background='black', style='nothing', newline=True):
    if newline:
        print _format_string(text, foreground, background, style)
    else:
        print _format_string(text, foreground, background, style),

def print_all_colors():
    for foreground in foreground_colors.iterkeys():
        for background in background_colors.iterkeys():
            for text_style in text_styles.iterkeys():
                color_print("%s %s %s" % (foreground, background, text_style),
                            foreground=foreground,
                            background=background,
                            style=text_style)

def _format_string(text, foreground, background, style):
    return '%s%s%s' % (_format_start(foreground, background, style), text, _format_reset())

def _format_start(foreground, background, style):
    return '\033[%d;%d;%dm' % (text_styles[style], background_colors[background], foreground_colors[foreground])

def _format_reset():
    return '\033[0m'
