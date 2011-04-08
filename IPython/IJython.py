# -*- coding: utf-8 -*-
import IPython
import GnuRL

try:
   IPython.Shell.start().mainloop(sys_exit=False)
finally:
 GnuRL.cleanup()
