from fastapi import FastAPI, HTTPException
from typing import Dict

app = FastAPI()


memos: Dict[int, str] = {}
memo_ids : int = 1

@app.post("/memos/post/") # POST /memos/post/?memo= [content]
async def create_memo(memo: str):
    global memo_ids
    memos[memo_ids] = memo
    memo_ids += 1
    return {"id" : memo_ids-1, "content" : memo}

@app.get("/memos/readall")
async def read_memos():
    return memos

@app.get("/memos/read/{memo_id}")
async def read_memo(memo_id: int):
    if memo_id in memos:
        return memos[memo_id]
    else:
        raise HTTPException(status_code=404, detail="Memo not found")
    
@app.put("/memos/update/{memo_id}")
async def update_memo(memo_id: int, memo: str):
    if memo_id in memos:
        memos[memo_id] = memo
        return memo
    else:
        raise HTTPException(status_code=404, detail="Memo not found")
    
@app.delete("/memos/delete/{memo_id}")
async def delete_memo(memo_id: int):
    if memo_id in memos:
        del memos[memo_id]
        return {"message": "Memo deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Memo not found")