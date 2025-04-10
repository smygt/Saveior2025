from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
import models, schemas
from database import get_db

router = APIRouter(
    prefix="/folders",
    tags=["folders"]
)

@router.post("/", response_model=schemas.Folder)
def create_folder(
    folder: schemas.FolderCreate,
    db: Session = Depends(get_db)
):
    db_folder = models.Folder(**folder.dict())
    db.add(db_folder)
    db.commit()
    db.refresh(db_folder)
    return db_folder

@router.get("/", response_model=List[schemas.Folder])
def read_folders(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    folders = db.query(models.Folder).offset(skip).limit(limit).all()
    return folders

@router.get("/{folder_id}", response_model=schemas.Folder)
def read_folder(
    folder_id: int,
    db: Session = Depends(get_db)
):
    folder = db.query(models.Folder).filter(models.Folder.id == folder_id).first()
    if folder is None:
        raise HTTPException(status_code=404, detail="Folder not found")
    return folder

@router.put("/{folder_id}", response_model=schemas.Folder)
def update_folder(
    folder_id: int,
    folder: schemas.FolderCreate,
    db: Session = Depends(get_db)
):
    db_folder = db.query(models.Folder).filter(models.Folder.id == folder_id).first()
    if db_folder is None:
        raise HTTPException(status_code=404, detail="Folder not found")
    
    for key, value in folder.dict().items():
        setattr(db_folder, key, value)
    
    db.commit()
    db.refresh(db_folder)
    return db_folder

@router.delete("/{folder_id}")
def delete_folder(
    folder_id: int,
    db: Session = Depends(get_db)
):
    db_folder = db.query(models.Folder).filter(models.Folder.id == folder_id).first()
    if db_folder is None:
        raise HTTPException(status_code=404, detail="Folder not found")
    
    db.delete(db_folder)
    db.commit()
    return {"message": "Folder deleted successfully"} 