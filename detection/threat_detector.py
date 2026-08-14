import pandas as pd
from sklearn.ensemble import IsolationForest

# Load sample network log data
df = pd.read_csv('../data/sample-network-log.csv')

# Select numerical features for anomaly detection
features = df[['packet_count',
               'failed_logins',
               'cpu_usage',
               'memory_usage',
               'connection_frequency',
               'destination_port',
               'session_duration']]

# Train Isolation Forest model
model = IsolationForest(
    contamination=0.2,
    random_state=42
)

# Predict anomalies
predictions = model.fit_predict(features)

# Map predictions to threat labels
df['threat'] = ['Suspicious' if p == -1 else 'Normal' for p in predictions]

# Display suspicious events
suspicious = df[df['threat'] == 'Suspicious']

print('Threat Detection Results')
print(df[['timestamp',
          'source_ip',
          'destination_port',
          'packet_count',
          'failed_logins',
          'threat']])

print('\nSuspicious Events')
print(suspicious[['timestamp',
                  'source_ip',
                  'destination_port',
                  'packet_count',
                  'failed_logins']])
