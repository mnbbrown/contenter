from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from starlette.responses import JSONResponse
from api.content.view import router as content_router
from api.accounts.views import router as accounts_router

app = FastAPI()



@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return JSONResponse({"message": str(exc)}, status_code=400)


@app.get("/")
def read_root():
    return {"status": "ok"}


app.include_router(content_router, prefix="/admin/content")
app.include_router(accounts_router, prefix="/auth")
