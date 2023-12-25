import wmi, os
fwmi = wmi.WMI()

seeproc = []
allproc = []

# Whitelist maker if isnt exist
if not os.path.exists('whitelist.txt'):
    whfile = open('whitelist.txt', 'x')
    whfile.close()

# - - - - - - - - - - - - -
# D E F   F U N C T I O N S
# - - - - - - - - - - - - -

# Shows whitelist
def seewh():
    # Check whitelist file
    whfile = open('whitelist.txt').readlines()
    whitelist = [line.rstrip() for line in whfile]
    output = '\n'.join(whitelist)
    return output

# Process checker
def seeall():
    for process in fwmi.Win32_Process():
        seeproc.append(f" PID - {process.ProcessId} | ИМЯ - {process.Name}")
        allproc.append(f"{process.Name}")
    output = '\n'.join(seeproc)
    return output

# Shows process if proc not on whitelist
def seenotwh():
    for process in fwmi.Win32_Process():
        allproc.append(f"{process.Name}")
    # Check whitelist file
    whfile = open('whitelist.txt').readlines()
    whitelist = [line.rstrip() for line in whfile]
    # Search processes not in whitelist
    notwhite = [item for item in allproc if item not in whitelist]
    output = '\n'.join(notwhite)
    return output

# Main menu
def main():
    os.system('cls')
    print("""
 + ------------------------------------- +
 |     P R O C E S S   F I L T E R       |
 + ------------------------------------- +
 |                                       |
 |   [1] - Показать процессы             |
 |   [2] - Показать белый список         |
 |   [3] - Найти процесс не в б.с.       |
 |   [4] - Выйти                         |
 |                                       |
 + ------------------------------------- +
    """)
    put = input('<PF/Ввод> ')
    if put == '1':
        os.system('cls')
        print('----={ Список процессов }=----')
        print(seeall())
        input('Enter - назад')
    elif put == '2':
        os.system('cls')
        print('----={ Белый список }=----')
        print(seewh())
        input('Enter - назад')
    elif put == '3':
        os.system('cls')
        print('----={ Не в белом списке }=----')
        print(seenotwh())
        input('Enter - назад')
    elif put == '4':
        exit()
    main()
main()

    
    
