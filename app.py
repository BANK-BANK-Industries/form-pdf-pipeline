import uvicorn
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.responses import RedirectResponse
from pathlib import Path
import json
import fillpdf
from fillpdf import fillpdfs


app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount(
    "/static",
    StaticFiles(directory=Path(__file__).parent.absolute() / "static"),
    name="static",
)


@app.get('/form', response_class=HTMLResponse)
def get_basic_form(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})


@app.post('/form', response_class=RedirectResponse)
def post_basic_form(request: Request, name: str = Form(...), gender: str = Form(...), address: str = Form(...), town: str = Form(...), phone: str = Form(...), email: str = Form(...), ethnicity: str = Form(...), isClin: str = Form("Off")):
    resp = {"name":  name, "gender":  gender, "address": address, "town": town, "phone": phone, "email": email, "ethnicity": ethnicity, "isClin": isClin}
    filename = "volform.pdf"
    filenamenew = f"pdfs/{name}.pdf"
    fillpdfs.write_fillable_pdf(filename, filenamenew, resp, flatten=False)
    return f"/files?filename={name}.pdf"

@app.post('/files', response_class=FileResponse)
def return_pdf(request: Request, filename: str):
    return f"pdfs/{filename}"

if __name__ == '__main__':
    uvicorn.run(app)
