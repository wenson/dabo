��    W      �     �      �  #   �  ,   �     �     �  �   �    �  I   �	  �   �	     �
  6   �
  �        �       *     #   A  C   e     �  0   �  z   �  6   o  F   �  @   �  1   .  �   `  S   @  �   �  *   G  6   r  *   �  k   �  �   @  C   �  +     2   >      q     �  *   �  +   �  g   �     d  $   g      �     �  E   �  G   �  5   D  �   z  6     E   :  M   �  <   �  (     n  4  I   �  5   �  3   #     W  K   v  C   �  =     D   D  =  �     �  .   �  %     6   ;  5   r  C   �  L   �  ?   9  I   y     �  {   �  /   ^  G   �  '   �  <   �     ;  #   [       :   �  r   �  �   6  4   �  "   �  "      �  3   7   �!  >   "     O"     l"  �   s"  &  ?#  \   f$  �   �$     �%  F   �%    �%  3   '     E'  '   N'  /   v'  S   �'     �'  >   (  �   Y(  *   
)  X   5)  K   �)  I   �)    $*  p   :+  �   �+  ?   h,  <   �,  .   �,  w   -  �   �-  G   0.  Q   x.  C   �.  6   /     E/  >   _/  /   �/  �   �/     h0  V   p0  "   �0     �0  P   �0  A   H1  8   �1  �   �1  H   p2  Q   �2  H   3  H   T3  2   �3  �  �3  i   z5  B   �5  =   '6  6   e6  R   �6  _   �6  Q   O7  O   �7  R  �7  #   D9  2   h9  L   �9  9   �9  E   ":  A   h:  L   �:  V   �:  K   N;     �;  p   �;  I   '<  X   q<  D   �<  O   =  +   _=  1   �=     �=  H   �=  �   >  �   �>  9   H?  #   �?  *   �?     K   #       3   S   &           R   +          '   (   9   H                  6   4   B   J          
   %   ,      U   N       C              ?           W      G                     5       A   1                     F       <                T          V   )          Q      =   M       *      D   O   ;                        /           $   "       :   E      L                 8          P          	   !   -   2   @       >      I          .       0                  7    #Queries for DB '%s' on host '%s':
 %s database connection definition(s) loaded. %s: Path does not exist. < None > A dictionary mapping virtual_field_name to function to call.

			The specified function will be called when getFieldVal() is called on
			the specified virtual field name. A dictionary specifying default values for fields when a new record is added.

			The values of the dictionary can be literal (must match the field type), or
			they can be a function object which will be called when the new record is added
			to the bizobj. After a requery, do we try to restore the record position to the same PK? After running a scan, do we attempt to restore the record position to
			where it was before the scan (True, default), or do we leave the pointer
			at the end of the recordset (False). (bool) Application finished. Base key used when saving/restoring preferences  (str) Base key used when saving/restoring preferences. This differs
			from the default definition of this property in that if it is empty, it 
			will return the ActiveForm's BasePrefKey or the MainForm's BasePrefKey
			in that order. (str) Can't set ActiveForm: no uiApp. Cancel Cannot reverse in the middle of iteration. Cannot update file: '%s'. Error: %s Could not access the database with the given username and password. Could not open file: '%s' Could not setup the database. Access was denied. DBA, please enter the username and password that has access to create tables for database on server '%s' and database '%s' Deletion prohibited - there are related child records. Determines if we are using a table that auto-generates its PKs. (bool) Do we scan the records in reverse order? (Default: False) (bool) Fields in the cursor to be ignored during updates For the DB Admin:
 The tables must either created by:
  1. using this program by TEMPORARLY giving this program access to the database to create the needed tables.
  2. or executing all the quries in the 'queries.sql' file. If this bizobj's parent has NewChildOnNew==True, do we create a record here? (bool) In the onNew() method, do we fill in the foreign key field specified by the
			LinkField property with the value returned by calling the bizobj's 	getParentPK()
			method? (bool) Login incorrect, please try again. (%s/%s) Method '%s' of object '%s' has the following error: %s Name of encoding to use for unicode  (str) Name of field that is the PK. If multiple fields make up the key,
			separate the fields with commas. (str) Name of the field in the parent table that is used to determine child
			records. If empty, it is assumed that the parent's PK is used  (str) Name of the field that is the foreign key back to the parent. (str) No Primary Key defined in the Bizobj for %s No base key set; preference will not be persisted. No key field defined for table:  No records deleted No table has been defined for this bizobj. No tables have been setup for autocreation. Normally new, unmodified records are not saved. If you need
			this behavior, set this to True.  (bool) OK PK Value %s not found in the dataset Parent must descend from dBizobj Password Reference to the cursor that handles SQL Builder information (cursor) Reference to the object that provides cryptographic services.  (varies) Reference to the parent bizobj to this one. (dBizobj) Represents a record in the data set. You can address individual
			columns by referring to 'self.Record.fieldName' (read-only) (no type) Returns True if the current record is new and unsaved. Returns the SQL statement automatically generated by the sql manager. Returns the current SQL that will be run, which is one of UserSQL or AutoSQL. Returns the form that currently has focus, or None.  (dForm) Returns the last executed SQL statement. Returns the structure of the cursor in a tuple of 6-tuples.

				0: field alias (str)
				1: data type code (str)
				2: pk field (bool)
				3: table name (str)
				4: field name (str)
				5: field scale (int or None)

				This information will try to come from a few places, in order:
				1) The explicitly-set DataStructure property
				2) The backend table method SQL statement to run. If set, the automatic SQL builder will not be used. SQL statement used to create the cursor's data. (str) SecurityManager must descend from dSecurityManager. SecurityManager previously set Should new child records be added when a new parent record is added? (bool) Specifies the form class to use for the application's About screen. Specifies the message to initially display on the login form. Specifies the number of attempts the user has to login successfully. Specifies whether a child bizobj gets requeried automatically.

				When True (the default) moving the record pointer or requerying the
				parent bizobj will result in the child bizobj's getting requeried
				as well. When False, user code will have to manually call
				child.requery() at the appropriate time.
				 Stub: dApp.onEditPreferences() Text to display for null (None) values.  (str) The UI cannot be reset once assigned. The base Dabo class of the object. Read-only.  (class) The class the object is based on. Read-only.  (class) The current position of the record pointer in the result set. (int) The cursor object for the currently selected key value. (dCursorMixin child) The database could not be setup. Contact your DB administrator. The friendly title of the cursor, used in messages to the end user. (str) The name of the object.  (str) The number of records in the cursor's data set. It will be -1 if the
			cursor hasn't run any successful queries yet. (int) The table definition for this bizobj.  (object) The title of the cursor. Used in resolving DataSource references. (str) Tried to set UI to '%s', but it failed. User interface already set to '%s', so dApp didn't touch it. User interface set set to None. User interface set to '%s' by dApp. Username WARNING: No BasePrefKey has been set for this application. When True (default), table and column names are enclosed with
			quotes during SQL creation in the cursor.  (bool) When True, the cursor object runs its query immediately. This
			is useful for lookup tables or fixed-size (small) tables. (bool) You do not have the database module for %s installed You must enter the password first. You must enter the username first. Project-Id-Version: dabo
Report-Msgid-Bugs-To: FULL NAME <EMAIL@ADDRESS>
POT-Creation-Date: 2007-08-26 10:04+0000
PO-Revision-Date: 2008-07-22 14:47+0000
Last-Translator: Julián Alarcón <alarconj@gmail.com>
Language-Team: Spanish <es@li.org>
MIME-Version: 1.0
Content-Type: text/plain; charset=UTF-8
Content-Transfer-Encoding: 8bit
X-Launchpad-Export-Date: 2008-11-29 16:28+0000
X-Generator: Launchpad (build Unknown)
 #Consultas por base de datos '%s' en el servidor '%s':
 %s definición(es) de conección del database fueron cargadas. %s: Subdirectorio no existe. <Nada> Una lista de relaciones entre el nombre_virtual_del_campo hacia funciones para ejecutar.

			La función especificada será llamada cuando getFieldVal() sea ejecutado
			desde el nombre de campo virtual. Una lista especificando valores predeterminados para los campos cuando se agrega un nuevo registro.

tab]		Los valores de la lista pueden ser literales (deben correspondera al tipo de campo), o 
			puden ser un objeto funcion que se ejecutara cuando el nuevo registro sea agregado
			al bizobj. ¿Restaurar la posicion del registro en la misma llave primaria despues de la actualizacion? Despues de hacer una busqueda, restaurar la posicion del puntero
			a la posición en la que estaba antes de la busqueda (Verdadero, predeterminado), o dejar el puntero
			al final del conjuto de datos (Falso). (boleano) Aplicación terminada. Clave base utilizada cuando se graban/restauran las preferencias (str) La clave utilizada cuando se establecieron las preferencias de grabado/restauración.  Esto difiere
			de la definición para esta propiedad en que esta vacia, va a
			devolver BasePrefKey del fomulario activo o el BasePrefKey del formulario principal
			en ese orden. (str) No pude configurar el ActiveForm:  no existe uiApp. Cancelar No se puede reversar dentro de un bucle No puedo actualizar el archivo: '%s'. Error. %s No puedo acceder la base de datos con el nombre del usuario y contraseña indicada. No puedo abrir el archivo: '%s' No puedo configurar la base de datos.  El acceso fue denegado. Administrador de Base de Datos, favor entrar el nombre del usuario y contraseña para acceder a crear las tablas de la base de datos en el servidor '%s' y la base de datos '%s' No se permite borrar - Hay registros hijos Determina si estamos utilizando una tabla para auto-generar sus claves primarias. (bool) ¿Buscar los registros en orden inverso? (Predeterminado: Falseo) (Boleano) Los campos en el cursor que serán ignorados durante las actualizaciones. Para el Administrador de Base de Datos:
Las tablas deben ser creadas de una de las siguientes formas:
1. utilizando este programa dándole acceso TEMPORALMENTE a la base de datos para crear las tablas necesarias.
2. o ejecutando todas las consultas en el archivo 'queries.sql'. Si el objeto bizobj tiene la propiedad NewChildOnNew en verdadero, ¿se debe crear un nuevo registro? (booleano) En el metodo onNew(), ¿debe llenarse la clave foranea especificada en la
			propiedad LinkField con el valor devuelto al hacer la llamada al metodo 	getParentPK()
			del bizobj? (boleano) Claves de entrada incorrectas, favor tratar nuevamente. (%s/%s) El método '%s' del objeto '%s' tiene el siguiente error: %s Nombre del codigo que usa para unicode (texto) Nombre del campo que es la llave primaria. Si varios campos componen la llave,
			separe los nombres con comas. (texto) Nombre del campo en la tabla padre que es usado para determinar los registros hijos.
			Si esa en blanco, se asume que la llave primaria del padre es usada (texto) Nombre del campo, llave foránea, que hace referencia al padre. (texto) No hay una clave primaria definida para este objecto de negocio [Bizobj] para %s. No se ha configurado la clave basica;  no permanece la preferencia. No se ha definido una clave primaria para esta tabla.  No se eliminaron récords No hay tablas definidas para este objecto de negocio [bizobj]. Noy hay tablas configuradas para autocreación. Normalmente los registros nuevos y sin modificaciones no son guardados.  Si desea 
			que sean guardados, asigne esta propiedad como Verdadero. (boleano) ACEPTAR El valor de la clave %s primaria %s  no se encuentra en el conjunto de datos [dataset] El Padre debe descender de dBizobj Contraseña: Hace referencia al cursor que maneja la información del creador de SQL (cursor) Referencia al objeto que provee servicios de crytografia. (varia) Referencia de este objeto con el bizobj padre. (dBizobj) Representa un registro en el conjunto de datos.  Puede hacer referencia individualmente
			a cada columna de la forma: 'self.Record.nombredecampo' (solo lectura) (sin tipo) Devuelve Cierto si el récord seleccionado es nuevo y no se ha guardado. Devuelve la instrucción en SQL generada automaticamente por el manejador de sql. Devuelve el SQL actual que va a ser ejecutado, que es UserSQL o AutoSQL. Devuelve el formulario que actualmente tiene el foco, o ninguno. (dForm) Devuelve la última instrucción de SQL ejecutada. Devuelve la estructura del cursor en una matriz de 6 filas.

				0: alias del campo (texto)
				1: codigo del tipo de datos (texto)
				2: llave primaria (boleano)
				3: nombre de la tabla (texto)
				4: nombre del campo (texto)
				5: escala del campo  (entero o Ninguno)

				Esta informacion intentara obtenerse de: 
				1) La propiedad DataStructure explicitamente definida 
				2) El metodo tabla del proveedor de datos La instrucción de SQL a ejecutar.  Si es seleccionada, el creador de SQL automático no será utilizado. instrucción de SQL utilizada para crear la data del cursor. (str) El manejador de Seguridad debe descender del dSecurityManager El Manejador de Seguridad fue previamente seleccionado ¿Se deben agregar registros hijos cuando se agrega un  registro padre? (booleano) Especifica la clase del formulario a ser utilizado por la pantalla Acerca de de la aplicación. Especifica el mensaje que se desplegara inicialmente en el formulario de entrada. Especifica el numero de intentos que tiene el usuario para entrar exitosamente. Especifica si un objeto bizobj hijo se actualiza automáticamente.

				Cuando es Verdadero (predeterminado) al mover el puntero o actualizar
				el objeto bizobj padre, hará que el bizobj hijo también sea actualizado.
				Cuando es Falso, el usuario debe especificar manualmente cuando 
				hacer la actualizacion del objeto hijo.
				 Fragmento: dApp.onEditPreferences() Texto a desplegar para nulo (Ningún) valor. (str) El Interfase de Usuario no puede ser reconfigurado una vez ha sido asignado. La clase Dabo base del objeto. Lectura solamente. (clase) La clase en la cual el objeto esta basado. Lectura solamente. (clase) La posición actual del puntero en el conjunto de datos. (entero) El objeto cursor para la llave actualmente seleccionada. (dCursorMixin hijo) La base de datos no pudo ser configurada.  Contacte al Administrador de Base de Datos. El nombre familiar del cursor, utilizado en mensajes para el usuario. (str) El nombre del objeto. (str) El número de registros en el cursor.  Será -1 si 
			no regresa ningun registro al hacer la consulta. (entero) La definición de la tabla para este objecto de negocio [bizobj. (objeto) El nombre del cursor.  Utilizado en resolver las referencias de la Fuente de Data. (str) Se trató de configurar el Interfase de Usuario a '%s', pero falló. La interface del usuario se ha establecido a '%s', dApp no hara ningún cambio. Interfase de usuario configurado a Ninguno. Interfase de usuario configurado a '%s' por dApp. Nombre del usuario ADVERTENCIA:  No se ha configurado el BasePrefKey para esta aplicación. Cuando es verdadero (predeterminado), el nombre de la tabla y las columnas es encerrado entre
			comillas durante la creacion del cursor SQL. (booleano) Cuando es verdadero, el objeto cursor ejecuta su consulta inmediatamente.  Esto
			es útil para tablas de consulta o de tamaño pequeño. (Booleano) No tiene el modulo de la base de datos para %s instalado. Debe entrar primero la contraseña. Debe entrar primero el nombre del usuario. 