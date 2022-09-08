import solution
from controller.record import Record
from model.handle_db import HandleDB
from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse


app = FastAPI()
@app.exception_handler(Exception) #modificamos el tipo de respuesta de fastapi, enviando la respuesta requerida (error)
async def catch_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=status.HTTP_401_UNAUTHORIZED,
        content={"error": "Error in parameters"},
    )
@app.get('/stats', response_class=JSONResponse) #recibe un numero entero y devuelve stats de este numero
def getInformation(number: int):
    db = HandleDB()
    stats = db.get_stats(number) #obtiene stats del numero
    count,total = stats[0], stats[1] 
    ratio = float("{0:.2f}".format(count/total))
    return {
        "count": count,
        "total": total,
        "ratio": ratio
        }

@app.post('/smallest',response_class=JSONResponse, status_code=200)
async def proccessArray(info : Request):
    req_info = await info.json()
    array = req_info["array"]
    result = solution.smallest_number(array)
    data = {
        "array": array,
        "result": result
    }
    record = Record(data)
    record.createRecord()
    if (result >= 1):
        return {"result": result}
    else:
        raise Exception() 