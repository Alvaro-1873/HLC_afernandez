import uvicorn
from fastapi import FastAPI, HTTPException, status, Body
import testmariadb as basedatos


app = FastAPI()

@app.get("/objetos_isaac")
def get_objetos(objeto_rare = None):
    if objeto_rare:
        return basedatos.consultar_rareza(objeto_rare)
    else:
        return basedatos.consultar()


@app.get("/objeto_id/{objeto_id}")
def get_objetos_id(objeto_id):
    if objeto := basedatos.consultar_id(objeto_id):
        return objeto
    else:
        raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail=f"El objeto con la ID {objeto_id} no existe")

@app.post("/insert_objeto")
def insertar_objeto(objeto_datos = Body()):
    try:
        objeto = basedatos.tranformar(objeto_datos)
        objeto.insertar()
        return "Nuevo objeto añadido correctamente"
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, 
            detail=f"Error when trying to save the new entry")

@app.put("/actu_objeto/{objeto_id}")
def actualizar_objeto(objeto_id, objeto_datos = Body()):
    try:
        if old_id := basedatos.consultar_id(objeto_id):
            basedatos.actualizar(objeto_id, objeto_datos)
            return f"El objeto a sido actualizado correctamente"
        else:
            return "La ID que has pasado no existe"
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, 
            detail=f"Error when trying to save the new entry")
    
@app.delete("/borra_objeto/{objeto_id}", status_code=status.HTTP_204_NO_CONTENT)
def borra_objeto(objeto_id):
    comprobar = basedatos.borrar(objeto_id)
    if comprobar == 0:
        return "El objeto a sido borrado correctamente"
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Couldn't delete pokemon ID {objeto_id}")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
