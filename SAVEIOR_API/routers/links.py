from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
import models, schemas
from database import get_db

router = APIRouter(
    prefix="/links",
    tags=["links"]
)

@router.post("/", response_model=schemas.Link)
def create_link(
    link: schemas.LinkCreate,
    db: Session = Depends(get_db)
):
    link_data = link.dict(exclude={'folder_ids', 'tag_ids'})
    db_link = models.Link(**link_data)
    
    if link.folder_ids:
        folders = db.query(models.Folder).filter(
            models.Folder.id.in_(link.folder_ids)
        ).all()
        db_link.folders = folders
    
    if link.tag_ids:
        tags = db.query(models.Tag).filter(
            models.Tag.id.in_(link.tag_ids)
        ).all()
        db_link.tags = tags
    
    db.add(db_link)
    db.commit()
    db.refresh(db_link)
    return db_link

@router.get("/", response_model=List[schemas.Link])
def read_links(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    links = db.query(models.Link).offset(skip).limit(limit).all()
    return links

@router.get("/{link_id}", response_model=schemas.Link)
def read_link(
    link_id: int,
    db: Session = Depends(get_db)
):
    link = db.query(models.Link).filter(models.Link.id == link_id).first()
    if link is None:
        raise HTTPException(status_code=404, detail="Link not found")
    return link

@router.put("/{link_id}", response_model=schemas.Link)
def update_link(
    link_id: int,
    link: schemas.LinkCreate,
    db: Session = Depends(get_db)
):
    db_link = db.query(models.Link).filter(models.Link.id == link_id).first()
    if db_link is None:
        raise HTTPException(status_code=404, detail="Link not found")
    
    link_data = link.dict(exclude={'folder_ids', 'tag_ids'})
    for key, value in link_data.items():
        setattr(db_link, key, value)
    
    if link.folder_ids:
        folders = db.query(models.Folder).filter(
            models.Folder.id.in_(link.folder_ids)
        ).all()
        db_link.folders = folders
    
    if link.tag_ids:
        tags = db.query(models.Tag).filter(
            models.Tag.id.in_(link.tag_ids)
        ).all()
        db_link.tags = tags
    
    db.commit()
    db.refresh(db_link)
    return db_link

@router.delete("/{link_id}")
def delete_link(
    link_id: int,
    db: Session = Depends(get_db)
):
    db_link = db.query(models.Link).filter(models.Link.id == link_id).first()
    if db_link is None:
        raise HTTPException(status_code=404, detail="Link not found")
    
    db.delete(db_link)
    db.commit()
    return {"message": "Link deleted successfully"} 