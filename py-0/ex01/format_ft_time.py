from time import time
from datetime import datetime

now = time()
time = f"{now:,.4f} or {now:.2e} in scientific notation"
print(f"Seconds since January 1, 1970: {time}")
print(datetime.now().strftime("%b %d %Y"))
