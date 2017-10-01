# Odontcloud

## Primeros pasos: 

#### 1. [Instalar python3.6](https://askubuntu.com/questions/865554/how-do-i-install-python-3-6-using-apt-get)

#### 2 Ejecutar:
        sudo apt-get install python3.6-dev

#### 3: Configurar entorno virtual dentro de la carpeta /backend. Elegir entre [virtualenv](https://virtualenv.pypa.io/en/stable/) ó [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/)
        Si elegiste virtualenv:
        virtualenv -p python3 venv

#### 4: Activar entorno virtual

#### 5: [Instalar nvm](https://github.com/creationix/nvm) dentro de la carpeta frontend, nosotros usamos la versión 6.10.3 (lts/boron)
        Dentro del directorio del proyecto:
        nvm install 6.10.3
        nvm use 6.10.3
        nvm alias default 6.10.3

#### 5.1: Instalar globalmente la [cli de angular](https://github.com/angular/angular-cli)

#### 6: Instalar dependencias para backend:
        pip install -r requirements.txt

#### 6.1: Activar el hook [pre-commit](http://pre-commit.com/).
        pre-commit && pre-commit install

#### 7: Correr migraciones dentro de /backend/api:
        python manage.py migrate

#### 8: Instalar dependencias en /frontend:
        npm install
        

#### 9: Correr server de frontend:
        npm start

#### 10: Correr server de backend:
        python manage runserver

# Reglas:
* Respetar **PEP257**.
* Nunca pushear directamente a master o al release. **SIEMPRE** hacer pull request con el nuevo feature.
* El largo límite de una sentencia es de **120**.
* Debe pasar **flakes8**.
* Cada método/clase debe ser comentada diciendo **QUÉ** hace, no cómo lo hace.
* La convención de formato de comentarios debe seguir la [JSDoc](https://en.wikipedia.org/wiki/JSDoc). 
* Los comentarios deben estar en inglés (exceptuando este readme que ya lo hice en castellano) :dizzy_face:
* Los comentarios deben incluir el tipo esperado (ej {str} o {int}) y una breve descripción para cada **parámetros de entrada** y **parámetros de salida**.
* Si tenés dudas, HABLÁ con tus compañeros.
* Si no sabés respecto a la filosofía python, escribí en tu intérprete de python ```import this```.
* El commit con los cambios debe respetar el siguiente formato: 
<código del proyecto>-<número de issue> [cualquier texto explicativo]. Por ejemplo:
    ```git commit -am 'ODC-21 some changes in the backend'```.

#### ¿En el horno? :P
Escribile a Nano o Javi.

##### TODO:
- :white_large_square: Proxiar el server de frontend para poder usar la api de backend.  
- :white_large_square: Scrip de deploy.
- :white_large_square: Agregar la sección de postgresql en el readme.
- :white_large_square: Adding code arquitecture for readers.
