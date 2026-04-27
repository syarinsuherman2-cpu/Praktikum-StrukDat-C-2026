# Data set
tim_frontend = {"HTML", "CSS", "JavaScript", "React"}
tim_backend = {"Python", "JavaScript", "SQL", "NodeJS"}

# 1. Irisan (skill yang dimiliki kedua tim)
irisan = tim_frontend.intersection(tim_backend)

# 2. Skill yang hanya dimiliki tim_backend
backend_only = tim_backend.difference(tim_frontend)

# 3. Gabungan semua skill unik
gabungan = tim_frontend.union(tim_backend)

# Output
print("Skill yang dimiliki kedua tim:", irisan)
print("Skill hanya di tim backend:", backend_only)
print("Total skill unik:", gabungan)