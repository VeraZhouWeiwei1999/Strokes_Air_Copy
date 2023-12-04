from typing import Annotated
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
import pandas as pd
import explore_data
app = FastAPI()

@app.post("/files/")
async def create_files(
    files: Annotated[list[bytes], File(description="Multiple files as bytes")],
):
    return {"file_sizes": [len(file) for file in files]}



# @app.post("/uploadfiles/")
# async def create_upload_files(files: List[UploadFile] = File(...)):
#     file1, file2 = files
#     result_df = explore(file1, file2)
#     return {"filename1": file1.filename, "filename2": file2.filename, "result_df": result_df.to_dict()}

@app.post("/uploadfiles/")
async def create_upload_files(
    files: Annotated[
        list[UploadFile], File(description="Multiple files as UploadFile")
    ],
):
    explore(file1, file2)
    return {"filenames": [file.filename for file in files]}

#захардкодить файлнеймы - они мне известны. Передавать

async def explore(file1: UploadFile = File(...), file2: UploadFile = File(...))-> pd.DataFrame:
    explore_data.process_data(file1.file, file2.file)
    return("result")

@app.get("/")
async def main():
    content = """
    <body>
    <h2>File Upload Form</h2>
    <form action="/uploadfiles/" method="post" enctype="multipart/form-data" id="upload-form">
        <input type="file" name="files" multiple>
        <input type="submit" value="Submit">
    </form>
    </body>
    """
    return HTMLResponse(content=content)



# <body>
# <form action="/files/" enctype="multipart/form-data" method="post">
# <input name="files" type="file" multiple>
# <input type="submit">
# </form>
# <form action="/uploadfiles/" enctype="multipart/form-data" method="post">
# <p>Choose air data file</p>
# <input name="files" type="file" multiple>
# <input type="submit">
# </form>
# <form action="/uploadfiles/" enctype="multipart/form-data" method="post">
# <p>Choose strokes data file</p>
# <input name="files" type="file">
# <input type="submit">
# </form>
# </body>