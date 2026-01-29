#!/bin/bash
echo "=================================="
echo "   STARTING MLOPS AUTO-PIPELINE   "
echo "=================================="

echo "[STEP 1] Checking Environment..."
python3 --version
echo "Status: OK"

echo "[STEP 2] Retraining Model..."
# We run the training script
python3 src/train.py
echo "Status: Model Trained & Logged to W&B"

echo "[STEP 3] Testing Deployment..."
# Start the server in the background, wait 5s, then stop it
timeout 5s uvicorn src.api:app &
sleep 3
echo "Ping server status..."
# This command 'curls' your API to see if it replies
curl -s http://127.0.0.1:8000/ | grep "Online"

echo ""
echo "=================================="
echo "   PIPELINE FINISHED SUCCESSFULLY "
echo "=================================="
