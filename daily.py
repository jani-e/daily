import subprocess
import webbrowser
import time

program_paths = [
    r'C:\Program Files\Mozilla Thunderbird\thunderbird.exe',
    r'C:\Users\janie\AppData\Local\Discord\Update.exe --processStart Discord.exe'
]

website_urls = [
    r'https://www.is.fi',
    r'https://www.facebook.com',
    r'https://www.youtube.com',
    r'https://sahko.tk/'
]

def start_programs():
    for path in program_paths:
        try:
            subprocess.Popen(
                path, 
                shell=True, 
                startupinfo=subprocess.STARTUPINFO(), 
                creationflags=subprocess.CREATE_NO_WINDOW
                )
            print(f'Started: {path}')
        except Exception as e:
            print(f'Error starting {path}:\n{e}')

def start_browser_with_urls():
    for url in website_urls:
        try:
            webbrowser.open_new_tab(url)
            print(f'Started: {url}')
        except webbrowser.Error as e:
            print(f'Error starting {url}:\n{e}')

def user_inputs():
    valid_commands = ['0', '1', '2']
    print('0 - Start all')
    print('1 - Start programs')
    print('2 - Start websites in browser')
    print('Any other key to close.')
    command = input()
    if command in valid_commands:
        if command == '0':
            start_programs()
            start_browser_with_urls()
        elif command == '1':
            start_programs()
        elif command == '2':
            start_browser_with_urls()
            input('over')

def close_program():
    t = 5
    while t: 
        mins, secs = divmod(t, 60) 
        timer = '{:02d}:{:02d}'.format(mins, secs) 
        print('Closing...',timer, end="\r") 
        time.sleep(1) 
        t -= 1

if __name__ == '__main__':
    user_inputs()
    close_program()