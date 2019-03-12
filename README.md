# Requerimientos
  - python3-venv    Para la creacion y el manejo de entornos virtuales.
  - python3-pip     Para la instalacion de los modulo python desde pypy.
  - libpq-dev       Utilidades de desarrollador para Python.  
  - python-dev      Utilidades de desarrollador para Python.
  - supervisor      Te permite monitorear y controlar los procesos en el sistema operativo.    

    Solamente hacer :
    ```
        sudo apt install python3-venv 
        sudo apt install python3-pip 
        sudo apt install libpq-dev 
        sudo apt install python-dev 
        sudo apt install supervisor
    ```
    O bien 
    ```
        sudo apt install python3-venv python3-pip libpq-dev python-dev supervisor
    ```

# Creando un entorno Virtual 

  Dentro del directorio del Proyecto crear el entorno virtual mediante el uso del comando 

```
  python3 -m venv "nombre_directorio_entorno_virtual
```

  Esto lo que hara es crear una copia Local de Python y pip en el directorio recien creado para el entorno virtual ("nombre_directorio_entorno_virtual")
  
  Antes de cualquier cosa es necesario activar el entorno virtual: 
  
```
  source <nombre_directorio_entorno_virtual>/bin/activate
```
  

# Estableciendo la Configuracion para el administrador de procesos(la applicacion Flask).
  
  Se tienen que instalar los paquetes(modulos python) :
  - gunicorn
  - flask
  - flask_restful
  - jsonify
  - setproctitle


  Para esto hacemos :

  ```
  pip install gunicorn flask flask_restful jsonify setproctitle
 ```
  y finalmente 
 
  ```
     pip install gunicorn[gevent]
  ```

# Configurando Gunicorn
  

  Como regla general NUM_WORKERS = (num_nucleos  * 2 ) + 1. La idea de esto es que en un algun momento dado la mitad de esos workers estaran realizando tareas I/O.

  Para saber el numero de procesadores que tiene el host ingresar el comando: ```nproc```.

  Para verificar que Gunicorn este funcionando correctamente con nuestra aplicacion Flask y el punto de entrada dado a Gunicorn(Se refiere al archivo "wsgi.py") usar el comando:

  ```
      gunicorn --workers=<NUM_WORKERS>  --worker-class gevent wsgi:app -b 0.0.0.0:5002
  ```

  Si todo salio bien, debera de generar una salida como esta: 
```
 [2018-08-22 20:36:46 -0500] [26124] [INFO] Starting gunicorn 19.9.0
 [2018-08-22 20:36:46 -0500] [26124] [INFO] Listening at: http://0.0.0.0:5002 (26124)
 [2018-08-22 20:36:46 -0500] [26124] [INFO] Using worker: gevent
 [2018-08-22 20:36:46 -0500] [26127] [INFO] Booting worker with pid: 26127
 [2018-08-22 20:36:46 -0500] [26128] [INFO] Booting worker with pid: 26128
 [2018-08-22 20:36:46 -0500] [26129] [INFO] Booting worker with pid: 26129
 [2018-08-22 20:36:46 -0500] [26131] [INFO] Booting worker with pid: 26131
 [2018-08-22 20:36:46 -0500] [26133] [INFO] Booting worker with pid: 26133
```


 Para matar el procesos de Gunicorn hacer : **Ctr + C**

 Ahora regresaremos al entorno global de Python, para esto tenemos que desactivar el entorno virtual. Para esto usar el comando 
 ```
    deactivate
 ```


Ahora se tiene que generar un script para hacer mas practico para que Gunicorn sirva nuestra aplicacion.

Crearemos nuestro archivo en la ruta /directorio_proyecto/directorio_entorno_virtual/bin/gunicorn_start.bash

```
#!/bin/bash

NAME="manage_process"                                    # Nombre de la aplicacion                         
FLASK_DIR=/home/<user_name>/<ruta_directorio_proyecto>   # Directorio del proyecto
USER=<nom_usuario>                                       # Nombre del usuario
GROUP=<algun_grupo>                                      # El grupo para el que correra el proceso
NUM_WORKERS=<algun_numero>                               # Numero de workers para que Gunicorn ejecute Procesos.
WORKER_CLASS=gevent                                      # Clase de worker 

echo "Starting $NAME as `whoami`"

# Activando el entorno Virtual
cd $FLASK_DIR                                            
source ./<entorno_virtual>/bin/activate      

# Iniciar aplicacion Flask con Gunicorn 
exec gunicorn --workers=$NUM_WORKERS  --worker-class $WORKER_CLASS wsgi:app -b 0.0.0.0:5002
```

Es necesario dar permisos a nuestro scrip recien creado

``` sudo chmod +x bin/gunicorn_start.bash```

Ahora podemos realizar una pruba de nuestro script

```
 ./gunicorn_start.bash
```

Si todo esta bien deberiamos de obtener una salida:

```
Starting manage_process as yo
[2018-08-29 15:47:20 -0500] [10889] [INFO] Starting gunicorn 19.9.0
[2018-08-29 15:47:20 -0500] [10889] [INFO] Listening at: http://0.0.0.0:5002 (10889)
[2018-08-29 15:47:20 -0500] [10889] [INFO] Using worker: gevent
[2018-08-29 15:47:20 -0500] [10893] [INFO] Booting worker with pid: 10893
[2018-08-29 15:47:20 -0500] [10894] [INFO] Booting worker with pid: 10894
[2018-08-29 15:47:20 -0500] [10896] [INFO] Booting worker with pid: 10896
[2018-08-29 15:47:20 -0500] [10897] [INFO] Booting worker with pid: 10897
[2018-08-29 15:47:21 -0500] [10913] [INFO] Booting worker with pid: 10913
[2018-08-29 15:47:21 -0500] [10915] [INFO] Booting worker with pid: 10915
[2018-08-29 15:47:21 -0500] [10917] [INFO] Booting worker with pid: 10917
[2018-08-29 15:47:21 -0500] [10918] [INFO] Booting worker with pid: 10918
```


# Iniciar y Monitorear la Aplicacion con supervisor

Es necesario asegurarse de que nuestro script se ejecute automaticamentey que ademas se reinicie automaticamente si por alguna razon dejase de funcionar. Ese tipo de tareas
son facilmente manejables con un servicio llamado supervisor.

Cuando supervisor esta instalado se puede controlar,  monitorear y ejecutar procesos  mediante la creacion de archivos que son alojados en el directorio ```/etc/supervisor/conf.d``` .
Para la aplicacion flask ```manage_process``` se creara el archivo ```/etc/supervisor/conf.d/manage_process.conf```
y le agregaremos el siguiente contenido:


```
[program:manage_process]
directory=/home/<user_name>/<ruta_directorio_proyecto>
command=/home/<user_name>/<ruta_directorio_proyecto>/<entorno_virtual>/bin/gunicorn_start.bash
autostart=true
autorestart=true
stderr_logfile=home/<user_name>/directorio_log_nuestra_aplicacion/log/manage_process/manage_process.err.log    ; Donde guardara los mensajes de error de nuestra aplicacion
stdout_logfile=home/<user_name>/directorio_log_nuestra_aplicacion/log/manage_process/manage_process.out.log

```

Se debe de crear el directorio log para nuestra aplicacion ya que si este no existiera nuestra aplicacion no se ejecutara por el error generado al realizar la verificacion
de la existencia de ese directorio.

Una vez realizado todo lo anterior se tiene que pedir a supervisor que vuelva a leer los archivos de configuracion y actulizar. (Ya que hemos agregado el archivo que supervisor registrara para iniciar la apliacion Flask).

```
sudo supervisorctl reread
process_manage: available
sudo supervisorctl update
process_manage: added process group
```

Se puede verificar el estado de la aplicacion Flask, iniciar, detener o reiniciar,  todo esto mediante supervisor.

```
sudo supervisorctl status process_manage                       
process_manage                            RUNNING    pid 18020, uptime 0:00:50
sudo supervisorctl stop process_manage  
process_manage: stopped
sudo supervisorctl start process_manage                        
process_manage: started
sudo supervisorctl restart process_manage 
process_manage: stopped
process_manage: started
```

La aplicacion Flask ahora deberia de iniciarse automaticamente despues de que el sistema se inicie y reiniciarse si por alguna razon falla.



