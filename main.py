import os
import time
# Firstly you enter a file folder location!
while True:
    print('1.Create new file')
    print('2.Delete file')
    print("3.Update file")
    print("4.No of file")
    print('5.Read file')
    print('6.Exit')
    try:
        no = input('Enter a num: ')
        if '1' in no:
            filename = str(input('Enter a flie name:'))
            contant = str(input('Enter a file contant: '))
            file = open(f'Enter a location\ {filename}','w')
            file.write(contant)
            file.close()
            print('------------File is created!---------------')
        
        
        if '2' in no:
            try:
                filename = str(input('Enter a file name: '))
                os.remove(f'Enter a location\ {filename}')
                print('------------File has been deleted!---------------')
            except FileNotFoundError() as e:
                print(e)
                
            except:
                print('There is an error!')
                
                
                
        if '3' in no:
            try:
                filename = str(input('Enter a file name: '))
                contant  = str(input('Enter a file contant: '))
                file = open(f'Enter a location\ {filename}', 'w')
                file.write(contant)
                file.close()
                print('------------File has been updated!---------------')
            except FileNotFoundError() as e:
                print(e)
            except:
                print('There is an error!')
                
                
        if "4" in no:
            ha = os.listdir('Enter a location')
            print(len(ha))
        
        if "5" in no:
            filename = input('Enter a file name: ')
            file = open(f'Enter a location\ {filename}','r')
            fa = file.read()
            print(fa)
            file.close()
            
        if "6" in no:
            print('-----Program is closing-------')
            time.sleep(1)
            break
    except:
        print('There is an error!')