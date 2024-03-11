import os

# Color definitions with RGB values
green_rgb = (0, 255, 0)  # RGB values for green
red_rgb = (255, 0, 0)    # RGB values for red
blue_rgb = (255, 255, 0)  # RGB values for #F0FFFF

green = '\033[38;2;{};{};{}m'.format(*green_rgb)  # Green
red = '\033[38;2;{};{};{}m'.format(*red_rgb)    # Red
blue = '\033[38;2;{};{};{}m'.format(*blue_rgb)   # Blue

# Define marker here
marker = green + "[" + red + "+" + green + "]" + blue

# Rest of the code remains the same...

def print_colored_text(text):
    colored_text = ""
    for char in text:
        if char == '[' or char == ']':
            colored_text += blue + char  # Blue
        elif char == '+':
            colored_text += red + char    # Red
        else:
            colored_text += blue + char  # Blue
    print(colored_text)

def print_banner():
    banner = """
    ____             _       _       _       
   / ___|  ___   ___| | ____| | ___ | |_ ___ 
   \___ \ / _ \ / __| |/ / _` |/ _ \| __/ __|
    ___) | (_) | (__|   < (_| | (_) | |_\__ \\
   |____/ \___/ \___|_|\_\__,_|\___/ \__|___/
                                              
    """
    print(banner)

def main():
    print_colored_text("Starting Package Manager...".format(marker=marker))
    print_banner()

    sudo_choice = input(blue + "{marker} Do you want to use sudo? (y/n): ".format(marker=marker))

    if sudo_choice.lower() == 'y':
        sudo = 'sudo '
    else:
        use_sudo = input(blue + "{marker} Do you want to use sudo? (y/n): ".format(marker=marker))
        sudo = 'sudo ' if use_sudo.lower() == 'y' else ''

    os_choice = input(blue + "{marker} Which operating system are you using? (Termux/Ubuntu/Debian/Arch/Fedora): ".format(marker=marker))
    package_manager = ''

    if os_choice.lower() == 'termux':
        package_manager = 'pkg'
    elif os_choice.lower() in ['ubuntu', 'debian']:
        package_manager = 'apt'
    elif os_choice.lower() == 'arch':
        package_manager = 'pacman'
    elif os_choice.lower() == 'fedora':
        package_manager = 'dnf'

    action_choice = input(blue + "{marker} Do you want to search/install (s/i): ".format(marker=marker))

    if action_choice.lower() == 'i':
        package_action = 'install'
    elif action_choice.lower() == 's':
        package_action = 'search'

    package_name = input(blue + "{marker} Which package do you want to {action}: ".format(marker=marker, action=package_action))

    if package_action == 'install':
        command = sudo + package_manager + ' ' + package_action + ' ' + package_name
    elif package_action == 'search':
        command = sudo + package_manager + ' ' + package_action + ' ' + package_name

    print_colored_text("{marker} Executing command: ".format(marker=marker) + command)
    os.system(command)
    print_colored_text("{marker} Thanks for using!".format(marker=marker))

if __name__ == "__main__":
    main()
