import os
import subprocess

def run_case(selected_option):
    if selected_option == '1':
        print("\nRunning: os.system('ls')")
        os.system('ls')
    elif selected_option == '2':
        print("\nRunning: subprocess.run(['ls', '-l'])")
        subprocess.run(['ls', '-l'])
    elif selected_option == '3':
        print("\nRunning: subprocess.run(['ls', '-l', 'README.md'])")
        subprocess.run(['ls', '-l', 'README.md'])
    elif selected_option == '4':
        command="uname"
        commandArgument="-a"
        print(f'\nGathering system information with command: {command} {commandArgument}')
        subprocess.run([command,commandArgument])
    elif selected_option == '5':    
        command="ps"
        commandArgument="-x"
        print(f'\nGathering active process information with command: {command} {commandArgument}')
        subprocess.run([command,commandArgument])        
    else:
        print("Invalid case")


os.system('clear')
selected_option = input('Type an option between 1 to 5: ')
run_case(selected_option)




