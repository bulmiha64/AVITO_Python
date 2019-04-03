def ask_question(question, answers=('yes', 'no')):
    print(question)
    print('Choose your destiny:')
    if len(answers) == 2:
        print(answers[0] + ' or ' + answers[1])
    else:
        for a in answers:
            print(a, end=' ')
        print()
    a = input()
    try:
        answer = answers.index(a)
    except:
        print('Wrong answer')
        return ask_question(question, answers)
    return answer


def start():
    a = ask_question("You've bought a new laptop\nWhich OS should you install?",
                     ('Arch linux', 'Debian', 'Windows', 'macOS'))
    if a == 2:
        win()
    elif a == 3:
        mac()
    elif a == 0:
        arch()
    else:
        deb()


def arch():
    a = ask_question('Will you read the install guide?')
    if a == 0:
        arch_guide()
    else:
        arch_noguide()


def deb():
    print('Nice and simple, but a bit old')
    de_pick()


def arch_guide():
    print('You were succesful with basic arch install')
    de_pick()


def de_pick():
    a = ask_question('Time to pick your DE', ('KDE', 'XFCE', 'LXDE', 'Gnome', 'Deepin'))
    if a == 0:
        print('Nice pick')
        theme()
    elif a == 1:
        print('Looks kinda ugly but runs fast, not bad')
    elif a == 2:
        if ask_question('Are you from 2002?') == 0:
            print("Then it's fine I guess")
        else:
            print("What are you thinking?")
    elif a == 3:
        print('Nice and clean')
        theme()
    else:
        print('Say hello to the Chinese government for me')
        theme()


def arch_noguide():
    print("You've tried so hard but didnt get past the user profile setup\nBetter luck next time")


def win():
    print('Шindows must die')


def mac():
    print('Apple lawyers are on their way\nGame over')


def theme():
    if ask_question('Theme?', ('Light', 'Dark')) == 0:
        print('Light it is')
    else:
        print('Dark is cool, nice pick')


if __name__ == '__main__':
    start()
