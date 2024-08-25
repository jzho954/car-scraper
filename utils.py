import pandas as pd
import csv

#write all cars from dict to csv file
def write_to_csv(car_list, filename="cars.csv"):
    final_df = pd.DataFrame()
    with open(filename, "w", newline="", encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["ID", "Name", "Location", "KMs", "Engine Size", "Transmission", "Price", "Link"])
        for car in car_list:
            df = pd.DataFrame([car.to_dict()])
            final_df = pd.concat([final_df, df], ignore_index=True)
    final_df.to_csv(filename, index=False)
    print(f"Data written to {filename} successfully.")
