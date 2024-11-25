import os

def process_file(input_path, output_path):
    # preheader lines
    preheader_lines = [
        "WigleWifi-1.4,appRelease=1.0.0,model=Flipper Zero,release=1.0.3,device=Flipper Zero,display=Monochrome LCD,board=Flipper Main,brand=Flipper Devices\n",
        "MAC,SSID,AuthMode,FirstSeen,Channel,RSSI,CurrentLatitude,CurrentLongitude,AltitudeMeters,AccuracyMeters,Type\n"
    ]

    processed_lines = []
    found_data = False

    # open/read input file
    with open(input_path, 'r') as file:
        for line in file:
            if not found_data:
                # check for the pipe symbol "|"
                if '| ' in line and line.split()[0].isdigit():
                    found_data = True
                    processed_lines.extend(preheader_lines)  # add preheader
                    processed_line = line.split('| ', 1)[1]  # remove number and pipe
                    processed_lines.append(processed_line)
            elif found_data:
                # process the rest
                if '| ' in line:
                    processed_line = line.split('| ', 1)[1]  # remove number and pipe
                    processed_lines.append(processed_line)
                else:
                    processed_lines.append(line)  # leave other lines unchanged

    # write to output file
    with open(output_path, 'w') as file:
        file.writelines(processed_lines)

    print(f"output saved to: {output_path}, now go upload to wigle!")


if __name__ == "__main__":
    input_file = "wardrive_4.log" 
    output_file = "processed_wardrive_4.log" 

    if os.path.exists(input_file):
        process_file(input_file, output_file)
    else:
        print(f"Input file '{input_file}' does not exist.")
