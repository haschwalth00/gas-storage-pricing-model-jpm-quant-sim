
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from scipy.interpolate import interp1d

# Load natural gas price data
nat_gas_data = pd.read_csv('Nat_Gas (1).csv')
nat_gas_data['Dates'] = pd.to_datetime(nat_gas_data['Dates'])
nat_gas_data.set_index('Dates', inplace=True)

# Create price interpolation function
days_from_start = (nat_gas_data.index - nat_gas_data.index[0]).days
price_interp = interp1d(days_from_start, nat_gas_data['Prices'], kind='linear', fill_value="extrapolate")

def get_price(target_date):
    days = (target_date - nat_gas_data.index[0]).days
    return float(price_interp(days))

# Storage contract pricing function
def price_storage_contract(
    injection_dates, 
    withdrawal_dates, 
    injection_rate, 
    withdrawal_rate, 
    max_storage_volume, 
    storage_cost_per_unit_per_day
):
    storage_volume = 0.0
    cash_flows = []
    all_dates = sorted(set(injection_dates + withdrawal_dates))
    current_date = min(all_dates)
    end_date = max(all_dates)
    
    while current_date <= end_date:
        if current_date in injection_dates:
            amount = min(injection_rate, max_storage_volume - storage_volume)
            purchase_price = get_price(current_date)
            cash_flows.append(-purchase_price * amount)
            storage_volume += amount
        
        if current_date in withdrawal_dates:
            amount = min(withdrawal_rate, storage_volume)
            sale_price = get_price(current_date)
            cash_flows.append(+sale_price * amount)
            storage_volume -= amount
        
        storage_cost = storage_volume * storage_cost_per_unit_per_day
        cash_flows.append(-storage_cost)
        
        current_date += timedelta(days=1)
    
    total_contract_value = sum(cash_flows)
    return round(total_contract_value, 2)

# Example usage
if __name__ == "__main__":
    injection_dates = [datetime(2023, 6, 1), datetime(2023, 6, 15), datetime(2023, 7, 1)]
    withdrawal_dates = [datetime(2024, 1, 15), datetime(2024, 2, 1), datetime(2024, 3, 1)]
    injection_rate = 1000  # units/day
    withdrawal_rate = 800  # units/day
    max_storage_volume = 10000  # units
    storage_cost_per_unit_per_day = 0.01  # $

    contract_value = price_storage_contract(
        injection_dates,
        withdrawal_dates,
        injection_rate,
        withdrawal_rate,
        max_storage_volume,
        storage_cost_per_unit_per_day
    )
    print(f"Estimated storage contract value: ${contract_value}")
