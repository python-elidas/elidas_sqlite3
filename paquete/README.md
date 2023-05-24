# simply_sqlite

[ESP]`<br>`
Esta es una versión que pretende simplificar el módulo sqlite3 de python.

Se incluyen la siguientes funciones:


**get_tables(****)**

    

  __create_tables__(name, p_key, typ):`<br>`
  crea una tabla con una unica columna.`<br>`
  &ensp;&emsp;{name}  hace referencia al nombre de la tabla a crear.`<br>`
  &ensp;&emsp;{p_key} hace referencia al valor clave de la fila.`<br>`
  &ensp;&emsp;{typ}   almacena el tipo de dato del valor clave.

  __insert_column__(table, column, type):`<br>`
  Inserta columnas nuevas en la tabla establecida `<br>`
  &ensp;&emsp;{table}  Nombre de la tabla `<br>`
  &ensp;&emsp;{column} Nombre de la columna `<br>`
  &ensp;&emsp;{type}   Establece el tipo de caracter almacenado en la columna.

  __insert_info__(self, table, column, info):`<br>`
  Se emplea para insertar informacion en la tabla seleccionada en la `<br>`
  columna establecida.`<br>`
  &ensp;&emsp;{table}  Nombre de la tabla empleada `<br>`
  &ensp;&emsp;{column} Columna en la que introducir la informacion `<br>`
  &ensp;&emsp;{info}   infromacion a introdicir en la columna

  __update__(self, table, column, key, info):`<br>`
  actualiza la infromacion en la columna especificada de una cierta tabla `<br>`
  &ensp;&emsp;{table}  Nombre de la tabla empleada `<br>`
  &ensp;&emsp;{column} nombre de la columna a actualizar `<br>`
  &ensp;&emsp;{key}    Nombre de la columna que almacena el key `<br>`
  &ensp;&emsp;{info}   Tupla con la siguiente estructura:`<br>`
  &ensp;&emsp;&ensp;&emsp;(val, key)`<br>`
  &ensp;&emsp;&ensp;&emsp;&ensp;&emsp;{val} Valor nuevo a introducir en la columna establecida `<br>`
  &ensp;&emsp;&ensp;&emsp;&ensp;&emsp;{key} Key de la fila a modificar.

  __show_column_names__(self, table):`<br>`
  Devuelve los nombres de las columnas de la tabla establecida.`<br>`
  &ensp;&emsp;{table} Nombre de la tabla de la que se desea saber las columnas.

  __show_all_rows__(self, table):`<br>`
  Devuelve toda la infromación de una tabla dada.`<br>`
  &ensp;&emsp;{table} Nombre de la tabla de la que se desea saber la información.

  __show_one_row__(self, table, column, info):`<br>`
  Devuelve la informacion de la fila seleccionada `<br>`
  &ensp;&emsp;{table}  Nombre de la tabla en la que buscar la infromación `<br>`
  &ensp;&emsp;{column} Nombre de la columna de referencia `<br>`
  &ensp;&emsp;{info}   Infromacion a buscar en la columna.
