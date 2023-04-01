from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(
    prefix="/inventory",
    tags=["inventory"]
)

class InventoryBase(BaseModel):
    description : str
    price : float
    stock : int

#สร้าง data จำลอง เพื่อให้สำหรับ crud ข้อมูล
fake_inventory = [
    {"description": "pencil", "price": 12, "stock":20},
    {"description": "pen", "price": 15, "stock":20},
    {"description": "notebook", "price": 20, "stock":20},
]

#การ quiry paramiter
@router.get("/")
def get_all_inventory(version: int = 1):
    if version > 1:
        return {"msg" : "data not available"}
    else:
        return fake_inventory

# @app.get("/")
# def hello_word():
#     return fake_inventory

# @app.get("/")
# def hello_word():
#     return{"hello":"world"}

# ส่วนของ path paramiter
@router.get("/{id}")
def inventory_by_id(id:int):
    # สร้างตัวแปรก่อน
    item = fake_inventory[id - 1]
    return item

# 1.การ post ข้อมูลเพื่อ add ในฐานข้อมูลชื่อ fake_inventory โดย กำหนด parameter สำหรับรับค่าก่อน post_api(inventory) ประเภทข้อมูลเป็น invetorybase 
# @app.post("/")
# def post_api(inventory : InventoryBase):
#     print(inventory)
#     return {"hello":"post"}

# 2.การ post ข้อมูลเพื่อ add ในฐานข้อมูลชื่อ fake_inventory โดย กำหนด parameter สำหรับรับค่าก่อน post_api(inventory) ประเภทข้อมูลเป็น invetorybase แล้วให้แสดงข้อมูลใหม่ ใช้คำสั่ง  append
@router.post("/")
def post_api(inventory : InventoryBase):
    fake_inventory.append(inventory)
    return fake_inventory

# การ post แบบปกติไม่มีการส่งค่าใดๆ
# @app.post("/")
# def post_api():
#     return {"hello":"post"}

# update ข้อมูลใดข้อมูลหนึ่ง แล้วส่งค่าที่ update มาแสดง
@router.put("/{id}")
def put_api(id:int, inventory : InventoryBase):
    fake_inventory[id - 1].update(**inventory.dict())
    item = fake_inventory[id - 1]
    return item

# @app.put("/")
# def put_api():
#     return {"hello":"put"}

# การ delete โดยระบบตำแหน่งของข้อมูล ใช้คำสั่ง  pop
@router.delete("/{id}")
def delete_api(id : int ):
    item = fake_inventory.pop(id - 1)
    return item


# @app.delete("/")
# def delete_api():
#     return {"hello":"delete"}