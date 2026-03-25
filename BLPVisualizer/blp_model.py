


LEVELS = ["U", "C", "S", "TS"]
LEVEL_NAMES = {
    "U": "Unclassified",
    "C": "Classified",
    "S": "Secrete",
    "TS": "Top Secret"
}

def level_rank(level):
    return LEVELS.index(level)

class Subject:
    def __init__(self, name, max_level, start_level):
        self.name = name
        self.max_level = max_level
        self.curr_level = start_level

class Object:
    def __init__(self, name, level):
        self.name = name
        self.level = level

class BLPSystem:
    def __init__(self):
        self.subjects = {}
        self.objects = {}

    def add_subject():
        return
    
    def add_object():
        return
    
    def validate_levels():
        return
    
    def set_level():
        return
    
    def read():
        return
    
    def write():
        return
        
