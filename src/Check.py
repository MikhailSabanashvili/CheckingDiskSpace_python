import psutil

DISK_C = "C:"
DISK_E = "E:"

free_C = psutil.disk_usage(DISK_C).free / (1024 * 1024 * 1024)
print(f"{free_C:.4} Gb free on disk {DISK_C}")
free_E = psutil.disk_usage(DISK_E).free/(1024*1024*1024)
print(f"{free_E:.4} Gb free on disk {DISK_E}")
if free_E<5 and free_C<5: raise UserWarning("Место на дисках С и Е заканчивается")
if free_C<5: raise UserWarning("Место на диске С заканчивается")
if free_E<5: raise UserWarning("Место на диске E заканчивается")




