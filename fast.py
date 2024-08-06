from fastapi import FastAPI, HTTPException


app = FastAPI()



BANDS = [
    {'id':1, 'nome': 'legião urbano', 'genre': 'Mpb'},
    {'id':2, 'nome': 'mamonas assasinas', 'genre': 'Rock'},
    {'id':3, 'nome': 'cbrj', 'genre': 'Rock nacional '},
    {'id':4, 'nome': 'ira', 'genre': 'Rock nacional'},
    ]
@app.get('/bands')
async def bands() -> list[dict]:
    return BANDS
 
@app.get('/bands/{band_id}')
async def about(band_id: int)-> dict:
    band = next((b for b in BANDS if b['id'] == band_id),None)
    if band is None: 
        #status code 404
        raise HTTPException(status_code=404,detail='Bandas not found')
    return band

@app.get('/bands/genre/{genre}')
async def bands_for_genre(genre:GenreURLChoices) -> list[dict]:
    return[ 
        b for b in bands if b ['genre'].lower() == genre.value()
        ]
