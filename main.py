from core import ui, parser, handleCMD

def manage_input():
    while True:
        dic = parser.parse(input(">> "))
        if dic == -1:
            continue
        msg = handleCMD.handle_cmd(dic)
        if not msg:
            continue
        print(msg)


def main():
    ui.welcome()
    manage_input()
        
main()