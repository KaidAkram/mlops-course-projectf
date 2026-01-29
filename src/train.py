import pandas as pd
import wandb
from mlxtend.frequent_patterns import apriori, association_rules
import joblib
# --- PASTE THIS LINE HERE WITH QUOTES ---
wandb.login(key="the api key") 
# ----------------------------------------
# --- W&B INIT ---
wandb.init(project="mlops-fast-track", name="experiment-1")

# --- 1. DATA PREP (Simulated) ---
data = {
    'Fever': [1, 1, 0, 1, 1],
    'Cough': [1, 1, 1, 0, 1],
    'Headache': [0, 1, 0, 1, 0],
    'Fatigue': [0, 1, 1, 1, 1]
}
df = pd.DataFrame(data)

# --- 2. TRAINING (Mining) ---
# Log hyperparameters
wandb.config.min_support = 0.5
frequent_itemsets = apriori(df, min_support=wandb.config.min_support, use_colnames=True)
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.6)

# --- 3. LOGGING METRICS ---
wandb.log({"rule_count": len(rules)})
wandb.log({"avg_lift": rules['lift'].mean()})

# --- 4. MODEL REGISTRY ---
# Save rules to a file and upload to W&B
joblib.dump(rules, "rules_model.pkl")
artifact = wandb.Artifact('apriori-model', type='model')
artifact.add_file("rules_model.pkl")
wandb.log_artifact(artifact)

print("Run Complete.")
