from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text, DateTime, Table
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base

# Association tables
link_tags = Table(
    'link_tags',
    Base.metadata,
    Column('link_id', Integer, ForeignKey('links.id', ondelete='CASCADE')),
    Column('tag_id', Integer, ForeignKey('tags.id', ondelete='CASCADE'))
)

folder_links = Table(
    'folder_links',
    Base.metadata,
    Column('folder_id', Integer, ForeignKey('folders.id', ondelete='CASCADE')),
    Column('link_id', Integer, ForeignKey('links.id', ondelete='CASCADE'))
)

class Folder(Base):
    __tablename__ = "folders"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    parent_id = Column(Integer, ForeignKey('folders.id', ondelete='CASCADE'), nullable=True)
    created_at = Column(DateTime(timezone=True), default=datetime.utcnow)
    updated_at = Column(DateTime(timezone=True), default=datetime.utcnow, onupdate=datetime.utcnow)

    parent = relationship("Folder", remote_side=[id], backref="children")
    links = relationship("Link", secondary=folder_links, back_populates="folders")

class Link(Base):
    __tablename__ = "links"

    id = Column(Integer, primary_key=True, index=True)
    url = Column(Text, index=True)
    title = Column(String, index=True)
    short_summary = Column(Text)
    long_summary = Column(Text)
    source_website = Column(String)
    image_url = Column(Text)
    created_at = Column(DateTime(timezone=True), default=datetime.utcnow)
    updated_at = Column(DateTime(timezone=True), default=datetime.utcnow, onupdate=datetime.utcnow)

    folders = relationship("Folder", secondary=folder_links, back_populates="links")
    tags = relationship("Tag", secondary=link_tags, back_populates="links")

class Tag(Base):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    is_auto_generated = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), default=datetime.utcnow)

    links = relationship("Link", secondary=link_tags, back_populates="tags") 