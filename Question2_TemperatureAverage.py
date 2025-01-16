import os
import csv
import time 

temperatures_folder = "Temperature_data"

seasons_data = {
    "Summer": [12, 1, 2],  # December, January, February
    "Autumn": [3, 4, 5],   # March, April, May
    "Winter": [6, 7, 8],   # June, July, August
    "Spring": [9, 10, 11]  # September, October, November
}

seasonal_data = {season: [] for season in seasons_data}

def calculate_seasonal_averages():
    global seasonal_data

    if not os.path.exists(temperatures_folder):
        print(f"Error: The folder '{temperatures_folder}' does not exist.")
        return

    for file in os.listdir(temperatures_folder):
        if file.endswith(".csv"):
            filepath = os.path.join(temperatures_folder, file)

            try:
                with open(filepath, "r") as csvfile:
                    reader = csv.DictReader(csvfile)

                    required_columns = [
                        "January", "February", "March", "April", "May", "June",
                        "July", "August", "September", "October", "November", "December"
                    ]
                    if not all(month in reader.fieldnames for month in required_columns):
                        print(f"Warning: File '{file}' is missing required columns. Skipping...")
                        continue

                    for row in reader:
                        for month_idx, month in enumerate(required_columns, start=1):
                            try:
                                temperature = float(row[month])

                                if month_idx in seasons_data["Summer"]:
                                    seasonal_data["Summer"].append(temperature)
                                elif month_idx in seasons_data["Autumn"]:
                                    seasonal_data["Autumn"].append(temperature)
                                elif month_idx in seasons_data["Winter"]:
                                    seasonal_data["Winter"].append(temperature)
                                elif month_idx in seasons_data["Spring"]:
                                    seasonal_data["Spring"].append(temperature)

                            except ValueError:
                                print(f"Warning: Skipping invalid temperature in file '{file}', row: {row}")

            except Exception as e:
                print(f"Error: Failed to process file '{file}'. Details: {e}")

    overall_seasonal_averages = {
        season: sum(temps) / len(temps) if temps else 0 for season, temps in seasonal_data.items()
    }

    print("Saving seasonal averages... Please wait.")
    time.sleep(2) 

    output_path = "Temperature_output_files/average_temp.txt"
    try:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, "w") as file:
            file.write("Season, Average Temperature\n")
            for season, avg_temp in sorted(overall_seasonal_averages.items()):
                file.write(f"{season}, {avg_temp:.2f}\n")
        print(f"Seasonal averages saved successfully to '{output_path}'.")
    except Exception as e:
        print(f"Error: Failed to save averages to file. Details: {e}")

def find_largest_temp_range():
    largest_range = 0
    stations_with_largest_range = []

    for file in os.listdir(temperatures_folder):
        if file.endswith(".csv"):
            filepath = os.path.join(temperatures_folder, file)

            try:
                with open(filepath, "r") as csvfile:
                    reader = csv.DictReader(csvfile)

                    if "STATION_NAME" not in reader.fieldnames:
                        print(f"Warning: File '{file}' is missing 'STATION_NAME'. Skipping...")
                        continue

                    for row in reader:
                        try:
                            temperatures = [float(row[month]) for month in reader.fieldnames[4:] if row[month]]
                            temp_range = max(temperatures) - min(temperatures)

                            if temp_range > largest_range:
                                largest_range = temp_range
                                stations_with_largest_range = [row["STATION_NAME"]]
                            elif temp_range == largest_range:
                                stations_with_largest_range.append(row["STATION_NAME"])

                        except ValueError:
                            print(f"Warning: Skipping invalid row in file '{file}': {row}")

            except Exception as e:
                print(f"Error: Failed to process file '{file}'. Details: {e}")

    print("Saving largest temperature range... Please wait.")
    time.sleep(2)  

    output_path = "Temperature_output_files/largest_temp_range_station.txt"
    try:
        with open(output_path, "w") as file:
            file.write("Station(s) with Largest Temperature Range:\n")
            file.write("\n".join(stations_with_largest_range))
        print(f"Largest temperature range stations saved to '{output_path}'.")
    except Exception as e:
        print(f"Error: Failed to save largest temperature range stations. Details: {e}")

def find_warmest_and_coolest_stations():
    station_averages = {}

    for file in os.listdir(temperatures_folder):
        if file.endswith(".csv"):
            filepath = os.path.join(temperatures_folder, file)

            try:
                with open(filepath, "r") as csvfile:
                    reader = csv.DictReader(csvfile)

                    if "STATION_NAME" not in reader.fieldnames:
                        print(f"Warning: File '{file}' is missing 'STATION_NAME'. Skipping...")
                        continue

                    for row in reader:
                        try:
                            temperatures = [float(row[month]) for month in reader.fieldnames[4:] if row[month]]
                            average_temp = sum(temperatures) / len(temperatures)

                            station_name = row["STATION_NAME"]
                            if station_name not in station_averages:
                                station_averages[station_name] = []
                            station_averages[station_name].append(average_temp)

                        except ValueError:
                            print(f"Warning: Skipping invalid row in file '{file}': {row}")

            except Exception as e:
                print(f"Error: Failed to process file '{file}'. Details: {e}")

    overall_averages = {
        station: sum(temps) / len(temps) for station, temps in station_averages.items()
    }

    warmest_stations = [
        station for station, avg in overall_averages.items()
        if avg == max(overall_averages.values())
    ]
    coolest_stations = [
        station for station, avg in overall_averages.items()
        if avg == min(overall_averages.values())
    ]

    print("Saving warmest and coolest station... Please wait.")
    time.sleep(2) 
    
    output_path = "Temperature_output_files/warmest_and_coolest_station.txt"
    try:
        with open(output_path, "w") as file:
            file.write("Warmest Station(s):\n")
            file.write("\n".join(warmest_stations))
            file.write("\n\nCoolest Station(s):\n")
            file.write("\n".join(coolest_stations))
        print(f"Warmest and coolest stations saved to '{output_path}'.")
    except Exception as e:
        print(f"Error: Failed to save warmest and coolest stations. Details: {e}")

if __name__ == "__main__":
    calculate_seasonal_averages()
    find_largest_temp_range()
    find_warmest_and_coolest_stations()