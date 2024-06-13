#!/usr/bin/env python
# coding: utf-8

# In[1]:


# main.py
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import engine, Base, get_db

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.post("/create_configuration", response_model=Configuration)
def create_configuration(configuration: ConfigurationCreate, db: Session = Depends(get_db)):
    return crud.create_configuration(db=db, configuration=configuration)

@app.get("/get_configuration/{country_code}", response_model=Configuration)
def get_configuration(country_code: str, db: Session = Depends(get_db)):
    db_configuration = crud.get_configuration(db, country_code=country_code)
    if db_configuration is None:
        raise HTTPException(status_code=404, detail="Configuration not found")
    return db_configuration

@app.post("/update_configuration", response_model=Configuration)
def update_configuration(configuration: ConfigurationUpdate, db: Session = Depends(get_db)):
    db_configuration = crud.update_configuration(db=db, country_code=configuration.country_code, updated_config=configuration)
    if db_configuration is None:
        raise HTTPException(status_code=404, detail="Configuration not found")
    return db_configuration

@app.delete("/delete_configuration/{country_code}", response_model=Configuration)
def delete_configuration(country_code: str, db: Session = Depends(get_db)):
    db_configuration = crud.delete_configuration(db=db, country_code=country_code)
    if db_configuration is None:
        raise HTTPException(status_code=404, detail="Configuration not found")
    return db_configuration

