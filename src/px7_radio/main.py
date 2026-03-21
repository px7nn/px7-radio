from px7_radio.core import ui, parser, handleCMD

def manage_input():
    while True:
        cmd = parser.parse(input(">> "))
        if cmd == -1:
            exit()
        if not cmd:
            continue
        handleCMD.handle_cmd(cmd)
        


def main():
    ui.welcome()
    manage_input()
        