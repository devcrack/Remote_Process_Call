from shutil import copyfile
import os
from datetime import datetime, date, time

# path = '/home/deve/REPOSITORIES/Bank_Models/01Sk_HSphere/Benny_Version/data/sk_HSpheere.dat'

def copy_files(path):
    os.chdir('/home/developer/REPOSITORIES/api_rest_example_Python')
    copyfile(path, './SKhard_sphere.dat')

def copy_files_by_user( source_path, user_path, name_file):
    os.chdir(user_path)
    copyfile(source_path, './' +  name_file +'-'+ get_date() + '.dat')

    return user_path + '/'+  name_file +'-'+ get_date() + '.dat'

def get_date():
    now = datetime.now()
    current_date = 'Date:' + str(now.year)  + '-'+ str(now.month)  + '-' + str(now.day) + '-' + 'Time:'+ str(now.hour) + '-' + str(now.minute) + '-'+ str(now.second)
    return current_date
 
if __name__ == "__main__":
    copy_files_by_user('/home/developer/REPOSITORIES/Bank_Models/01Sk_HSphere/Benny_Version/data/sk_HSpheere.dat', '/home/deve/Web_Site/chuyetin/Esfera_Dura')
    # now = datetime.now()

    # print('Year:' + str(now.year)  + '\n')
    # print('Month:' + str(now.month) + '\n')
    # print('Day:' + str(now.day)   + '\n')
