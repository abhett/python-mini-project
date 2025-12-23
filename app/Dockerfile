# Base image python
FROM python:3.9-slim

# Set folder kerja
WORKDIR /app

# Copy file requirements dulu (agar caching lebih efisien)
COPY requirements.txt .

# Install library yang ada di requirements.txt
RUN pip install -r requirements.txt

# Copy sisa kode (app.py)
COPY . .

# Beri tahu Docker bahwa aplikasi ini menggunakan Port 5000
EXPOSE 5000

# Jalankan aplikasi
CMD ["python", "app.py"]