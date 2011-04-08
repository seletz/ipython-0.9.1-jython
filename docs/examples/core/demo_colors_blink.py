#!/usr/bin/env python
"""
Test program; based on the main() of the PyColorize.py module.
"""

import token
import tokenize
_KEYWORD = token.NT_OFFSET + 1
_TEXT    = token.NT_OFFSET + 2

from IPython.ColorANSI import ColorScheme, TermColors
Colors = TermColors

BlinkLinuxColors = ColorScheme(
   'BlinkLinux', {
   token.NUMBER     : Colors.BlinkLightCyan,
   token.OP         : Colors.BlinkYellow,
   token.STRING     : Colors.BlinkLightBlue,
   tokenize.COMMENT : Colors.BlinkLightRed,
   token.NAME       : Colors.BlinkWhite,
   token.ERRORTOKEN : Colors.BlinkRed,

   _KEYWORD         : Colors.BlinkLightGreen,
   _TEXT            : Colors.BlinkYellow,

   'normal'         : Colors.Normal  # color off (usu. Colors.Normal)
   } )

if __name__ == "__main__":
   import sys
   from IPython.PyColorize import Parser
   if len(sys.argv) == 1:
       stream = sys.stdin
   else:
       stream = file(sys.argv[1])

   parser = Parser({'BlinkLinux': BlinkLinuxColors})
   try:
       try:
           # write colorized version to stdout
           parser.format(stream.read(), scheme="BlinkLinux")
       except IOError,msg:
           # if user reads through a pager and quits, don't print traceback
           if msg.args != (32,'Broken pipe'):
               raise
   finally:
       if stream is not sys.stdin:
           stream.close() # in case a non-handled exception happened above
