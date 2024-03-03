from pydantic import BaseModel
from typing import Any, Optional

class VehicleModelItem(BaseModel):
    rnr: str
    gruppe: str
    kurzname: str
    langtext: str
    info: str
    sort: str
    lagerort: str
    lteartikel: str
    businessUnit: str
    vondat: Optional[str]
    bisdat: Optional[str]
    hu: Optional[str]
    asu: Optional[str]
    createdOn: Optional[str]
    editedOn: str
    fuelConsumption: str
    priceInformation: Optional[str]
    safetyCheckDate: Optional[str]
    tachographTestDate: Any
    gb1: str
    ownerId: Optional[str]
    userId: Optional[str]
    externalId: Optional[str]
    vin: Optional[str]
    labelIds: Optional[str]
    bleGroupEnum: Optional[str]
    profilePictureUrl: Optional[str] = None
    thumbPathUrl: Optional[str] = None


class AuthResModel(BaseModel):
    oauth: dict
    userInfo: dict
    permissions: list
    apiVersion: str
    showPasswordPrompt: bool


class LabelModel(BaseModel):
    id: int
    enum: str
    displayText: str
    colorCode: str
    baseEntity: str
    isAbstract: bool