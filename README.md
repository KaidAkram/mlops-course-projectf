# mlops-course-project


# Healthcare Symptom Discovery - MLOps Pipeline

## 📌 Project Overview
This project implements an end-to-end **MLOps (Machine Learning Operations)** lifecycle for a healthcare Association Rule Mining system.

The objective is to discover hidden patterns in patient symptom data (e.g., *"If a patient has a cough and fever, they likely have fatigue"*) using the **Apriori Algorithm**. Unlike a static notebook, this project is a fully automated, versioned, and deployable software product.

## 🛠️ Tech Stack
* **Algorithm:** Apriori (Association Rule Mining via `mlxtend`)
* **Tracking & Registry:** [Weights & Biases (W&B)](https://wandb.ai/)
* **Deployment:** FastAPI
* **Automation:** Bash Pipeline

## 📂 Project Structure
```text
mlops-course-project/
├── src/
│   ├── train.py          # Training script (Mines rules & logs to W&B)
│   ├── api.py            # Deployment script (FastAPI server)
├── pipeline.sh           # Automated orchestration script
├── kaggle_notebook.ipynb # Original EDA and research
├── rules_model.pkl       # Serialized model artifact
└── README.md             # Documentation
```

# Clone the repo
git clone [https://github.com/KaidAkram/mlops-course-project.git](https://github.com/KaidAkram/mlops-course-project.git)
cd mlops-course-project

# Install dependencies
pip install pandas mlxtend wandb fastapi uvicorn joblib

You need a W&B API key for experiment tracking.

    Get your key from wandb.ai/authorize.

    The training script will prompt you to log in on the first run.

⚡ Automated Pipeline

We implemented a single-command orchestration script that handles the entire lifecycle:

    Retrains the model on fresh data.

    Versions the model to the W&B Cloud Registry.

    Deploys the API locally.

    Tests the endpoint status.



    chmod +x pipeline.sh
./pipeline.sh

Expected Output:

    "PIPELINE FINISHED SUCCESSFULLY"


#MLOps Features
##1. Experiment Tracking

We use Weights & Biases to log metrics (rule_count, lift) for every run, allowing us to compare how hyperparameters like min_support affect model performance.
##2. Model Registry

Every successful training run saves the rules_model.pkl to W&B Artifacts. This ensures Data Lineage—we can trace exactly which code and data produced the deployed model.
##3. Deployment

The model is served via a REST API using FastAPI.

    Endpoint: POST /recommend

    Function: Accepts a symptom and returns high-confidence associated symptoms.

    

    



    
