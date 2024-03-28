
from fastapi import APIRouter, Depends, HTTPException, status, Request
from uuid import UUID
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from configuration import config
from src.file_manager import FileManager
from src.file_manager import FileManager, FileZipper, FileSendler



router = APIRouter(
    prefix="/interview",
    tags=["interview"]
)


@router.get("/get_file/{uuid}")
async def get_file(uuid: UUID,  creditionals: HTTPBasicCredentials = Depends(HTTPBasic())):
    if creditionals.username != config['auth_info']['basic']['username'] or \
       creditionals.username != config['auth_info']['basic']['password']:
    
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
    file_manager = FileManager(config)
    result = await file_manager.fetch_file_by_uuid(uuid)
    return result


@router.get("/download_zip")
async def download_zip(request: Request, creditionals: HTTPBasicCredentials = Depends(HTTPBasic())):

    cookies = request.cookies
    
    if creditionals.username != config['auth_info']['zip_auth']['username'] or \
       creditionals.password != config['auth_info']['zip_auth']['password'] or \
       cookies.get("mojo") != config['auth_info']['zip_cookies']['value']:
            
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized")
    
    try:
         
         file_zipper = FileZipper(config)
         zip_path = await file_zipper.zip_files(temp_dir=config['files_info']['temp_dir'])
         responce = await FileSendler.send_zip_file(zip_path)
         return responce
    except Exception as e:
         raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))