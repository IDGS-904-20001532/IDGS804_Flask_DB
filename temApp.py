from db import get_connection

#BUSCAR ALUMNOS DE UN PROCEDIMIENTO ALMACENADA
# try:
#     connection=get_connection()
#     with connection.cursor() as cursor:
#         cursor.execute('call consulta_Alumno()')
#         resultset=cursor.fetchall()
#         for row in resultset:
#             print(row)
#             connection.close()
# except Exception as ex:
#     print(ex)

#BUSCAR UN ALUMNO DE UN PROCEDIMIENTO ALMACENADA
# try:
#     connection=get_connection()
#     with connection.cursor() as cursor:
#         cursor.execute('call consultar_unAlumno(%s)',(1,))
#         resultset=cursor.fetchall()
#         print(resultset)
#         connection.close()
# except Exception as ex:
#     print(ex)

#AGREGAR UN ALUMNO DE UN PROCEDIMIENTO ALMACENADA
try:
    connection=get_connection()
    with connection.cursor() as cursor:
        cursor.execute('call agregar_alumno(%s,%s,%s)',('Luis', 'Lopez', 'lopez@gmail.com'))
    connection.commit()
    connection.close()
except Exception as ex:
    print(ex)