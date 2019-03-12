# import json
import os
import subprocess as sbp
import subprocess
import convert_json as cjson
import copy_file as cp
import manage_files


home_directory = '/home/developer'
path_models = '/REPOSITORIES/Bank_Models'
dmc_mdl = '/REPOSITORIES/NSCGLE_Theory/CudaTemplate'


'''
    Ejecuta el proceso de esferas duras para un determinado usuario,
    esto es porque la ejecucion genera archivos que tienen
    que ir destinados a un determinado usuario.
'''


def exe_hard_sphere(user_name, fv):
    mdl = '/01Hard_Spheere'
    pth1 = home_directory + path_models + '/01Sk_HSphere/Benny_Version'
    pth = os.chdir(pth1)
    pth = os.getcwd()
    pcs = sbp.Popen([pth + mdl, fv.strip()], stdout=sbp.PIPE, stderr=sbp.PIPE)
    
    out, error = pcs.communicate()
    if out:
        print('OK', out)
    if error:
        print('Error', error.strip())
        return ':('
    if not pcs.poll():
        print("Program hard_sphere execute finish")
        
    out_pt = home_directory + '/Web_Site/' + user_name + '/Esfera_Dura'
    f_out = 'SKhard_sphere'
    d_store = '/data/sk_HSpheere.dat'
    out_data = cp.copy_files_by_user(pth1 + d_store, out_pt, f_out)
    
    generates_picture(out_data)
    return cjson.cvrt_fle_to_json(pth1 + d_store)
    
    # with open('sk_HSpheere.json') as json_data:
    #     d = json.load(json_data)
    # return d


'''
    Ejecuta el proceso de esferas suaves para un determinado usuario,
    esto es porque la ejecucion genera archivos que tienen
    que ir destinados a un determinado usuario.
'''


def exe_soft_sphere(usr_nme, fv, it):
    
    mdl = '/02SSphere'
    pth1 = home_directory + path_models + '/02SK_Soft_Sphere'
    ph = os.chdir(pth1)
    ph = os.getcwd()
    it = it.strip()
    fv = fv.strip()
    print('initial tempeture = ',it)
    print('fraction vol = ', fv)
    pcs = sbp.Popen([ph + mdl, fv, it], stdout=sbp.PIPE, stderr=sbp.PIPE)
    out, error = pcs.communicate()

    if out:
        print('OK', out)
    if error:
        print('Error', error.strip())
        return ':('
    if not pcs.poll():
        print("Program soft_sphere execute finish")

    out_pt = home_directory + '/Web_Site/' + usr_nme + '/Esfera_Suave'
    f_out = 'SKsoft_sphere'
    d_store = '/data/sk_SSphere.dat'
    out_data = cp.copy_files_by_user(pth1 + d_store, out_pt, f_out)

    generates_picture(out_data)
    cjson.cvrt_fle_to_json(pth1 + d_store)
    # cjson.convert_file_to_json(pth1 + d_store, out_pt)
    # with open('sk_SSphere.json') as json_data:
    #     d = json.load(json_data)
    # return d


def exe_Yukawa(usr_nme, fv, it):
    mdl = '/03Yuk'
    pt1 = home_directory + path_models + '/03SK-Yukawa_HardS'
    pth = os.chdir(pt1)
    pth = os.getcwd()

    fv = fv.strip()
    it = it.strip()
    
    pcs = sbp.Popen([pth + mdl, fv, it], stdout=sbp.PIPE, stderr=sbp.PIPE)
    out, error = pcs.communicate()
    
    if out:
        print('OK', out)
    if error:
        print('Error', error.strip())
        return ':('
    if not pcs.poll():
        print("Program Yukawa execute finish")

    out_pt = home_directory + '/Web_Site/' + usr_nme + '/Yukawa'
    f_out = 'SK_Yukawa'
    d_store = '/data/sk_MonoYuk.dat'
    out_data = cp.copy_files_by_user(pt1 + d_store, out_pt, f_out)
    
    generates_picture(out_data)
    return cjson.cvrt_fle_to_json(pt1 + d_store)

    # cjson.convert_file_to_json(pt1 + d_store, out_pt)
    # with open('sk_MonoYuk.json') as json_data:
    #     d = json.load(json_data)
    # return d


def exe_dynamic_mdle(usr_nme, fv):
    pt1 = home_directory + dmc_mdl
    pth = os.chdir(pt1)
    pth = os.getcwd()

    fv = fv.strip()
    pcs = sbp.Popen([pth + '/a.out', fv], stdout=sbp.PIPE, stderr=sbp.PIPE)
    out, error = pcs.communicate()
    
    if out:
        print('OK', out)
    if error:
        print('Error', error.strip())
        return ':('
    if not pcs.poll():
        print("Program Dynamic Module execute finish")

    out_pt = home_directory + '/Web_Site/' + usr_nme
    out_pt = out_pt + '/Dinamico/' + cp.get_date()

    manage_files.create_directory_on_path(out_pt)
    cp.copy_files_by_user(pt1 + '/coeficiente.dat', out_pt, 'Coeficiente')
    cp.copy_files_by_user(pt1 + '/delta_z.dat', out_pt, 'DeltaZ')
    cp.copy_files_by_user(pt1 + '/fcol.dat', out_pt, 'FCol')
    cp.copy_files_by_user(pt1 + '/fself.dat', out_pt, 'Fself')
    cp.copy_files_by_user(pt1 + '/sk.dat', out_pt, 'SK')
    
    return cjson.cvrt_fle_to_json(pt1 + '/sk.dat')


def gen_pict(source_path):
    # Se genera un arreglo a partir de la ruta
    split_path = source_path.split('/')
    directory_work = ''
    # Se obtiene el nombre del archivo en cuestion.
    name_file = split_path[len(split_path) - 1]
    # Obtenemos lá ruta del archivo para movernos a ese contexto.
    for i in range(len(split_path) - 1):
        directory_work = directory_work + split_path[i] + '/'
    # Se cambia de contexto la ejecucion del programa.
    os.chdir(directory_work)
    os.getcwd()
    # Se ejecuta el procceso que genera el grafico de los datos
    # gnuplot -e "set title 'Factor de Estructura'; set xlabel 'K'; set ylabel 'S(k)';  set terminal png size 1024,768; set output 'xyz.png'; plot '/home/delcracnk/REPOSITORIES/Bank_Models/01Sk_HSphere/Benny_Version/data/sk_HSpheere.dat' notitle"
    arg = 'set title \'Factor de Estructura\'; set xlabel \'K\';'

    arg = arg + 'set ylabel \'S(k)\';'
    arg = arg + 'set terminal png size 1024,768;'
    arg = arg + 'set output \'' + name_file
    arg = arg + '.png\'; ' + 'plot \''
    arg = arg + source_path + '\' notitle'
    
    pcs = sbp.Popen(['gnuplot', '-e', arg], stdout=sbp.PIPE, stderr=sbp.PIPE)

    out, error = pcs.communicate()

    if out:
        print('OK', out)
    if error:
        print('Error', error.strip())
        return ':('
    if not pcs.poll():
        print("Program fort plot finish")
        
    return directory_work + name_file + '.png'







def generates_picture(source_path):
    #Se genera un arreglo a partir de la ruta.
    split_path  = source_path.split('/') # 
    directory_work = ''
    # Se obtiene el nombre del archivo en cuestion.
    name_file = split_path[len(split_path) - 1]
    # Obtenemos lá ruta del archivo para movernos a ese contexto.
    for i in range (len(split_path)- 1):
        directory_work = directory_work + split_path[i] + '/'
    # Se cambia de contexto la ejecucion del programa.
    os.chdir(directory_work)
    os.getcwd()
    # Se ejecuta el procceso que genera el grafico de los datos
    
    # gnuplot -e "set title 'Factor de Estructura'; set xlabel 'K'; set ylabel 'S(k)';  set terminal png size 1024,768; set output 'xyz.png'; plot '/home/delcracnk/REPOSITORIES/Bank_Models/01Sk_HSphere/Benny_Version/data/sk_HSpheere.dat' notitle" 
    arguments = 'set title \'Factor de Estructura\'; set xlabel \'K\'; set ylabel \'S(k)\';  set terminal png size 1024,768; set output \''+ name_file + '.png\'; ' + 'plot \'' + source_path + '\' notitle' 

    process_plot = subprocess.Popen(['gnuplot','-e',arguments], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # process_plot = subprocess.Popen(['grace', source_path, '-hdevice', 'PNG', '-hardcopy', '-printfile',name_file + '.ps'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, error = process_plot.communicate()


    if out:
        print('OK', out)
    if error:
        print('Error', error.strip())
        return ':('
    if not process_plot.poll():
        print("Program fort plot finish")
    return directory_work +  name_file + '.png'
    


if __name__ == "__main__":
    # exe_hard_sphere_by_user('daniela', '0.4')
    # exe_Yukawa_by_user('alexlara', '0.3', '0.3')
    # exe_dynamic_module('andes204', '0.2')
    generates_picture('/home/yo/Web_Site/andes204/Esfera_Dura/SKhard_sphere_Date:2018-4-17-Time:13-21.dat')
    # my_list = ['p','r','o','g','r','a','m','i','z']
    # # elements 3rd to 5th
    # print(my_list[2:])


