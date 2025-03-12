time_in_seconds = int(input("Enter the duration in seconds: "))
hrs = time_in_seconds // 3600
mins = (time_in_seconds % 3600) // 60
secs = time_in_seconds % 60
print(f"Duration in HH:MM:SS format: {hrs:02}:{mins:02}:{secs:02}")