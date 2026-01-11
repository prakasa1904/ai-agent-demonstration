import psutil

# =====================================
# Local Function (Tool)
# =====================================

def get_cpu_usage() -> float:
    print(">>> get_cpu_usage() CALLED")
    return psutil.cpu_percent(interval=1)

# =====================================
# Local Function (Tool)
# =====================================
def get_memory_usage() -> float:
    print(">>> get_memory_usage() CALLED")
    return psutil.virtual_memory().percent

# =====================================
# Local Function (Tool)
# =====================================
def find_user_by_email(email: str) -> dict:
    print(">>> find_user_by_email() CALLED")
    return {
        "id": 100,
        "name": "Nedya Amrih Prakasa",
        "email": email
    }