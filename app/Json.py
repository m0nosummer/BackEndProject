from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class BattleData(BaseModel):
    playerAttack: int
    monsterName: str
    monsterHp: int
    monsterDefense: int

class BattleResult(BaseModel):
    monsterName: str
    remainingMonsterHp: int

@app.post("/battle/", response_model=BattleResult)
async def battle(battleData: BattleData):
    remaining_hp = battleData.monsterHp - (battleData.playerAttack - battleData.monsterDefense)
    return BattleResult(monsterName=battleData.monsterName, remainingMonsterHp=remaining_hp)