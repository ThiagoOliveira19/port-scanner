import socket
import pandas as pd

def scan_ports(target, start_port, end_port):
    open_ports = []
    print(f"Scanning {target} from port {start_port} to {end_port}...")

    for port in range(start_port, end_port + 1):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            result = sock.connect_ex((target, port))
            if result == 0:
                print(f"Port {port} is open.")
                open_ports.append(port)
            sock.close()
        except KeyboardInterrupt:
            print("Scan interrupted by user.")
            break
        except socket.error as e:
            print(f"Socket error: {e}")
            break

    return open_ports

def save_results_to_csv(open_ports, target):
    df = pd.DataFrame(open_ports, columns=["Open Ports"])
    df.to_csv(f"{target}_open_ports.csv", index=False)
    print(f"Results saved to {target}_open_ports.csv")

if __name__ == "__main__":
    target = input("Enter target IP or hostname: ")
    start_port = int(input("Enter start port: "))
    end_port = int(input("Enter end port: "))

    open_ports = scan_ports(target, start_port, end_port)
    if open_ports:
        print(f"Open ports: {open_ports}")
        save_results_to_csv(open_ports, target)
    else:
        print("No open ports found.")

def scan_ports(target, start_port, end_port):
    open_ports = []
    print(f"Scanning {target} from port {start_port} to {end_port}...")

    for port in range(start_port, end_port + 1):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            result = sock.connect_ex((target, port))
            if result == 0:
                try:
                    service = socket.getservbyport(port)
                except OSError:
                    service = "Unknown"
                print(f"Port {port} is open (Service: {service}).")
                open_ports.append({"port": port, "service": service})
            sock.close()
        except KeyboardInterrupt:
            print("Scan interrupted by user.")
            break
        except socket.error as e:
            print(f"Socket error: {e}")
            break

    return open_ports

def save_results_to_csv(open_ports, target):
    df = pd.DataFrame(open_ports)
    df.to_csv(f"{target}_open_ports.csv", index=False)
    print(f"Results saved to {target}_open_ports.csv")
