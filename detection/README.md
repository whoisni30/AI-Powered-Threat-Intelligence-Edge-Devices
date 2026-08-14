# Threat Detection Module

This module implements an anomaly detection pipeline for identifying suspicious activities on edge devices using machine learning.

## Detection Workflow

1. Load network traffic metadata.
2. Extract numerical security features.
3. Train an Isolation Forest anomaly detection model.
4. Predict anomalous events.
5. Classify events as **Normal** or **Suspicious**.
6. Generate threat alerts for security monitoring.

## Implemented Script

* `threat_detector.py`

The detection logic analyzes packet volume, failed login attempts, CPU usage, memory usage, connection frequency, destination ports, and session duration to identify abnormal behavior patterns that may indicate cyber attacks.
