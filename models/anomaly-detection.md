# Anomaly Detection Model

## Objective

The anomaly detection module identifies suspicious activity in edge-device logs and network traffic metadata. The model is designed to detect abnormal behavior without requiring a large labeled attack dataset.

## Selected Model

**Isolation Forest**

Isolation Forest is an unsupervised machine learning algorithm that isolates anomalous observations by recursively partitioning data. It is well suited for cybersecurity applications because network attacks are often rare compared to normal activity.

## Input Features

The detection engine uses numerical features extracted from network and system logs.

| Feature              | Description                      |
| -------------------- | -------------------------------- |
| packet_count         | Number of packets observed       |
| failed_logins        | Failed authentication attempts   |
| cpu_usage            | CPU utilization percentage       |
| memory_usage         | Memory utilization percentage    |
| connection_frequency | Number of connections per minute |
| destination_port     | Target network port              |
| session_duration     | Duration of the network session  |

## Detection Pipeline

1. Collect network and system logs.
2. Clean and preprocess data.
3. Normalize numerical features.
4. Train Isolation Forest on historical behavior.
5. Predict anomaly scores.
6. Classify events as Normal or Suspicious.
7. Generate security alerts.

## Example Python Implementation

```python
from sklearn.ensemble import IsolationForest
import pandas as pd

df = pd.read_csv('sample-network-log.csv')

features = df[['packet_count',
               'failed_logins',
               'cpu_usage',
               'memory_usage',
               'connection_frequency',
               'destination_port',
               'session_duration']]

model = IsolationForest(
    contamination=0.05,
    random_state=42
)

df['prediction'] = model.fit_predict(features)

df['threat'] = df['prediction'].apply(
    lambda x: 'Suspicious' if x == -1 else 'Normal'
)

print(df[['threat']].head())
```

## Threat Classification

* Normal
* Suspicious
* High-Risk Anomaly

## Expected Output

The model labels unusual device behavior such as repeated failed login attempts, abnormal traffic spikes, or unexpected connection patterns as **Suspicious**, allowing the alerting system to notify administrators immediately.

## Security Benefit

Isolation Forest enables lightweight anomaly detection suitable for resource-constrained edge devices, making it appropriate for local intrusion detection and real-time cyber threat monitoring.
