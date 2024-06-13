#!/usr/bin/env python
# coding: utf-8

# In[1]:


# schemas.py
from pydantic import BaseModel, Field
from typing import Dict

class ConfigurationBase(BaseModel):
    country_code: str = Field(..., example="IN")
    requirements: Dict[str, str] = Field(..., example={"Business Name": "string", "PAN": "string", "GSTIN": "string"})

class ConfigurationCreate(ConfigurationBase):
    pass

class ConfigurationUpdate(ConfigurationBase):
    pass

class Configuration(ConfigurationBase):
    id: int

    class Config:
        orm_mode = True

