from fastapi import FastAPI, HTTPException
from uuid import uuid4

app = FastAPI()

"""

    - /create-table : Créer une table. -> table-ID
    - /add-member (table-ID, firstname, lastname) : Ajouter une personne à une table
    - /settle-table (table-ID, location-ID) : Associer un groupe-table à un numéro de table
    - /table-info (table-ID) : Renvoie les infos sur la table (nb personnes, noms...)

    - Gérer la partie google auth

"""

# Il faudra utiliser une base de donnée plutot qu'un simple dict

tables = {}

@app.get("/")
async def root():
    return {"message": "Coucou le LP"}

@app.post("/create-table")
async def create_table_route():
    new_table_ID = uuid4()
    while new_table_ID in tables.keys():
        new_table_ID = uuid4()
    tables[new_table_ID] = []
    return {"table-ID": new_table_ID,}

@app.put("/add-member")
async def add_member_route(tableid: str, firstname: str, lastname: str):

    return {"status": "not ready"}

    # Verify the tableid is valid
    if tableid not in tables.keys():
        return {"status": "table not found"}
    return {"status": "ok", "table-ID": tableid}
    # add the person to the table   

@app.put("/settle-table")
async def settle_table_route(tableid: str, locationid: str):
    return {"status": "not ready"}
    # match an e-table and an actual table

@app.get("/table-info")
async def table_info_route(tableid: str):
    return {"status": "not ready"}
    # information about the table
