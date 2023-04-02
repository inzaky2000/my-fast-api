from fastapi import APIRouter, Depends
from typing import List
# from pydantic import BaseModel

from sqlalchemy.orm import Session
from models.database import get_db
from models.inventory.inventory_model import InventoryBase, InventoryDisplayBase

from routers.inventory import inventory_controller

router = APIRouter(
    prefix="/inventory",
    tags=["inventory"]
)

# class InventoryBase(BaseModel):
#     description : str
#     price : float
#     stock : int

# #สร้าง data จำลอง เพื่อให้สำหรับ crud ข้อมูล
# fake_inventory = [
#     {"description": "pencil", "price": 12, "stock":20},
#     {"description": "pen", "price": 15, "stock":20},
#     {"description": "notebook", "price": 20, "stock":20},
# ]

#การ quiry paramiter
@router.get("/",response_model=List[InventoryDisplayBase])
def get_all_inventory(db: Session = Depends(get_db)):
    return inventory_controller.read_inventory(db)

# @app.get("/")
# def hello_word():
#     return fake_inventory

# @app.get("/")
# def hello_word():
#     return{"hello":"world"}

# ส่วนของ path paramiter
# @router.get("/{id}")
# def inventory_by_id(id:int):
#     # สร้างตัวแปรก่อน
#     pass
@router.get("/{id}")
def inventory_by_id(id: int, db: Session = Depends(get_db)):
    return inventory_controller.read_inventory_by_id(db, id)


# 1.การ post ข้อมูลเพื่อ add ในฐานข้อมูลชื่อ fake_inventory โดย กำหนด parameter สำหรับรับค่าก่อน post_api(inventory) ประเภทข้อมูลเป็น invetorybase 
# @app.post("/")
# def post_api(inventory : InventoryBase):
#     print(inventory)
#     return {"hello":"post"}


@router.post("/")
def create_inventory(request:InventoryBase, db:Session = Depends(get_db)):
    return inventory_controller.create(db, request)

# 2.การ post ข้อมูลเพื่อ add ในฐานข้อมูลชื่อ fake_inventory โดย กำหนด parameter สำหรับรับค่าก่อน post_api(inventory) ประเภทข้อมูลเป็น invetorybase แล้วให้แสดงข้อมูลใหม่ ใช้คำสั่ง  append
# @router.post("/")
# def post_api(inventory : InventoryBase):
#     fake_inventory.append(inventory)
#     return fake_inventory

# การ post แบบปกติไม่มีการส่งค่าใดๆ
# @app.post("/")
# def post_api():
#     return {"hello":"post"}

# update ข้อมูลใดข้อมูลหนึ่ง แล้วส่งค่าที่ update มาแสดง
@router.put("/{id}")
def put_api(id:int,request: InventoryBase ,db: Session = Depends(get_db)):
    return inventory_controller.update(db, id, request)

    # fake_inventory[id - 1].update(**inventory.dict())
    # item = fake_inventory[id - 1]
    # return item

# @app.put("/")
# def put_api():
#     return {"hello":"put"}

# การ delete โดยระบบตำแหน่งของข้อมูล ใช้คำสั่ง  pop
@router.delete("/{id}")
def delete_api(id : int, db:Session=Depends(get_db)):
    return inventory_controller.delete(db,id)
    # item = fake_inventory.pop(id - 1)
    # return item


# @app.delete("/")
# def delete_api():
#     return {"hello":"delete"}