

from src.pipelines.predict_pipeline import PredictPipeline, CustomData

data = CustomData(
    area=7420,
    bedrooms=4,
    bathrooms=2,
    stories=3,
    parking=2,
    mainroad="yes",
    guestroom="no",
    basement="no",
    hotwaterheating="no",
    airconditioning="yes",
    prefarea="yes",
    furnishingstatus="furnished"
)

df = data.get_data_as_dataframe()

pipeline = PredictPipeline()

prediction = pipeline.predict(df)

print(prediction)


# from src.pipelines.train_pipeline import TrainPipeline
# import os
# TP = TrainPipeline()
# dataset_path = os.path.join("notebook","Housing.csv")
# TP.run_pipeline(dataset_path)