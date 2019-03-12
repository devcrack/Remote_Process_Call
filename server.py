#  ***********TODO ESTO HAY QUE REFACTORIZARLO****************
from flask import Flask
from flask_restful import Resource, Api
from flask import jsonify
from flask import send_file
import spawn_process
import manage_files

home_directory = '/home/developer'
# Importa la capsula de c++
# import hola
# import example

# Variable predifinida de python. Esto simplemente es una instancia de Flask.
app = Flask(__name__)
# http://flask-restful.readthedocs.io/en/latest/api.html#flask_restful.Api
api = Api(app)
# Prueba del API REST y la capsula en C++


class Saludo(Resource):
    def get(self, nombre):
        result = {'saludo': hola.Saluda(nombre)}
        return jsonify(result)


# --------------------------------------------------------------------------------------------------------------------------------
'''
    Prueba #2 de API REST
    Solo multiplica 2 numeros, dichos numeros son los parametros entrates.
 '''


class Mult(Resource):
    def get(self, num1, num2):
        result = {'res': example.Suma(int(num1), int(num2))}
        return jsonify(result)


# --------------------------------------------------------------------------------------------------------------------------------
'''Ejecuta el proceso para el calculo de Esfera Dura
frac_vol: Este parametro viene en la URL es la fraccion de
'''


class execute_hard_sphere(Resource):
    def get(self, user_name, frac_vol):
        # return spawn_process.exe_hard_sphere(frac_vol)
        print(user_name, frac_vol)
        return spawn_process.exe_hard_sphere(user_name, frac_vol)
# --------------------------------------------------------------------------------------------------------------------------------


# -------------------------------------------------------------------1-------------------------------------------------------------
'''
    Genera el recurso para la descarga del archivo generado por la ejecucion
    MODIFICAR
'''


class hard_sphere_download_file(Resource):
    
    def get(self, usr_nme, fle_nme):

        path = manage_files.ret_path(usr_nme, 'Esfera_Dura', fle_nme, '\0')
        split_path = path.split('/')
        nme = split_path[len(split_path) - 1]
        
        return send_file(path, attachment_filename=nme)
# --------------------------------------------------------------------------------------------------------------------------------


# --------------------------------------------------------------------------------------------------------------------------------
'''
   Peticion al API para crear el directorio de un usuario.
   MODIFICAR
'''


class create_directory(Resource):
    def get(self, user_name):
        manage_files.create_directory(user_name)
        return 'succees'
# --------------------------------------------------------------------------------------------------------------------------------


# --------------------------------------------------------------------------------------------------------------------------------
'''
    Obtiene los archivos de un determinado directorio
    de un determinado Usuario
'''


class list_user_files(Resource):
    def get(self, user_name):
        return jsonify(manage_files.list_files_directory_user(user_name))
# --------------------------------------------------------------------------------------------------------------------------------


# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
    Ejecuta el proceso para el calculo de Esfera Suave
    frac_vol: Este parametro viene en la URL es la fraccion de volumen dada para el calculo del factor de estructura.

'''


class execute_soft_sphere(Resource):
    def get(self, user_name, frac_vol, ini_t):
        data = spawn_process.exe_soft_sphere(user_name, frac_vol, ini_t)
        # data = spawn_process.exe_soft_sphere_by_user(user_name, frac_vol, ini_t)
        return data
# --------------------------------------------------------------------------------------------------------------------------------



# --------------------------------------------------------------------------------------------------------------------------------
'''
    Genera el recurso para la descarga del archivo generado por la ejecucion de esfera dura
    MODIFICAR
'''
class soft_sphere_download_file(Resource):
    def get(self, user_name, file_name):
        path_to_download = manage_files.ret_path(user_name, 'Esfera_Suave', file_name, '\0')
        split_path = path_to_download.split('/')

        return send_file(path_to_download, attachment_filename = split_path[len(split_path) - 1])

# --------------------------------------------------------------------------------------------------------------------------------


# --------------------------------------------------------------------------------------------------------------------------------
'''
Genera el recurso que obtiene los archivos de un determinado directorio de un determinado  Usuario
'''
class get_files_by_user_by_directory(Resource):
    def get(self, user_name, current_directory):
        path = home_directory+ '/Web_Site/' + user_name + '/' + current_directory
        return jsonify(manage_files.get_directory_content(path))
        # return jsonify(manage_files.get_files_by_user_by_directory(user_name, current_directory))
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

class execute_Yukawa_by_user(Resource):
    def get(self, user_name, frac_vol, ini_t):
        return spawn_process.exe_Yukawa(user_name, frac_vol, ini_t)
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


class Yukawa_download_file(Resource):
    '''
    Genera el recurso para la descarga del archivo generado
    por la ejecucion de esfera dura
    '''
    def get(self, user_name, file_name):
        path_to_download = manage_files.ret_path(user_name, 'Yukawa', file_name, '\0')
        split_path = path_to_download.split('/')
        return send_file(path_to_download, attachment_filename = split_path[len(split_path) - 1])


class Dynamic_Module_Process(Resource):
    def get(self, user_name, frac_vol):
        return spawn_process.exe_dynamic_mdle(user_name, frac_vol)

    
class Dynamic_Download_files(Resource):
    '''
    Permite la descarga de un archivo generado por el modulo dinamico.
    '''
    def get(self, usr_nme, subflder_nme, fle_nme):
        '''
        Args: 
                 user_name      :      Nombre del usuario que esta solicitando la descarga.
                 subfolder_name :      Nombre del subdirectorio del cual se requiere el archivo.
                 file_name      :      Nombre del archivo que se desea descargar.
        '''
        path_to_download = manage_files.ret_path(usr_nme, 'Dinamico', fle_nme, subflder_nme)
        split_path = path_to_download.split('/')
        return send_file(path_to_download, attachment_filename = split_path[len(split_path) - 1])

class Get_content_dynamic_module(Resource):
    '''
    Obtiene el contenido de los directorios generados por la ejecucion del modulo dinamico.
    '''
    def get(self, user_name, subfolder):
        '''
        Args:
             user_name:   Nombre de usuario desde el cual se esta haciendo la peticion del recurso.
             subfolder:   Nombre del subfolder del cual se desea obtener el contenido.
        '''
        return jsonify(manage_files.get_directory_content(manage_files.ret_path(user_name, 'Dinamico', subfolder,'\0')))


class get_hs_ss_yuk_picture(Resource):
    def get(self, user_name, model, name_file):
        path_to_download = spawn_process.generates_picture(manage_files.return_path_to_download(user_name, model, name_file, '\0'))
        split_path = path_to_download.split('/')

        return send_file(path_to_download, attachment_filename = split_path[len(split_path) - 1]) 


##################################################################################################################################
# HACIENDO PETICIONES AL API REST

# add_resource(resource, *urls, **kwargs)
# resource (Resource) – the class name of your resource
# Ruta de prueba 1


api.add_resource(Saludo, '/saludo/<nombre>')

# Ruta de prueba #2
api.add_resource(Mult, '/saludo/<num1>/<num2>')

link_exe_hard_sphere = '/exe_hard_sphere/<user_name>/<frac_vol>'
api.add_resource(execute_hard_sphere, link_exe_hard_sphere)
link_exe_soft_sphere = '/exe_soft_sphere/<user_name>/<frac_vol>/<ini_t>'
api.add_resource(execute_soft_sphere, link_exe_soft_sphere)
link_exe_yukawa = '/exe_Yukawa/<user_name>/<frac_vol>/<ini_t>'
api.add_resource(execute_Yukawa_by_user, link_exe_yukawa)
link_exe_dynamic_mod = '/exe_dynamic_module/<user_name>/<frac_vol>'
api.add_resource(Dynamic_Module_Process, link_exe_dynamic_mod)
# ----------------------------------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------------------------------
# Administrando descargas de archivos
link_down_file_hrd_sphre = '/download_file_hard_sphere/<usr_nme>/<fle_nme>'
api.add_resource(hard_sphere_download_file, link_down_file_hrd_sphre)
link_down_fle_soft_sphre = '/download_file_soft_sphere/<user_name>/<file_name>'
api.add_resource(soft_sphere_download_file, link_down_fle_soft_sphre)
link_down_file_yuk = '/download_file_Yukawa/<user_name>/<file_name>'
api.add_resource(Yukawa_download_file, link_down_file_yuk)
link_din_fle = '/download_fle_dyn_modl/<usr_nme>/<subflder_nme>/<fle_nme>'
api.add_resource(Dynamic_Download_files, link_din_fle)
# -----------------------------------------------------------------------------------------------------------

# Administrando directorios y Archivos
link_user_directory = '/user_directory/<user_name>'
api.add_resource(create_directory, link_user_directory)
link_user_simple_list_files = '/user_list_files/<user_name>'
api.add_resource(list_user_files, link_user_simple_list_files)
link_get_files = '/get_files/<user_name>/<current_directory>'
api.add_resource(get_files_by_user_by_directory, link_get_files)
link_files_dynamic_mdle = '/get_files_dynamic/<user_name>/<subfolder>'
api.add_resource(Get_content_dynamic_module, link_files_dynamic_mdle)
link_get_model_plot = '/get_model_plot/<user_name>/<model>/<name_file>'
api.add_resource(get_hs_ss_yuk_picture, link_get_model_plot)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5002, debug=True)

# gnuplot -e "set terminal png size 1024,768; set output 'xyz.png'; plot '/home/delcracnk/REPOSITORIES/Bank_Models/01Sk_HSphere/Benny_Version/data/sk_HSpheere.dat'"
# gnuplot -e "set terminal png size 1024,768; set output 'xyz.png'; plot '/home/delcracnk/REPOSITORIES/Bank_Models/01Sk_HSphere/Benny_Version/data/sk_HSpheere.dat' with lines"
