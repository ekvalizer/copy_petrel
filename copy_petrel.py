import os

petrel = os.environ.get("PETREL2019")
#or
petrel_exists = "PETREL2019" in os.environ

# petrel_path = 
os.environ.putenv("PETREL", )
print(f"{petrel_exists}")
print(f"{petrel}")
