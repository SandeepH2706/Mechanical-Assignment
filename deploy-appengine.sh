#!/bin/bash

# Google App Engine Deployment Script
# Make sure you have gcloud CLI installed and authenticated

echo "🚀 Deploying to Google App Engine..."

# Deploy to App Engine
echo "🌐 Deploying application..."
gcloud app deploy app.yaml --quiet

echo "✅ Deployment complete!"
echo "🔗 Your app is available at:"
gcloud app browse --no-launch-browser
