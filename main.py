
import os

import requests
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

load_dotenv()

URL = os.getenv(
    "LLM_URL"
)
MODEL = os.getenv("LLM_MODEL")
KEY = os.getenv("LLM_API_KEY")

app = FastAPI()


class MessageRequest(BaseModel):
    system: str
    user: str
    temperature: float = 0.2


@app.post("/")
def appeler_llm(data: MessageRequest) -> str:
    headers = {
        "Authorization": f"Bearer {KEY}",
        "Content-Type": "application/json",
    }

    try:
        reponse = requests.post(
            URL,
            headers=headers,
            json={
                "model": MODEL,
                "temperature": data.temperature,
                "messages": [
                    {"role": "system", "content": data.system},
                    {"role": "user", "content": data.user},
                ],
            },
            timeout=180,
        )
        reponse.raise_for_status()

        return reponse.json()["choices"][0]["message"]["content"]

    except requests.RequestException as erreur:
        raise HTTPException(
            status_code=502,
            detail=f"Erreur lors de l'appel au LLM : {erreur}",
        )
