
from sklearn.datasets import fetch_olivetti_faces
from sklearn.model_selection import train_test_split 
from sklearn.tree import DecisionTreeClassifier 
from sklearn.metrics import accuracy_score

import pandas as pd

def load_data(): 
    data = fetch_olivetti_faces()

    X = data.data
    y = data.target

    return X, y

def get_decision_tree_model():  

    model = DecisionTreeClassifier(
        random_state=42
    )

    return model

def split_data(data):

    X, y = data

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.3,
        random_state=42
    )

    return X_train, X_test, y_train, y_test


def train_model(model, X_train, y_train):

    model.fit(X_train, y_train)

    return model


def evaluate_model(
    model,
    X_test,
    y_test
):
    predictions = model.predict(X_test)

    accuracy = accuracy_score(
        y_test,
        predictions
    )

    return accuracy

def show_sample_image(X, y, prediction, index=0):
    import matplotlib.pyplot as plt

    plt.imshow(X[index].reshape(64, 64), cmap="gray")
    plt.title(f"Example Olivetti Face (Subject {y[index]}), Predicted: {prediction[0]}")
    plt.axis("off")
    plt.show()

def modified_view(sample_index, actual_label, prediction, accuracy):
    result_summary = pd.DataFrame(
        [
            {"Metric": "Test Accuracy", "Value": f"{accuracy:.4f}"},
            {"Metric": "Sample Index", "Value": sample_index},
            {"Metric": "Actual Label", "Value": actual_label},
            {"Metric": "Predicted Label", "Value": prediction[0]},
        ]
    )

    print("\n" + "=" * 60)
    print("TEST MODEL RESULTS".center(60))
    print("=" * 60 + "\n")

    # Nicely formatted table with underlined headers
    header1 = "Metric"
    header2 = "Value"
    col1 = result_summary[header1].astype(str)
    col2 = result_summary[header2].astype(str)
    w1 = max(col1.map(len).max(), len(header1)) + 4
    w2 = max(col2.map(len).max(), len(header2)) + 4
        # Format table to match screenshot: Metric left, Value right, centered overall
    header1 = "Metric"
    header2 = "Value"
    col1 = result_summary[header1].astype(str)
    col2 = result_summary[header2].astype(str)
    w1 = max(col1.map(len).max(), len(header1))
    w2 = max(col2.map(len).max(), len(header2))
    gap = 6

    table_width = w1 + gap + w2
    left_pad = max(0, (60 - table_width) // 2)
    pad = " " * left_pad

    header_line = header1.center(w1) + (" " * gap) + header2.center(w2)
    underline_line = ("-" * len(header1)).center(w1) + (" " * gap) + ("-" * len(header2)).center(w2)

    print(pad + header_line)
    print(pad + underline_line)

    for _, row in result_summary.iterrows():
        row_line = str(row[header1]).center(w1) + (" " * gap) + str(row[header2]).center(w2)
        print(pad + row_line)

    print("\n" + "=" * 60 + "\n")

def modified_view_train(model_name, model_filename, accuracy):
    # Prepare table rows
    rows = [
        ("Accuracy", f"{accuracy:.6f}"),
        ("Model saved", model_filename),
    ]

    header1 = "Metric"
    header2 = "Value"
    w1 = max(len(header1), max(len(r[0]) for r in rows))
    w2 = max(len(header2), max(len(r[1]) for r in rows))
    gap = 6

    table_width = w1 + gap + w2
    left_pad = max(0, (60 - table_width) // 2)
    pad = " " * left_pad

    header_line = header1.ljust(w1) + (" " * gap) + header2.ljust(w2)
    underline_line = ("-" * len(header1)).ljust(w1) + (" " * gap) + ("-" * len(header2)).ljust(w2)

    lines = []
    lines.append("\n" + "=" * 60)
    lines.append(f"Model: {model_name}".center(60))
    lines.append("=" * 60 + "\n")
    lines.append(pad + header_line)
    lines.append(pad + underline_line)
    for k, v in rows:
        lines.append(pad + k.ljust(w1) + (" " * gap) + v.ljust(w2))
    lines.append("\n" + "=" * 60 + "\n")

    result = "\n".join(lines)

    print(result)
    return result