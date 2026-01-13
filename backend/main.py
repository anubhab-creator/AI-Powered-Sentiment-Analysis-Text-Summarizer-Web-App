from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
import pandas as pd
import sys
sys.path.append("backend")

from auth import authenticate_user

from auth import authenticate_user, create_access_token, SECRET_KEY, ALGORITHM
from models import sentiment_pipeline, summarizer_pipeline

app = FastAPI(title="AI Sentiment & Summarizer API")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload.get("sub")
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

# AUTH 
@app.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Incorrect credentials")
    token = create_access_token({"sub": user["username"]})
    return {"access_token": token, "token_type": "bearer"}

#  SENTIMENT 
@app.post("/sentiment")
def sentiment_analysis(text: str, user=Depends(get_current_user)):
    result = sentiment_pipeline(text)[0]

    label_map = {
        "LABEL_0": ("Negative 😞", "The text expresses dissatisfaction or criticism."),
        "LABEL_1": ("Positive 😊", "The text expresses satisfaction or appreciation.")
    }

    sentiment, explanation = label_map.get(
        result["label"], 
        ("Neutral 😐", "The sentiment is mixed or unclear.")
    )

    return {
        "sentiment": sentiment,
        "confidence": f"{result['score'] * 100:.2f}%",
        "explanation": explanation
    }

# SUMMARIZATION
@app.post("/summarize")
def summarize(text: str, user=Depends(get_current_user)):
    if len(text.strip()) < 50:
        return {
            "summary": "Text is too short to summarize meaningfully.",
            "note": "Please provide a longer paragraph for better results."
        }

    result = summarizer_pipeline(
        text,
        max_length=130,
        min_length=30,
        do_sample=False
    )[0]

    return {
        "summary": result["summary_text"],
        "original_length": len(text.split()),
        "summary_length": len(result["summary_text"].split())
    }


#  FILE UPLOAD 
@app.post("/analyze-csv")
def analyze_csv(file: bytes, user=Depends(get_current_user)):
    df = pd.read_csv(pd.io.common.BytesIO(file))
    df["sentiment"] = df["text"].apply(lambda x: sentiment_pipeline(x)[0]["label"])
    return df.head(10).to_dict()
