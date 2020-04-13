import psutil

DISK_C = "C:"
DISK_E = "E:"

free = psutil.disk_usage(DISK_C).free / (1024 * 1024 * 1024)
print(f"{free:.4} Gb free on disk {DISK_C}")
if free<100: print("Место на диске С заканчивается")
free = psutil.disk_usage(DISK_E).free/(1024*1024*1024)
print(f"{free:.4} Gb free on disk {DISK_E}")
if free<100: print("Место на диске E заканчивается")


