from typing import Annotated
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
import explore_data
app = FastAPI()

@app.post("/files/")
async def create_files(
    files: Annotated[list[bytes], File(description="Multiple files as bytes")],
):
    return {"file_sizes": [len(file) for file in files]}



@app.post("/uploadfiles/")
async def create_upload_files(files: Annotated[
         list[UploadFile], File(description="Multiple files as UploadFile")
     ],):
    file1, file2 = files
    explore_data.process_data(file1.file, file2.file)
    # set exceptions (think about different error codes)
    # basic negative scenarios
    return{file1.filename, file2.filename}

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