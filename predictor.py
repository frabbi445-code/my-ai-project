import numpy as np
import pandas as pd

def generate_mock_data():
    np.random.seed(42)
    n_samples = 1000
    cpu_usage = np.random.uniform(10, 100, n_samples)
    ram_usage = np.random.uniform(20, 95, n_samples)
    temperature = np.random.uniform(40, 90, n_samples)
    
    health_score = 100 - (0.3 * cpu_usage + 0.2 * ram_usage + 0.4 * temperature)
    health_score = np.clip(health_score + np.random.normal(0, 5, n_samples), 0, 100)
    
    df = pd.DataFrame({
        'cpu_usage': cpu_usage,
        'ram_usage': ram_usage,
        'temperature': temperature,
        'health_score': health_score
    })
    return df

def predict_health(cpu, ram, temp):
    base_score = 100 - (0.3 * cpu + 0.2 * ram + 0.4 * temp)
    predicted_score = np.clip(base_score, 0, 100)
    return round(predicted_score, 2)