# -*- coding: utf-8 -*-
import GnuRL

console = GnuRL.RLWrapper()

def cleanup():
    GnuRL.cleanup()
    pass

def parse_and_bind(string):
    console.parse_and_bind(string)
    pass

def get_line_buffer():
    return console.get_line_buffer()

def read_init_file(filename):
    console.read_init_file(filename)
    pass

def read_history_file(filename="~/.ipython/jhistory"):
    console.read_history_file(filename)
    pass
    
def write_history_file(filename="~/.ipython/jhistory"):
    console.write_history_file(filename)
    pass
        
def clear_history():
    console.clearHistory()
    pass
    
def get_current_history_length():
    return console.get_current_history_length()

def get_history_item(index):
    return console.get_history_item(index)
        
def set_completer(function=None):
    console.set_completer(function)
    pass
    
def get_completer():
    return console.get_completer()

def set_completer_delims(string):
    console.set_completer_delims(string)
    pass

def get_completer_delims():
    return console.get_completer_delims()

def add_history(line):
    console.add_history(line)
    pass

def get_completion_type():
    return console.get_completion_type()

def get_begidx():
    return console.get_begidx()

def get_endidx():
    return console.get_endidx()

def redisplay():
    console.redisplay()
    pass

def get_history_length():
    return console.get_history_length()

def set_history_length(length):
    console.set_history_length(length)
    pass

def set_completion_display_matches_hook(function=None):
    console.set_completion_display_matches_hook(function)
    pass

def remove_history_item(pos):
    console.remove_history_item(pos)
    pass

def replace_history_item(pos, line):
    console.replace_history_item(pos, line)
    pass
    
def insert_text(string):
    conosole.insert_text(string)
    pass

def set_pre_input_hook(function=None):
    console.set_pre_input_hook(function)
    pass
    
def set_startup_hook(function=None):
    console.set_startup_hook(function)
    pass
