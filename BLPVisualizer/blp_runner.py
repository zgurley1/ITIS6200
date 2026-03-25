from blp_model import BLPSystem


def build_sytem():
    sys = BLPSystem()

    sys.add_subject("Alice", max_level="S", start_level="U")
    sys.add_subject("Bob", max_level="C", start_level="C")
    sys.add_subject("Eve", max_level="U", start_level="U")

    sys.add_object("pub.txt", "U")
    sys.add_object("emails.txt", "C")
    sys.add_object("username.txt", "S")
    sys.add_object("password.txt", "TS")
    return sys


def run_case(number, description, actions):
    blp = build_sytem()
    blp.reset()
    print()
    print("=" * 60)
    print(f"Case {number}")
    print("=" * 60)

    print(f"Action:  {description}")
    blp.print_state()
    actions(blp)
    
def case1(blp):
    blp.read("Alice", "emails.txt")

def case2(blp):
    blp.read("Alice", "password.txt")

def case3(blp):
    blp.read("Eve", "pub.txt")

def case4(blp):
    blp.read("Eve", "emails.txt")

def case5(blp):
    blp.read("Bob", "password.txt")

def case6(blp):
    blp.read("Alice", "emails.txt")
    blp.write("Alice", "pub.txt")

def case7(blp):
    blp.read("Alice", "emails.txt")
    blp.write("Alice", "password.txt")

def case8(blp):
    blp.read("Alice", "emails.txt")
    blp.write("Alice", "emails.txt")
    blp.read("Alice", "username.txt")
    blp.write("Alice", "emails.txt")

def case9(blp):
    blp.read("Alice", "username.txt")
    blp.write("Alice", "emails.txt")
    blp.read("Alice", "password.txt")
    blp.write("Alice", "password.txt")

def case10(blp):
    blp.read("Alice", "pub.txt")
    blp.write("Alice", "emails.txt")
    blp.read("Bob", "emails.txt")

def case11(blp):
    blp.read("Alice", "pub.txt")
    blp.write("Alice", "username.txt")
    blp.read("Bob", "username.txt")

def case12(blp):
    blp.read("Alice", "pub.txt")
    blp.write("Alice", "password.txt")
    blp.read("Bob", "password.txt")

def case13(blp):
    blp.read("Alice", "pub.txt")
    blp.write("Alice", "emails.txt")
    blp.read("Eve", "emails.txt")

def case14(blp):
    blp.read("Alice", "emails.txt")
    blp.write("Alice", "pub.txt")
    blp.read("Eve", "pub.txt")

def case15(blp):
    blp.set_level("Alice", "S")
    blp.read("Alice", "username.txt")

def case16(blp):
    blp.read("Alice", "emails.txt")
    blp.set_level("Alice", "U")
    blp.write("Alice", "pub.txt")
    blp.read("Eve", "pub.txt")

def case17(blp):
    blp.read("Alice", "username.txt")
    blp.set_level("Alice", "C")
    blp.write("Alice", "emails.txt")
    blp.read("Eve", "emails.txt")

def case18(blp):
    blp.read("Eve", "pub.txt")
    blp.read("Eve", "emails.txt")



if __name__ == "__main__":
    cases = [
        (1,  "Alice reads emails.txt", case1),
        (2,  "Alice reads password.txt", case2),
        (3,  "Eve reads pub.txt",  case3),
        (4,  "Eve reads emails.txt", case4),
        (5,  "Bob reads password.txt", case5),
        (6,  "Alice reads emails.txt then writes to pub.txt",  case6),
        (7,  "Alice reads emails.txt then writes to password.txt", case7),
        (8,  "Alice reads/writes emails.txt; reads username.txt; writes emails.txt", case8),
        (9,  "Alice reads username.txt, writes emails.txt, reads/writes password.txt", case9),
        (10, "Alice reads pub.txt, writes emails.txt; Bob reads emails.txt", case10),
        (11, "Alice reads pub.txt, writes username.txt; Bob reads username.txt", case11),
        (12, "Alice reads pub.txt, writes password.txt; Bob reads password.txt", case12),
        (13, "Alice reads pub.txt, writes emails.txt; Eve reads emails.txt", case13),
        (14, "Alice reads emails.txt, writes pub.txt; Eve reads pub.txt", case14),
        (15, "Alice sets level to S then reads username.txt", case15),
        (16, "Alice reads emails.txt, sets level to U, writes pub.txt; Eve reads pub.txt", case16),
        (17, "Alice reads username.txt, sets level to C, writes emails.txt; Eve reads emails.txt", case17),
        (18, "Eve reads pub.txt then reads emails.txt", case18),
    ]

    print(f"=" * 60)
    print(" Bell-LaPadula (BLP) Simulator CLI")
    print(f"=" * 60)


    for number, description, fn in cases:
        run_case(number, description, fn)