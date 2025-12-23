from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    hasil = ""
    # Default nilai agar form tidak error saat pertama buka
    angka1 = ""
    angka2 = ""
    
    if request.method == 'POST':
        try:
            angka1 = float(request.form.get('angka1'))
            angka2 = float(request.form.get('angka2'))
            operasi = request.form.get('operasi')
            
            if operasi == 'tambah':
                total = angka1 + angka2
                simbol = "+"
            elif operasi == 'kurang':
                total = angka1 - angka2
                simbol = "-"
            elif operasi == 'kali':
                total = angka1 * angka2
                simbol = "x"
            elif operasi == 'bagi':
                if angka2 == 0:
                    hasil = "<h3 style='color:red;'>Error: Tidak bisa membagi dengan nol!</h3>"
                    total = None
                else:
                    total = angka1 / angka2
                    simbol = ":"
            
            if hasil == "": # Jika tidak ada error pembagian
                # Format agar angka bulat tidak ada koma nol (misal 5.0 jadi 5)
                total = int(total) if total.is_integer() else total
                angka1 = int(angka1) if angka1.is_integer() else angka1
                angka2 = int(angka2) if angka2.is_integer() else angka2
                
                hasil = f"<h3 style='color:green;'>Hasil: {angka1} {simbol} {angka2} = {total}</h3>"
                
        except ValueError:
            hasil = "<h3 style='color:red;'>Masukkan angka yang benar!</h3>"

    return f"""
    <div style="font-family: sans-serif; text-align:center; padding-top:50px; background-color: #f0f2f5; height: 100vh;">
        <div style="background-color: white; padding: 30px; border-radius: 10px; display: inline-block; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
            <h1 style="color: #333;">🧮 Super Kalkulator</h1>
            <form method="post">
                <input type="number" step="any" name="angka1" placeholder="Angka 1" value="{angka1}" required style="padding: 10px;">
                <select name="operasi" style="padding: 10px;">
                    <option value="tambah">+</option>
                    <option value="kurang">-</option>
                    <option value="kali">x</option>
                    <option value="bagi">:</option>
                </select>
                <input type="number" step="any" name="angka2" placeholder="Angka 2" value="{angka2}" required style="padding: 10px;">
                <br><br>
                <button type="submit" style="padding: 10px 20px; background-color: #007bff; color: white; border: none; border-radius: 5px; cursor: pointer;">Hitung Sekarang</button>
            </form>
            <br>
            {hasil}
        </div>
        <p style="margin-top: 20px; color: #666;">Versi 2.0 - Support Docker</p>
    </div>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)