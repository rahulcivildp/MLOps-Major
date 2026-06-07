from misc import (
    load_data,
    show_sample_image,
    split_data,
    evaluate_model,
    modified_view
)
import joblib


def test_model():
    # Load saved model
    
    print("Loading saved model...")
    model = joblib.load(
        "saved_models/savedmodel.pth"
    )

    print("Loading dataset...")
    # Load dataset
    data = load_data()
    X, y = data

    # Same split as training
    X_train, X_test, y_train, y_test = split_data(data)

    # Select sample image
    sample_index = 18

    sample_image = X[sample_index].reshape(1, -1)
    actual_label = y[sample_index]


    # Predict
    prediction = model.predict(sample_image)

    # Accuracy
    accuracy = evaluate_model(
        model,
        X_test,
        y_test
    )

    modified_view(sample_index, actual_label, prediction, accuracy)

    show_sample_image(X, y, prediction, index=sample_index)



if __name__ == "__main__":
    test_model()