import pandas as pd
import os
class Flight:
    def __init__(self, flight_num, delay_time):
        self.flight_num = flight_num
        self.delay_time = float(delay_time)

    def check_severity(self):
        if 30 <= self.delay_time <= 60:
            print(f"Standard Warning: Flight {self.flight_num} is delayed by {self.delay_time} minutes.")
        elif self.delay_time > 60:
            print(f"Severe Warning: Flight {self.flight_num} is delayed by {self.delay_time} minutes.")

df = pd.read_csv('arrivals.csv')
df['Minutes_Delayed'] = df['Minutes_Delayed'].fillna(0)
delayed_flights = df[df['Minutes_Delayed'] > 30]

if not delayed_flights.empty:
    most_delayed_row = delayed_flights.loc[delayed_flights['Minutes_Delayed'].idxmax()]
    flight_obj = Flight(most_delayed_row['Flight_Number'], most_delayed_row['Minutes_Delayed'])
    flight_obj.check_severity()
    new_log_data = {
        'Flight_Number': [flight_obj.flight_num],
        'Minutes_Delayed': [flight_obj.delay_time]
    }
    df_new_log = pd.DataFrame(new_log_data)

    log_file = 'severe_delays_log.csv'
    if os.path.exists(log_file):
        df_master = pd.read_csv(log_file)
        df_master = pd.concat([df_master, df_new_log], ignore_index=True)
    else:
        df_master = df_new_log
df_master.to_csv(log_file, index=False)
print("\nProcessed Data:")
print(df)
if os.path.exists('severe_delays_log.csv'):
    print("\nMaster Log:")