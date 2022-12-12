from dal.db import Db

def listar():
    sql = "SELECT Rol_Id, Nombre FROM Roles ORDER BY Rol_Id;"
    result = Db.consultar(sql)
    return result