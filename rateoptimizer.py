import time

# Configuration
MAX_REQUESTS = 10
WINDOW = 60  # seconds

# Store request timestamps
request_times = []

def is_allowed():
    current_time = time.time()

    # Remove old requests outside the window
    while request_times and current_time - request_times[0] > WINDOW:
        request_times.pop(0)

    # Check limit
    if len(request_times) < MAX_REQUESTS:
        request_times.append(current_time)
        return True
    return False


# Testing the rate limiter
for i in range(15):
    if is_allowed():
        print(f"Request {i+1}: Allowed")
    else:
        print(f"Request {i+1}: Rate limit exceeded")
    time.sleep(2)
    exit;
