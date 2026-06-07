
from misc import (
    evaluate_model,
    split_data,
    load_data,
    train_model,
    get_decision_tree_model,
    modified_view_train
)

import joblib


def main():

    print("Loading dataset...")

    # Load dataset
    df = load_data()

    print("Dataset loaded successfully")

    # Split dataset

    # Preprocess
    print("Preprocessing data...")
    X_train, X_test, y_train, y_test = split_data(df)

    model_name = f"DecisionTreeClassifier"

    # Train model
    model = get_decision_tree_model()

    # Train
    trained_model = train_model(
        model,
        X_train,
        y_train
    )

    # Save model
    model_filename = f"saved_models/savedmodel.pth"

    joblib.dump(
        trained_model,
        model_filename
    )

    # Evaluate
    accuracy = evaluate_model(
        model,
        X_test,
        y_test
    )

    result = modified_view_train(model_name, model_filename, accuracy)

    # Save to file
    with open("results/metrics.txt", "a") as file:
        file.write(result + "\n")
    

if __name__ == "__main__":
    main()