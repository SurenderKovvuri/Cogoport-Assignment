#!/usr/bin/env python
# coding: utf-8

# In[1]:


# crud.py
from sqlalchemy.orm import Session

def create_configuration(db: Session, configuration: ConfigurationCreate):
    db_configuration = Configuration(**configuration.dict())
    db.add(db_configuration)
    db.commit()
    db.refresh(db_configuration)
    return db_configuration

def get_configuration(db: Session, country_code: str):
    return db.query(Configuration).filter(Configuration.country_code == country_code).first()

def update_configuration(db: Session, country_code: str, updated_config: ConfigurationUpdate):
    db_configuration = get_configuration(db, country_code)
    if db_configuration:
        for key, value in updated_config.dict().items():
            setattr(db_configuration, key, value)
        db.commit()
        db.refresh(db_configuration)
        return db_configuration
    return None

def delete_configuration(db: Session, country_code: str):
    db_configuration = get_configuration(db, country_code)
    if db_configuration:
        db.delete(db_configuration)
        db.commit()
        return db_configuration
    return None

