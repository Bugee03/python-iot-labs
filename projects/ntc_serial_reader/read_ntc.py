#!/usr/bin/env python3
import serial
import serial.tools.list_ports
import json
import time
import sys

def find_arduino_port():
    ports = serial.tools.list_ports.comports()
    for port in ports:
        if "usbmodem" in port.device or "Arduino" in port.description or "Mega" in port.description:
            return port.device
    # Fallback default on macOS
    return "/dev/cu.usbmodem1201"

def main():
    port = find_arduino_port()
    baudrate = 115200

    print(f"Connecting to Arduino on {port} at {baudrate} baud...")
    
    try:
        ser = serial.Serial(port, baudrate, timeout=2)
        # Give Arduino time to reset after opening serial port
        time.sleep(2)
        ser.reset_input_buffer()
        print("Connected! Reading analog input A0 (NTC sensor)...\n")
        print(f"{'ADC Value':<12} | {'Voltage (V)':<12} | {'Resistance (Ω)':<16} | {'Temp (°C)':<12} | {'Temp (°F)':<12}")
        print("-" * 72)

        read_count = 0
        max_reads = 20  # Read 20 samples in demonstration run

        # Allow passing --continuous flag or count argument
        if len(sys.argv) > 1 and sys.argv[1] == "--loop":
            max_reads = float('inf')

        while read_count < max_reads:
            line = ser.readline().decode('utf-8', errors='replace').strip()
            if not line:
                continue
            
            try:
                data = json.loads(line)
                adc = data.get("adc", 0)
                voltage = data.get("voltage", 0.0)
                resistance = data.get("resistance", 0.0)
                temp_c = data.get("temp_c", 0.0)
                temp_f = (temp_c * 9/5) + 32 if temp_c else 0.0

                print(f"{adc:<12} | {voltage:<12.3f} | {resistance:<16.1f} | {temp_c:<12.2f} | {temp_f:<12.2f}")
                read_count += 1
            except json.JSONDecodeError:
                # Raw output fallback
                print(f"Raw: {line}")
                read_count += 1

    except serial.SerialException as e:
        print(f"Error opening serial port {port}: {e}")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nStopped by user.")
    finally:
        if 'ser' in locals() and ser.is_open:
            ser.close()

if __name__ == "__main__":
    main()
