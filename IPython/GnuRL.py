# -*- coding: utf-8 -*-
"""
Tries to wrap org.gnu.readline impl as if it was default python readline module
"""
import org.gnu.readline.Readline as Readline
import org.python.util.ReadlineWrapper as ReadlineWrapper

def cleanup():
    Readline.cleanup()
    pass

class RLWrapper(ReadlineWrapper):
    def __init__(self, printUnsupported=False):
        ReadlineWrapper.__init__(self)
        self.printUnsupported=printUnsupported
        self.completeFunc=Readline.getCompleter()
        self.initFunc=None
        Readline.setCompleter(self)
        pass
    
    def py_complete(self, text, state):
        """call the registered function to do completion"""
        if self.completeFunc is None:
            return None
        return self.completeFunc(text,state)
    
    def py_doinit(self):
        if self.initFunc is not None:
            self.initFunc()
        pass

    def parse_and_bind(self,string):
        """Parse and execute single line of a readline init file."""
        return Readline.parseAndBind(string)

    def get_line_buffer(self):
        """Return the current contents of the line buffer."""
        return Readline.getLineBuffer()
    
    def read_init_file(self,filename):
        """Parse a readline initialization file."""
        Readline.readInitFile(filename)
        pass

    def read_history_file(self,filename):
        """Load a readline history file. The     default filename is ~/.history."""
        Readline.readHistoryFile(filename)
        pass
    
    def write_history_file(self,filename):
        """Save a readline history file. The         default filename is ~/.history."""
        Readline.writeHistoryFile(filename)
        pass
        
    def clear_history(self):
        """Clear the current history. (Note: this function is not available if the installed version of GNU readline doesn’t support it.)"""
        Readline.clearHistory()
        pass
    
    def get_current_history_length(self):
        """Return the number of lines currently in the history."""
        return Readline.getHistorySize()

    def get_history_item(self,index):
        """Return the current contents of history item at index."""
        return self.getHistoryLine(index)
        
    def set_completer(self,function):
        """Set or remove the completer function. If function is specified, it will be used as the new completer function; if omitted or None, any completer function already installed is removed. The completer function is called as function(text, state), for state in 0, 1, 2, ..., until it returns a non-string value. It should return the next possible completion starting with text."""
        self.completeFunc=function
        pass
    
    def get_completer(self):
        """Get the completer function, or None if no completer function has been set."""
        return self.completeFunc
        
    def set_completer_delims(self,string):
        """Set the readline word delimiters for tab-completion."""
        Readline.setWordBreakCharacters(string)

    def get_completer_delims(self):
        """Get the readline word delimiters for tab-completion."""
        return str(Readline.getWordBreakCharacters())

    def add_history(self,line):
        """Append a line to the history buffer, as if it was the last line typed."""
        Readline.addToHistory(line)

    def set_startup_hook(self,function):
        """Set or remove the startup_hook function. If function is specified, it will be used as the new startup_hook function; if omitted or None, any hook function already installed is removed. The startup_hook function is called with no arguments just before readline prints the first prompt."""
        self.initFunc=function
        pass
    
    def get_completion_type(self):
        """Get the type of completion being attempted."""
        self.unsupportedFunction("get_completion_type()") #XXX
        return 0
    
    def get_begidx(self):
        """Get the beginning index of the readline tab-completion scope."""
        self.unsupportedFunction("get_begidx()") #XXX
        return 0
    
    def get_endidx(self):
        """Get the ending index of the readline tab-completion scope."""
        self.unsupportedFunction("get_endidx()") #XXX
        return 1
    
    def redisplay(self):
        """Change what’s displayed on the screen to reflect the current contents of the line buffer."""
        self.unsupportedFunction("redisplay()") #XXX
        pass
    
    def get_history_length(self):
        """Return the desired length of the history file. Negative values imply unlimited history file size."""
        self.unsupportedFunction("get_history_length()") #XXX
        return - 1
    
    def set_history_length(self,length):
        """Set the number of lines to save in the history file. write_history_file() uses this value to truncate the history file when saving. Negative values imply unlimited history file size."""
        self.unsupportedFunction("set_history_length(%i)"%(length)) #XXX
        pass
    
    def set_completion_display_matches_hook(self,function):
        """Set or remove the completion display function. If function is specified, it will be used as the new completion display function; if omitted or None, any completion display function already installed is removed. The completion display function is called as function(substitution, [matches], longest_match_length) once each time matches need to be displayed."""
        self.unsupportedFunction("set_completion_display_matches_hook(function)") #XXX

    def remove_history_item(self,pos):
        """Remove history item specified by its position from the history."""
        self.unsupportedFunction("remove_history_item(%i)"%(pos)) #XXX
        pass

    def replace_history_item(self,pos, line):
        """Replace history item specified by its position with the given line."""
        self.unsupportedFunction("replace_history_item(%i, %i)"%(pos,line)) #XXX
        pass

    def insert_text(self,string):
        """Insert text into the command line."""
        self.unsupportedFunction("insert_text(%s)"%(string)) #XXX
        pass

    def set_pre_input_hook(self,function):
        """Set or remove the pre_input_hook function. If function is specified, it will be used as the new pre_input_hook function; if omitted or None, any hook function already installed is removed. The pre_input_hook function is called with no arguments after the first prompt has been printed and just before readline starts reading input characters."""
        self.unsupportedFunction("set_pre_input_hook([function])") #XXX
        pass
    
    def unsupportedFunction(self, msg):
        if self.printUnsupported:
            print "UNSUPPORTED: '%s'" %(msg)
            pass
        pass
    
    pass #end RLWrapper
