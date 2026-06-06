# End-to-End MLOps Pipeline with Decision Tree Classifier

## Overview

This project demonstrates a complete Machine Learning Operations (MLOps) workflow using the Olivetti Faces dataset from Scikit-Learn. The objective is to train, evaluate, automate, containerize, and deploy a machine learning model while following industry-standard development practices.

The project follows a structured Git branching strategy and incorporates GitHub Actions for Continuous Integration and Continuous Deployment (CI/CD).

---

## Dataset

**Dataset:** Olivetti Faces Dataset

* Total Images: 400
* Subjects: 40
* Images per Subject: 10
* Image Size: 64 × 64 pixels
* Source: Scikit-Learn

---

## Model

**Algorithm:** Decision Tree Classifier

The model is trained on 70% of the dataset and evaluated on the remaining 30%.

---

## Project Structure

```text
MLOps-Major/
│
├── train.py
├── test.py
├── misc.py
├── requirements.txt
├── README.md
│
├── saved_models/
│   └── savedmodel.pth
│
├── results/
│   └── metrics.txt
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── templates/
│   └── index.html
│
├── k8s/
│   ├── deployment.yaml
│   └── service.yaml
│
└── Dockerfile
```

---

## Installation

Clone the repository:

```bash
git clone git@github.com:rahulcivildp/MLOps-Major.git
cd MLOps-Major
```

Create a new Conda environment:

```bash
conda create -n digit python=3.14
```

Activate the environment:

```bash
conda activate digit
```


Install dependencies:

```bash
python -m pip install -r requirements.txt
```

---

## Train the Model

Run:

```bash
python train.py
```

This will:

* Load the Olivetti Faces dataset
* Split data into training and testing sets
* Train a Decision Tree Classifier
* Save the model as `savedmodel.pth`
* Generate training metrics

---

## Test the Model

Run:

```bash
python test.py
```

This will:

* Load the saved model
* Evaluate model performance
* Display test accuracy
* Predict a sample face image

---

## CI/CD Pipeline

GitHub Actions automatically runs on every push.

The workflow performs:

1. Repository checkout
2. Python environment setup
3. Dependency installation
4. Model training
5. Model testing
6. Accuracy verification

Workflow file:

```text
.github/workflows/ci.yml
```

---

## Docker

Build the Docker image:

```bash
docker build -t rahulcivildp/olivetti-face-app:0.1 .
```

Run the container:

```bash
docker compose up -d
```

---

## Kubernetes

Deploy the application:

```bash
kubectl apply -f kubernetes/deployment.yaml
kubectl apply -f kubernetes/service.yaml
```

Verify deployment:

```bash
kubectl get pods
kubectl get services
```

The deployment maintains three replicas to ensure high availability.

---

## Git Branch Strategy

### main

Initial project setup and documentation.

### dev

Model development, training, testing, and CI/CD workflow.

### docker_cicd

Dockerization, Kubernetes deployment, and automation.

---

## Technologies Used

* Python
* Scikit-Learn
* Pandas
* Joblib
* Matplotlib
* Git & GitHub
* GitHub Actions
* Docker
* Kubernetes
* Flask

---

## Scribe

Tanmay Sarkar G25AI1050

MLOps Major Assignment
PGD Program
