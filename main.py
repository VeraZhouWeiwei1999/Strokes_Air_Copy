from typing import Annotated
from fastapi import FastAPI, File, HTTPException, UploadFile
from fastapi.responses import HTMLResponse, JSONResponse
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
    
    allowed_extensions = {'csv'} 
    try:
        if len(files) != 2:
            raise HTTPException(status_code=400, detail="Please upload exactly 2 files")
        
        for uploaded_file in files:
            if uploaded_file.filename.split(".")[-1] not in allowed_extensions:
                raise HTTPException(status_code=400, detail="Only .csv files are allowed")

        file1, file2 = files
        explore_data.process_data(file1.file, file2.file)
        return{file1.filename, file2.filename}

    except HTTPException as e:
        return JSONResponse(content={"error": str(e.detail)}, status_code=e.status_code)
    


@app.get("/")
async def main():
    content = """
    <body>
    <h2>File Upload Form</h2>
    <h3>Please, select two data sets: one for strokes data and one for air quality data</h3>
    <form action="/uploadfiles/" method="post" enctype="multipart/form-data" id="upload-form">
        <input type="file" name="files" multiple>
        <input type="submit" value="Submit">
    </form>
    </body>
    """
    return HTMLResponse(content=content)