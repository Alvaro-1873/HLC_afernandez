import uvicorn
from fastapi import FastAPI, HTTPException, status, Body
import testmariadb as basedatos


app = FastAPI()

#----------------------------------------------------------------
#- Consulta todos los objetos de la tabla o filtrado por rareza -
#----------------------------------------------------------------

#Si la variable contiene un dato este lo pasara por la funcion Consultar_rareza, si no contiene nada presentara por pntalla toda la tabla
@app.get("/objetos_isaac")
def get_objetos(objeto_rare = None): #Esto indica que en cuyo caso de que no se le pase un parametro, lo deje vacio
    if objeto_rare:
        return basedatos.consultar_rareza(objeto_rare)
    else:
        return basedatos.consultar()

#------------------------------------
#- Consulta la tabla mediate una ID -
#------------------------------------

@app.get("/objeto_id/{objeto_id}")
def get_objetos_id(objeto_id):
    if objeto := basedatos.consultar_id(objeto_id): #Consulta si la ID exixte, si es asi devuelve el dato
        return objeto
    else:
        raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail=f"El objeto con la ID {objeto_id} no existe")

#-----------------------------------
#- Insertamos un objeto a la tabla -
#-----------------------------------

@app.post("/insert_objeto")
def insertar_objeto(objeto_datos = Body()): #Le pasamos por el cuerpo de la consulta un JSON
    try:
        objeto = basedatos.tranformar(objeto_datos) #Transforma el JSON a un objeto
        objeto.insertar() #Inserta el objeto a la sentcia slq
        return "Nuevo objeto añadido correctamente"
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, 
            detail=f"Error, no se a podido guardar la nueva entrada")

#-----------------------------------
#- Insertamos un objeto a la tabla -
#-----------------------------------

@app.put("/actu_objeto/{objeto_id}")
def actualizar_objeto(objeto_id, objeto_datos = Body()): #Le pasamos por el cuerpo de la consulta un JSON y la id del objeto que deseamos modificar
    try:
        if old_id := basedatos.consultar_id(objeto_id): #consultamos si la ID exixste
            basedatos.actualizar(objeto_id, objeto_datos) #Pasamos directamente la variabel que contiene el cuerpo de JSON y la id del objeto a acambiar
            return f"El objeto a sido actualizado correctamente"
        else:
            return "La ID que has pasado no existe"
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, 
            detail=f"Error, no se a podido guardar la nueva entrada")

#-------------------------------
#- Borrar un objeto a la tabla -
#-------------------------------
#    
@app.delete("/borra_objeto/{objeto_id}", status_code=status.HTTP_204_NO_CONTENT) #Pasadmos la ID del objeto
def borra_objeto(objeto_id):
    comprobar = basedatos.borrar(objeto_id)
    if comprobar == 0:
        return "El objeto a sido borrado correctamente"
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No se pudo borra el objeto con ID {objeto_id}")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
