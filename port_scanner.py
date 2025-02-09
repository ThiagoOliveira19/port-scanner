import socket
import pandas as pd
from tkinter import *
from tkinter import messagebox, filedialog, ttk  # ttk foi importado aqui
import threading

def scan_ports(target, start_port, end_port):
    open_ports = []
    progress_bar["value"] = 0
    progress_bar["maximum"] = end_port - start_port + 1

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
                open_ports.append({"port": port, "service": service})
                update_result(f"Port {port} is open (Service: {service})\n")
            sock.close()
        except socket.error as e:
            update_result(f"Error scanning port {port}: {e}\n")
            break
        progress_bar["value"] += 1

    return open_ports

def update_result(text):
    result_text.insert(END, text)
    result_text.see(END)  # Rola para o final automaticamente
    root.update_idletasks()  # Atualiza a interface sem bloquear

def start_scan():
    target = entry_target.get()
    start_port = int(entry_start_port.get() or 1)
    end_port = int(entry_end_port.get() or 1024)

    if not target:
        messagebox.showerror("Error", "Please enter a target IP or hostname.")
        return

    result_text.delete(1.0, END)
    update_result(f"Scanning {target} from port {start_port} to {end_port}...\n")

    def scan_thread():
        open_ports = scan_ports(target, start_port, end_port)
        if open_ports:
            update_result("Scan complete! Ports found:\n")
            for port in open_ports:
                update_result(f"Port {port['port']} - Service: {port['service']}\n")
            save_results(open_ports, target)
        else:
            update_result("No open ports found.\n")

    threading.Thread(target=scan_thread, daemon=True).start()

def save_results(open_ports, target):
    save_path = filedialog.asksaveasfilename(defaultextension=".csv",
                                             filetypes=[("CSV files", "*.csv")],
                                             initialfile=f"{target}_open_ports.csv")
    if save_path:
        df = pd.DataFrame(open_ports)
        df.to_csv(save_path, index=False)
        messagebox.showinfo("Saved", f"Results saved to {save_path}")

# Create the GUI
root = Tk()
root.title("Python Port Scanner")
root.geometry("700x500")

Label(root, text="Target IP/Hostname:").grid(row=0, column=0, padx=10, pady=5, sticky=W)
entry_target = Entry(root, width=30)
entry_target.grid(row=0, column=1, padx=10, pady=5)

Label(root, text="Start Port:").grid(row=1, column=0, padx=10, pady=5, sticky=W)
entry_start_port = Entry(root, width=10)
entry_start_port.grid(row=1, column=1, padx=10, pady=5, sticky=W)

Label(root, text="End Port:").grid(row=2, column=0, padx=10, pady=5, sticky=W)
entry_end_port = Entry(root, width=10)
entry_end_port.grid(row=2, column=1, padx=10, pady=5, sticky=W)

Button(root, text="Start Scan", command=start_scan).grid(row=3, column=0, columnspan=2, pady=10)

progress_bar = ttk.Progressbar(root, length=600, mode="determinate")
progress_bar.grid(row=4, column=0, columnspan=2, pady=5)

result_text = Text(root, height=15, width=85)
result_text.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

root.mainloop()
