#Importing modules
import xml.etree.ElementTree as et
import subprocess
import os
import shutil
import time


#Show connected wifi's to show password
def show_wifi():
        print("Enter the number corresponding  to the password from the list:")
        x = subprocess.check_output('netsh wlan show profile', shell=True, encoding='utf8')
        x = x.split('\n')
        wifi = []
        for i in x:
                if '    All User Profile     : ' in i:
                        wifi.append(i[27:])
        c = 1
        for i in wifi:
               print(c, i)
               c += 1
        return wifi




#manages input
def inp():
        while True:
                print()
                num = input('Enter the number: ')
                try:
                        if num.isdigit:
                                num = int(num)
                                if num != 0:
                                        if len(wifi) >= num:
                                                break
                                        else:
                                                print('Invalid Input!')
                                else:
                                        print('Invalid Input!')
                        else:
                                print('Invalid Input!')
                except:
                        print('Invalid Input!')
                                
        return num


#shows password
def show_pass(func):
        global wi
        wi = wifi[func - 1]
        search = 'pwd\Wi-Fi-' + wi + '.xml'
        mytree = et.parse(search)
        myroot = mytree.getroot()
        if myroot[4].tag == '{http://www.microsoft.com/networking/WLAN/profile/v1}MSM':
                pw = myroot[4][0][1][2].text
        else:
                pw = myroot[5][0][1][2].text
        return pw


try:
        os.mkdir('pwd')
        subprocess.run('netsh wlan export profile folder = pwd key=clear', shell=True)
        wifi = show_wifi()
        func = inp()
        pw = show_pass(func)
        print('\n', 'The password of', wi, ':', pw)
        while True:
                ask = input("Do you want to exit(y/n)? ")
                if ask.lower() == 'n':
                        subprocess.run('netsh wlan export profile folder = pwd key=clear', shell=True)
                        wifi = show_wifi()
                        func = inp()
                        pw = show_pass(func)
                        print('\n', 'The password of', wi, ':', pw)
                        continue
                elif ask.lower() == 'y':
                        time.sleep(1)
                        break
                else:
                        continue
except:
        print('Some error occured!')
finally:
        try:
                shutil.rmtree('pwd')
        except:
                pass
