'''
Author: Oscar Gutierrez
Email: o.guty66@gmail.com
Date: 2021-04-22
'''
# __LIBRARIES__ #
import sqlite3
from sqlite3 import Error

# __MAIN CODE__ #


class SQL:
    def __init__(self, name):
        self.db_name = name + '.db'
        self.create_connexion()
        self.cursorObj = self.conn.cursor()
        # try:
        #    self.find_tables()
        # except Error:
        #    self.table_names = list()
        #    self.create_table()

    def create_connexion(self):  # crea la conexion a la BDD o la propia BDD
        self.conn = None  # creamos el objeto conect
        # print('Estableciendo conexion...')
        try:  # caso de omitir la ruta se crea en el directorio actual
            self.conn = sqlite3.connect(self.db_name)  # crea la BD en la ruta
            # print('Conexion establecida con exito.')   # especificada
            # time.sleep(1)
        except Error as e:
            print(e)

    def find_tables(self):  # busca y almacena el nombre d ls tablas de la BDD
        self.table_names = list()
        self.cursorObj.execute(
            'SELECT name FROM sqlite_master WHERE type="table";')
        for name in self.cursorObj.fetchall():
            self.table_names.append(str(name)[2:-3])

    def create_table(self, name, p_key, typ):  # crea tablas nuevas en la BDD
        # name = str(input('Introduce el nombre de la Tabla: '))
        # p_key = str(input('Introduce el Valor Clave de la tabla: '))
        # typ = str(input('Introduce el tipo de variable (int, char): '))
        self.cursorObj.execute(
            'CREATE TABLE %s(%s %s PRIMARY KEY)' % (name, p_key, typ)
        )
        self.table_names.append(name)

    def insert_column(self, table, column, type):  # añade columnas a la BDD
        # table = str(input('Introduce el nombre de la Tabla: '))
        # column = str(input('Introduce el nombre de la columna: '))
        # type = str(input('Introduce el tipo de variable (int, char): '))
        self.cursorObj.execute(
            'ALTER TABLE %s ADD COLUMN %s %s' % (table, column, type)
        )

    def insert_info(self, table, column, info):
        value = (info,)
        self.cursorObj.execute(
            'INSERT INTO %s(%s) VALUES(?)' % (table, column), value
        )

    def update(self, table, column, key, info):
        self.cursorObj.execute(
            'UPDATE %s SET %s = ? WHERE %s = ?' % (table, column, key), info
        )

    def commit(self):
        self.conn.commit()


'''

    def list(self):

    def delete(self):
'''


def run():
    db = SQL('Mia')
    # db.insert_info('Replicas', 'SN', '12345')
    # db.commit()
    db.update('Replicas', 'Modelo', 'SN', ('P90', '12345'))
    db.commit()


if __name__ == '__main__':
    run()

# __NOTES__ #
'''
    __init__(name):
        {name}  hace referencia a la variable que almacena el nombre de la base
                de datos.
    create_connexion():
        Crea la conexion con la base de datos.
    create_tables(name, p_key, typ):
        crea una tabla con una unica columna.
        {name}  hace referencia al nombre de la tabla a crear.
        {p_key} hace referencia al valor clave de la fila.
        {typ}   almacena el tipo de dato del valor clave.
    insert_column():

    inster_info():
        Se emplea para insertar informacion en la tabla seleccionada
        en la columna establecida.
    update():
        actualiza la infromacion en la columna especificada de una cierta tabla
    list_simple():
        nos permite ver la infromacion de una fila dada mediante el key value
    list_all():
        nos permite ver toda la infromacion de una tabla
    list_complete():
        nos permite ver toda la informacion en una base de datos
    delete():
        eliminara la informacion especificada.

'''
# __BIBLIOGRAPHY__ #
