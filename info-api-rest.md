# API REST

**GET /api/rest/users**

Obtiene todos los usuarios de la base de datos

Parámetros opcionales:

- offset (int): lista usuarios a partir del usuario número *offset*
- limit (int): lista *limit* usuarios

Ejemplos:

Línea de comandos con curl

```sh
curl  -H "x-hasura-admin-secret:myadminsecretkey" http://localhost:8080/api/rest/users

curl  -H "x-hasura-admin-secret:myadminsecretkey" "http://localhost:8080/api/rest/users?offset=10&limit=2"
```

Python, con librería requests:

```python
import requests

r = requests.get("http://localhost:8080/api/rest/users?offset=10&limit=2", 
     headers={"x-hasura-admin-secret":"myadminsecretkey"})
data = r.json()
print(data)
```

**GET /api/rest/user/:id**

Obtiene la información de un usuario con identificador *id*

Ejemplo:

```sh
curl  -H "x-hasura-admin-secret:myadminsecretkey" http://localhost:8080/api/rest/users/cb8e3ff9-2c7c-452d-9828-37ab4a6eb660
```



**GET /api/rest/user**

Obtiene la información de un usuario especificando su nombre y apellidos

Parámetros obligatorios:

- name (string): nombre del usuario
- surname (string): apellidos del usuario

Ejemplo:

```sh
curl  -H "x-hasura-admin-secret:myadminsecretkey" "http://localhost:8080/api/rest/user?name=Alberto&surname=Lopez"
```



**GET /api/rest/facilities**

Obtiene todos los edificios de la base de datos

Parámetros opcionales:

- offset (int): lista edificios a partir del edificio número *offset*
- limit (int): lista *limit* edificios

Ejemplo:

```sh
curl  -H "x-hasura-admin-secret:myadminsecretkey" "http://localhost:8080/api/rest/facilities" 
```



**GET /api/rest/facilities/:id**

Obtiene la información del edificio con identificador *id*

Ejemplo:

```shell
curl  -H "x-hasura-admin-secret:myadminsecretkey" "http://localhost:8080/api/rest/facilities/111"
```



**GET /api/rest/access_log**

Obtiene todos los registros de acceso

Parámetros opcionales:

- offset (int): lista registros a partir del registro número *offset*
- limit (int): lista *limit* registros

Ejemplo:

```sh
curl  -H "x-hasura-admin-secret:myadminsecretkey" "http://localhost:8080/api/rest/access_log"
```



**GET /api/rest/facility_access_log/:id**

Obtiene los registros de acceso del edificio con identificador *id*

Parámetros opcionales:

- offset (int): lista registro a partir del registro número *offset*
- limit (int): lista *limit* registros

Ejemplo:

```sh
curl  -H "x-hasura-admin-secret:myadminsecretkey" "http://localhost:8080/api/rest/facility_access_log/111"
```



**GET /api/rest/user_access_log/:id**

Obtiene los registros de acceso del usuario con identificador *id*

Parámetros opcionales:

- offset (int): lista registros a partir del registro número *offset*
- limit (int): lista *limit* registros

Ejemplo:

```sh
curl  -H "x-hasura-admin-secret:myadminsecretkey" "http://localhost:8080/api/rest/user_access_log/cb8e3ff9-2c7c-452d-9828-37ab4a6eb660"
```



**GET /api/rest/facility_access_log/:id/daterange**

Obtiene los registros de acceso del edificio con identificador *id* en un rango de fechas especificado.

Parámetros obligatorios:

- startdate (timestamp): fecha de inicio del rango
- enddate (timestamp): fecha final del rango

Parámetros opcionales:

- offset (int): lista registro a partir del registro número *offset*
- limit (int): lista *limit* registros

Ejemplo:

```sh
curl  -H "x-hasura-admin-secret:myadminsecretkey" "http://localhost:8080/api/rest/facility_access_log/111/daterange" -d '{"startdate": "2021-01-01T02:03:00+00:000", "enddate": "2021-12-01T02:03:00+00:000"}' -X GET
```

```python
import requests
r = requests.get( 
  "http://localhost:8080/api/rest/facility_access_log/111/daterange?offset=0&limit=10", 
  headers={"x-hasura-admin-secret":"myadminsecretkey"}, 
  json={"startdate": "2021-01-01T02:03:00+00:000", "enddate": "2021-12-01T02:03:00+00:000"})
data = r.json()
print(data)
```



**GET /api/rest/user_access_log/:id/daterange**

Obtiene los registros de acceso del usuario con identificador *id* en un rango de fechas especificado.

Parámetros obligatorios:

- startdate (timestamp): fecha de inicio del rango
- enddate (timestamp): fecha final del rango

Parámetros opcionales:

- offset (int): lista registros a partir del registro número *offset*
- limit (int): lista *limit* registros

Ejemplo:

```sh
curl  -H "x-hasura-admin-secret:myadminsecretkey" "http://localhost:8080/api/rest/user_access_log/cb8e3ff9-2c7c-452d-9828-37ab4a6eb660/daterange" -d '{"startdate": "2021-01-01T02:03:00+00:000", "enddate": "2021-12-01T02:03:00+00:000"}' -X GET
```

**POST /api/rest/user**

Crea un nuevo usuario en la base de datos. 

Parámetros obligatorios:

- username (string): nombre de usuario
- password (string): contraseña en claro
- name (string): nombre
- surname (string): apellidos
- phone (string): teléfono
- email (string): dirección de correo electrónico
- is_vaccinated (boolean): indica si el usuario está vacunado. 

Devuelve el identificador del usuario (uuid),

NOTA: el campo login está definido como unique en la base de datos por lo que no es posible insertar dos usuarios con el mismo nombre de login.

Ejemplo:

```sh
curl  -H "x-hasura-admin-secret:myadminsecretkey" "http://localhost:8080/api/rest/user" -d '{"username": "pepe", "password": "xx", "name": "Jose", "surname": "Garcia", "phone": "555555", "email": "pepe@pepe.com", "is_vaccinated": "true"}' -X POST
```

```python
import requests
r = requests.post(
  "http://localhost:8080/api/rest/user",
  headers={"x-hasura-admin-secret":"myadminsecretkey"},
  data={"username": "pepe", "password": "xx", "name": "Jose", "surname": "Garcia", 
        "phone": "555555", "email": "pepe@pepe.com", "is_vaccinated": "true"})
data = r.json()
print(data)
```



**POST /api/rest/login**

Simula la operación de login en el servidor. Devuelve la información del usuario.

Parámetros obligatorios:

- username (string): nombre de usuario
- password (string): contraseña. Por simplicidad, la contraseña se envía en claro. Esta práctica no sería aceptable en una aplicación real!

Ejemplo:

```sh
curl  -H "x-hasura-admin-secret:myadminsecretkey" "http://localhost:8080/api/rest/login?username=pepe&password=xx" -X POST
```



**POST /api/rest/access_log**

Crea un nuevo registro de acceso de un usuario a un edificio

Parámetros obligatorios:

- user_id (uuid): identificador de usuario
- facility_id (int): identificador de edificio
- timestamp (timestamp): timestamp con la fecha y hora de acceso
- type (string): tipo de acción, Dos posibles valores: IN (registro de entrada) y OUT (registro de salida), 
- temperature (string): temperatura del usuario  

Ejemplo:

```sh
curl  -H "x-hasura-admin-secret:myadminsecretkey" "http://localhost:8080/api/rest/access_log" -d '{"facility_id": 111, "user_id": "cb8e3ff9-2c7c-452d-9828-37ab4a6eb660", "timestamp": "2021-09-05T18:58:00+00:00","type":"IN", "temperature": "35.7"}' -X POST

```

Ejemplo en Dart (usando paquetes http y dart:convert):
```dart

 var data = {
      "user_id": "cb8e3ff9-2c7c-452d-9828-37ab4a6eb660",
      "facility_id": 130,
      "timestamp": "2021-10-14T18:58:00+00:00",
      "type": "IN",
      "temperature": "35.5"
    };

var url = Uri.parse("http://localhost:8080/api/rest/access_log");
var response = await http.post(
      url,
      headers: {
        "x-hasura-admin-secret": "myadminsecretkey",
      },
      body: json.encode(data),
);
```
