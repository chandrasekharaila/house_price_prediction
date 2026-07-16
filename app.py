from fastapi import FastAPI
from pydantic import BaseModel
from src.pipelines.predict_pipeline import CustomData, PredictPipeline

class HouseData(BaseModel):
    area: float
    bedrooms: int
    bathrooms: int
    stories: int
    parking: int
    mainroad: str
    guestroom: str
    basement: str
    hotwaterheating: str
    airconditioning: str
    prefarea: str
    furnishingstatus: str

app = FastAPI(
    title="House price prediction API",
    version="1.0"
)


@app.get("/")
async def read_root():
    return {
        "message": "House price prediction API"
    }




@app.post("/predict")
async def predict(data: HouseData):

    custom_data = CustomData(
        area=data.area,
        bedrooms=data.bedrooms,
        bathrooms= data.bathrooms,
        stories = data.stories,
        parking= data.parking,
        mainroad= data.mainroad,
        guestroom= data.guestroom,
        basement= data.basement,
        hotwaterheating=data.hotwaterheating,
        airconditioning=data.airconditioning,
        prefarea=data.prefarea,
        furnishingstatus=data.furnishingstatus
    )

    df = custom_data.get_data_as_dataframe()

    prediction_pipeline = PredictPipeline()

    prediction = prediction_pipeline.predict(df)

    return {
        "predicted_price": float(prediction[0])
    }