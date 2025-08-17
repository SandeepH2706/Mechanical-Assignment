#!/usr/bin/env python3
"""
Database initialization script for production deployment.
Run this after deploying to create the database tables.
"""

from app import app
from models import db

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        print("Database tables created successfully!")
