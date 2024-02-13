import psutil

# Iterate over all running processes
for proc in psutil.process_iter():
    try:
        # Get process information
        process_info = proc.as_dict(attrs=['pid', 'name', 'cmdline'])

        # Check if process has command line arguments
        if process_info['cmdline']:
            if process_info['name']=="python.exe":  # print only python's proccess list
                print(process_info['cmdline'])
                # print(
                # f"PID: {process_info['pid']}, Name: {process_info['name']}, Command Line: {' '.join(process_info['cmdline'])}")
    except psutil.NoSuchProcess:
        pass
    except psutil.AccessDenied:
        pass