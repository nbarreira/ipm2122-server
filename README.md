# Instalación de Docker

## debian/ubuntu

- [ ] Instala docker (como superusuario)

```bash
apt-get install docker docker-compose
```

- [ ] Prueba la instalación de docker con tu usuario (no como superusuario!)

```
docker version
```

Deberá salir por pantalla información sobre la versión actualmente instalada.

> En caso de producirse un error de permisos como el siguiente:
>
> ```
> Got permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: Get http://%2Fvar%2Frun%2Fdocker.sock/v1.39/info: dial unix /var/run/docker.sock: connect: permission denied
> ```
>
> Conéctate como superusuario y añade a tu usuario al grupo docker:
>
> ```
> usermod -aG docker myuser
> ```
>
> donde *myuser* es tu nombre de usuario. 
>
> Una vez realizada esta operación, cierra el terminal y abre uno nuevo para que la inclusión de tu usuario en el nuevo grupo se haga efectiva. Comprueba que tu usuario pertenece al grupo docker con el comando 
> ```
> groups
> ```
> Si el grupo docker no aparece en la lista, prueba a salir de la sesión y volver a entrar o a reiniciar el ordenador.



## Windows 10

- [ ] Descarga e instala git

- [ ] Descarga e instala Docker desktop for Windows. Abre el programa.

- [ ] > Docker depende del subsistema de Windows para Linux (WSL). Es posible que tengas que instalar o actualizar este paquete durante la instalación de docker. Revisa los mensajes que aparecen durante la instalación/ejecución de docker. 
  >
  > También es posible que tengas que reiniciar Windows tras las instalación de docker.

- [ ] Abre un terminal del sistema, Powershell o git-bash y prueba si docker se está ejecutando con

  ```
  C:\Users\User> docker version
  ```



## osX

- [ ] Descarga e instala Docker for Mac. Abre el programa.

- [ ] Abre un terminal y prueba si docker se está ejecutando con 

  ```
  $ docker version
  ```



# Instalación y ejecución del servidor

- [ ] Abre un terminal (command line/powershell/git-bash en Windows  o terminal del sistema en osX/Linux)

- [ ] Descarga los ficheros de configuración del servidor [usuario normal]

```
git clone https://github.com/nbarreira/ipm2122-server.git
cd ipm2122-server
```

- [ ] Arranca la base de datos (usuario normal)

```
docker-compose up database
```

Asegúrate que la última línea que aparece en el log es:

```
db_ipm2122        | 2021-09-08 14:51:11.887 UTC [1] LOG:  database system is ready to accept connections 
```

- [ ] Abre otro terminal, sitúate en el directorio ipm2122-server y arranca el motor graphql (usuario normal)

```
docker-compose up graphql-engine
```

- [ ] Prueba el API REST (usuario normal) con curl, por ejemplo:

```
curl  -H "x-hasura-admin-secret:myadminsecretkey" "http://localhost:8080/api/rest/facilities" 
```

Deberías recibir un fichero JSON con los edificios almacenados en la base de datos.

Para detener la ejecución de los contenedores docker, pulsa Control+C en el terminal correspondiente

## Regeneración de la base de datos [opcional]

La base de datos se inicializa con datos por defecto la primera vez que se ejecuta el docker *database*. Si queremos reinicializar los datos, lo más sencillo es borrar los contenedores docker y volver a arrancarlos. Para borrar los contenedores docker (una vez parados), podéis utilizar el comando:

```
docker-compose rm
```

o bien

```
docker rm -f $(docker ps -a -q)
```

Una vez borrados los contenedores, sigue los pasos descritos en el apartado anterior para arrancar la base de datos y el motor graphql

Tenéis además un script en python a vuestra disposición para borrar los datos por defecto y generar nuevos datos. Para ejecutar este script tenéis que instalar las dependencias de la siguiente forma:

```
cd ipm2122-server/db
pip3 install -r requirements.txt
```

Una vez instaladas las dependencias, editad el fichero `generate_data.py` y adaptad las siguientes variables a vuestras necesidades:

```
NUM_USERS=100 # Número de usuarios que se crearán
NUM_FACILITIES=20 # Número de edificios que se crearán
MAX_ACCESS_PER_USER=20 # Número máximo de accesos por usuario que se crearán

# Datos de conexión a la base de datos.
CONNECTION_DATA="dbname='ipm2122_db' host='localhost' port='5438' user='ipm2122_user' password='secret'" 
```

El script se ejecuta de la siguiente forma:

```
python3 generate_data.py
```

I
