# Flipper Zero/Marauder Wardrive Log File Cleaner

A Python script designed to clean and process Flipper Zero wardrive log files for seamless WiGLE uploads.

- Processes multiple .log files in a directory at once.
- Removes text above the first relevant line in the input file.
- Strips leading numbers and the pipe symbol (|) from each line.
- Adds the required preheader to the processed files.
- Outputs the cleaned and formatted files for WiGLE uploads.

## Prerequisites

- Python 3.6 or higher
- 1. **Clone the Repository**: (e.g. `logs/` contating files like `wardrive_0.log`)

## How to Use

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/your-username/flipper-wardrive-log-cleaner.git
    ```
    
2. **Prepare your log files**:
   Place all your .log files (e.g., `wardrive_0.log`, `wardrive_1.log`, etc.) into a directory named `logs` in the same location as the script.

3. **Run the script**:
   ```bash
   python3 flipper-wardrive-log-cleaner.py

4. ***Upload process files**
   The processed files will be saved in a new directory named `processed_logs`, with filenames prefixed by processed_ (e.g., `processed_wardrive_0.log`).

## File Structure Example

Original Log File:
```
Some header text...
More irrelevant data...
48 | 2C:EA:DC:7A:B9:FA,Verizon_P3R3CY,[WPA2_PSK],2024-11-24 14:54:3,6,-55,36.0555916,-79.9968796,227.10,7.25,WIFI
49 | CE:9E:43:B4:D2:7E,NIMAYL677703 ,[WPA2_PSK],2024-11-24 14:54:3,6,-60,36.0555916,-79.9968796,227.10,7.25,WIFI
```
Updated Log File:
```
WigleWifi-1.4,appRelease=1.0.0,model=Flipper Zero,release=1.0.3,device=Flipper Zero,display=Monochrome LCD,board=Flipper Main,brand=Flipper Devices
MAC,SSID,AuthMode,FirstSeen,Channel,RSSI,CurrentLatitude,CurrentLongitude,AltitudeMeters,AccuracyMeters,Type
2C:EA:DC:7A:B9:FA,Verizon_P3R3CY,[WPA2_PSK],2024-11-24 14:54:3,6,-55,36.0555916,-79.9968796,227.10,7.25,WIFI
CE:9E:43:B4:D2:7E,NIMAYL677703 ,[WPA2_PSK],2024-11-24 14:54:3,6,-60,36.0555916,-79.9968796,227.10,7.25,WIFI
```
