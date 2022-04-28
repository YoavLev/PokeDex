from fastapi import FastAPI, HTTPException, Path
from fastapi.middleware.cors import CORSMiddleware
from app.get_pokemon_data import PokemonData


app = FastAPI()

origins = [
    "http://localhost:3000",
    "localhost:3000"
]
# Allow front-end to send cross origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/{poke_id}")
async def root(poke_id: int = Path("The ID of the pokemon to get", gt=0, le=898)):
    """
    create new pokemon object with the given ID. Send the object as dict(valid json)
    :param poke_id: greater than 0 or lower than 899. Returns 422 error if not valid.
    :return:
    """
    try:
        return await PokemonData.fetch_pokemon_by_id(poke_id)  # returns PokemonData object as Dict, Could dump to JSON
    except Exception as e:
        # If something is missing, return 404 error.
        print("Error on fetching API: ", e)
        raise HTTPException(status_code=404, detail='Not found')
