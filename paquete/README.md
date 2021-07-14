# elidas_sqlite3
[ESP]
\nEsta es una versión que pretende simplificar el módulo sqlite3 de python.

Se incluyen la siguientes funciones:

  __init__(name):
    {name}  hace referencia a la variable que almacena el nombre de la base de datos.

  __create_tables__(name, p_key, typ):
    crea una tabla con una unica columna.
    {name}  hace referencia al nombre de la tabla a crear.
    {p_key} hace referencia al valor clave de la fila.
    {typ}   almacena el tipo de dato del valor clave.

  __insert_column__(table, column, type):
        Inserta columnas nuevas en la tabla establecida
        {table}  Nombre de la tabla
        {column} Nombre de la columna
        {type}   Establece el tipo de caracter almacenado en la columna.

  __insert_info__(self, table, column, info):
        Se emplea para insertar informacion en la tabla seleccionada en la
        columna establecida.
        {table}  Nombre de la tabla empleada
        {column} Columna en la que introducir la informacion
        {info}   infromacion a introdicir en la columna

  __update__(self, table, column, key, info):
      actualiza la infromacion en la columna especificada de una cierta tabla
      {table}  Nombre de la tabla empleada
      {column} nombre de la columna a actualizar
      {key}    Nombre de la columna que almacena el key
      {info}   Tupla con la siguiente estructura:
          (val, key)
              {val} Valor nuevo a introducir en la columna establecida
              {key} Key de la fila a modificar.

  __show_column_names__(self, table):
        Devuelve los nombres de las columnas de la tabla establecida.
        {table} Nombre de la tabla de la que se desea saber las columnas.

  __show_all_rows__(self, table):
      Devuelve toda la infromación de una tabla dada.
      {table} Nombre de la tabla de la que se desea saber la información.

  __show_one_row__(self, table, column, info):
      Devuelve la informacion de la fila seleccionada
      {table}  Nombre de la tabla en la que buscar la infromación
      {column} Nombre de la columna de referencia
      {info}   Infromacion a buscar en la columna.