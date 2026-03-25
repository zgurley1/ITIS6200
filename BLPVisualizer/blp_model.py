


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

    def add_subject(self, name, max_level, start_level):
        if level_rank(start_level) > level_rank(max_level):
            print(f" Cannot add subject '{name}': start {start_level} > max {max_level}.")
            return
        self.subjects[name] = Subject(name, max_level, start_level)

        
    
    def add_object(self, name, level):
        self.objects[name] = Object(name, level)
        
    
    def validate_levels(self, subject_name, object_name):
        subject = self.subjects[subject_name]
        object = self.objects[object_name]
        return level_rank(subject.curr_level) == level_rank(object.level)
    
    def set_level(self, subject_name, new_level):
        subject = self.subjects[subject_name]

        # Check that subject is not decreasing level
        if level_rank(new_level) < level_rank(subject.curr_level):
            print(f"Level not set, {subject_name} connot lower level from {subject.curr_level} to {new_level}")
            return False
        # Check that subject is not going above max level
        if level_rank(new_level) > level_rank(subject.max_level):
            print(f"Level not set, {subject_name} cannot raise level to {new_level}. Max clearance is {subject.max_level}.")
            return False
        

        print(f"LEVEL SET: {subject_name} is not {new_level}")
        subject.curr_level = new_level
        return True
    
    def read(self, subject_name, object_name):
        subject = self.subjects[subject_name]
        object = self.objects[object_name]

        subject_level = level_rank(subject.curr_level)
        object_level = level_rank(object.level)

        if subject_level > object_level:
            print(f"Read Granted: {subject_name} ({subject.curr_level}) reads {object_name} ({object.level})")
            return True
        
        if object_level <= level_rank(subject.max_level):
            print(f"Read Granted: {subject_name} auto-raised to {object.level} to read {object_name}.")
            subject.curr_level = object.level
            return True
        
        print(f"Read Denied: {subject_name} ({subject.curr_level}), max={subject.max_level}, cannot read {object_name} ({object.level})")
        return False
        
    
    def write(self, subject_name, object_name):
        subject = self.subjects[subject_name]
        object = self.objects[object_name]

        subject_level = level_rank(subject.curr_level)
        object_level = level_rank(object.level)

        if subject_level <= object_level:
            print(f"Write Granted: {subject_name} ({subject.curr_level}) writes to {object_name} ({object.level})")
            return True
        print(f"Write Denied: {subject_name} ({subject.curr_level}) does not have persmission to write to {object_name} ({object.level})")
        return False
    



    def print_state(self):
        print("\n  === Current Access Levels ===")
        for name, s in self.subjects.items():
            print(f"    [Subject] {name:6s}: current={s.curr_level}, max={s.max_level}")
        
        for name, o in self.objects.items():
            print(f"    [Object] {name:6s}: current={o.level}") 
        print("=" * 32)
        print()

    def reset(self):
        defaults = {
            "Alice": ("S", "U"),
            "Bob":   ("C", "C"),
            "Eve":   ("U", "U"),
        }
        for name, (max_lvl, start_lvl) in defaults.items():
            self.subjects[name].max_level  = max_lvl
            self.subjects[name].curr_level = start_lvl
        
