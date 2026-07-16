import os

from src.pipelines.train_pipeline import TrainPipeline
from src.pipelines.predict_pipeline import PredictPipeline, CustomData


def train():
    dataset_path = os.path.join("notebook", "Housing.csv")

    pipeline = TrainPipeline()
    report = pipeline.run_pipeline(dataset_path)

    print("\nTraining Completed")
    print(report)


def predict():

    custom_data = CustomData(
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
        furnishingstatus="furnished",
    )

    df = custom_data.get_data_as_dataframe()

    pipeline = PredictPipeline()

    prediction = pipeline.predict(df)

    print(f"\nPredicted House Price: {prediction[0]:,.2f}")


if __name__ == "__main__":

    # Uncomment to train the model
    # train()

    # Uncomment to test prediction
    predict()