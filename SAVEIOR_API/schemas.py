from pydantic import BaseModel
from typing import Optional, List, ForwardRef
from datetime import datetime

# Folder schemas
class FolderBase(BaseModel):
    name: str
    parent_id: Optional[int] = None

class FolderCreate(FolderBase):
    pass

class Folder(FolderBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

# Tag schemas
class TagBase(BaseModel):
    name: str
    is_auto_generated: bool = False

class TagCreate(TagBase):
    pass

class Tag(TagBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

# Link schemas
class LinkBase(BaseModel):
    url: str
    title: str
    short_summary: Optional[str] = None
    long_summary: Optional[str] = None
    source_website: Optional[str] = None
    image_url: Optional[str] = None

class LinkCreate(LinkBase):
    folder_ids: Optional[List[int]] = None
    tag_ids: Optional[List[int]] = None

class Link(LinkBase):
    id: int
    created_at: datetime
    updated_at: datetime
    folders: List[Folder] = []
    tags: List[ForwardRef('Tag')] = []

    class Config:
        from_attributes = True

# Token schemas
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

# Update forward references
Link.model_rebuild() 