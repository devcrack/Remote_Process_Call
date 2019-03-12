import os
import errno
import pathlib


def create_directory(path_name):
    # Esta ruta esta sujeta a modificaciones varia dependiendo
    # el servidor en el que dicho directorio se aloje.
    real_path_name = '/home/developer/Web_Site/'                                
    directories = ['Esfera_Dura', 'Esfera_Suave', 'Yukawa', 'Dinamico']
    print(directories)

    real_path_name = real_path_name + path_name

    try:
        os.makedirs(real_path_name)
        for a_directory in directories:
            if not os.path.exists(real_path_name + '/' + a_directory):
                os.makedirs(real_path_name + '/' + a_directory)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


'''
    Lista todos los archivos de un determinado usuario
'''


def list_files_directory_user(user_name):
    # Esta ruta esta sujeta a modificaciones varia dependiendo el
    # servidor en el que dicho directorio se aloje.
    real_path_name = '/home/developer/Web_Site/'
    # directories = ['Esfera_Dura', 'Esfera_Suave', 'Yukawa', 'Dinamico']
    # Dentro de si contendra otro diccionario.
    data = {}
    data[user_name] = {}
    real_path_name = real_path_name + user_name
    # Abriendo el directorio del usuario
    current_directory = pathlib.Path(real_path_name)
    ptr_data = data[user_name]
    for directories_inside in current_directory.iterdir():
        ptr_data[directories_inside.name] = []
        # Abriendo cada archivo dentro de los
        # directorios que estan dentro del directorio de usuario.
        current_directory_nested = pathlib.Path(directories_inside)
        for files_in_directory in current_directory_nested.iterdir():
            ptr_data[directories_inside.name].append(files_in_directory.name)
        ptr_data[directories_inside.name].sort()
    return data
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
    Descarga un Archivo de un determinado directorio de un determinado usuario
'''


def ret_path(user_name, sign_model, file_name, subfolder):
    # switch_model = {
    #     0: 'Esfera_Dura',
    #     1: 'Esfera_Suave',
    #     2: 'Yukawa',
    #     3: 'Dinamico'
    # }
    # switch_model.get(sign_model)
    path_download = '/home/developer/Web_Site/' + user_name + '/' + sign_model 
    if subfolder == '\0':
        path_download += '/' + file_name
    else:
        path_download += '/' + subfolder + '/' + file_name
    return path_download
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
    Descarga un Archivo de un determinado directorio de un determinado usuario
'''


def get_files_by_user_by_directory(user_name, current_work):
    # Esta ruta esta sujeta a modificaciones varia dependiendo
    # el servidor en el que dicho directorio se aloje.
    base_path = '/home/developer/Web_Site/' + user_name + '/' + current_work
    data = {}
    data[current_work] = []
    # Obtenemos la lista de archivos que se encuentran en el directorio. 
    current_directory = pathlib.Path(base_path)

    for files_in_directory in current_directory.iterdir():
        # Agregamos el archivo al directorio
        data[current_work].append(files_in_directory.name)
    # Ordenamos la lista dentro del diccionario
    data[current_work].sort()
    return data

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


'''
    Crea un directorio en la ruta especificada.
'''


def create_directory_on_path(source_path):
    try:
        os.makedirs(source_path)                      
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

# --------------------------------------------------------------------------------------------------------------------------------


def get_directory_content(directory_path):
    
    '''Obtiene el contenido de un determinado directorio
        
    Args:
         directory_path:      Ruta absoluta del directorio que se quiere leer.
    '''
    
    split_name_path = directory_path.split('/')
    name_directory = split_name_path[len(split_name_path)-1]
    data = {}
    
    data[name_directory] = []
    # Obtenemos la lista de archivos que se encuentran en el directorio. 
    current_directory = pathlib.Path(directory_path)

    for files_in_directory in current_directory.iterdir():
        # Agregamos el archivo al directorio
        data[name_directory].append(files_in_directory.name) 
        # Ordenamos la lista dentro del diccionario
        data[name_directory].sort()
    return data


if __name__ == "__main__":
    # list_files_directory_user('daniela')
    # create_directory('chuyetin')
    get_directory_content('/home/devrack/Web_Site/andes204/Esfera_Dura')
