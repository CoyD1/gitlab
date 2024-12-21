# Новый комментарий
from flask import Flask, request, jsonify, render_template
import serial 


app = Flask(__name__) 

# Настройка последовательного порта
serial_port = 'COM14'  
baud_rate = 9600  
ser = serial.Serial(serial_port, baud_rate)  # Открываем последовательный порт с указанными параметрами

# Определяем маршрут для главной страницы
@app.route('/') 
def index(): 
    return render_template('ardu.html')  # Возвращаем HTML для отображения

# Определяем маршрут для получения температуры
@app.route('/temperature', methods=['GET']) 
def get_temperature(): 

    try: 
        # Проверяем, есть ли входящие данные в последовательном порту
        if ser.in_waiting > 0: 
            line = ser.readline() 
            temperature = line.decode("utf-8").strip()  
            return jsonify({"temperature": temperature})  
        else: 
            return jsonify({"error": "No data available"}), 300  
    except Exception as e: 
        return jsonify({"error": str(e)}), 300  


if __name__ == '__main__': 
    app.run(debug=False, port=4000)  # Запускаем сервер Flask на порту 5000