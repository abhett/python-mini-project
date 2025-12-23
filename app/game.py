from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def hello_world():
    jam_sekarang = datetime.now().strftime("%H:%M:%S")
    return f"""
    <h1 style="text-align:center; color:blue;">Halo dari Docker! 🐳</h1>
    <h2 style="text-align:center;">Jam Server saat ini: {jam_sekarang}</h2>
    <p style="text-align:center;">Aplikasi ini jalan di dalam Container.</p>
    """

if __name__ == '__main__':
    # host='0.0.0.0' penting agar aplikasi bisa diakses dari luar kontainer
    app.run(host='0.0.0.0', port=5000)