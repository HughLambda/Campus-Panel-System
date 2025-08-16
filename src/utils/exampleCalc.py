import json
from typing import Dict, Any
from task import Task
from page import Page
from app import SimpApp


def getApp() -> SimpApp:
    task = CalculatorTask()
    page = Page(calculator_html, "Calculator Application")
    app = SimpApp("calculator", task, page)
    return app

# Example application 1: Calculator
class CalculatorTask(Task):
    def invoke(self, data):
        try:
            operation = data.get('operation')
            a = float(data.get('a', 0))
            b = float(data.get('b', 0))
            
            result = 0
            if operation == 'add':
                result = a + b
            elif operation == 'subtract':
                result = a - b
            elif operation == 'multiply':
                result = a * b
            elif operation == 'divide':
                if b == 0:
                    return {'error': 'cannot divide by zero'}
                result = a / b
            else:
                return {'error': 'Not supported operation'}
                
            return {'result': result, 'operation': operation, 'a': a, 'b': b}
        except Exception as e:
            return {'error': str(e)}

calculator_html = """
<!DOCTYPE html>
<html>
<head>
    <title>{{ title }}</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/socket.io/4.0.1/socket.io.js"></script>
    <style>
        body { font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto; padding: 20px; }
        .calculator { border: 1px solid #ccc; padding: 20px; border-radius: 5px; }
        .input-group { margin: 10px 0; }
        input, select { padding: 8px; margin: 0 5px; width: 100px; }
        button { padding: 8px 15px; background-color: #4CAF50; color: white; border: none; border-radius: 3px; cursor: pointer; }
        .result { margin: 15px 0; padding: 10px; border: 1px solid #eee; border-radius: 3px; }
    </style>
</head>
<body>
    <h1>{{ title }}</h1>
    <div class="calculator">
        <div class="input-group">
            <input type="number" id="num1" placeholder="number 1">
            <select id="operation">
                <option value="add">+</option>
                <option value="subtract">-</option>
                <option value="multiply">*</option>
                <option value="divide">/</option>
            </select>
            <input type="number" id="num2" placeholder="number 2">
            <button onclick="calculate()">Calculate</button>
        </div>
        <div class="result" id="result">results here</div>
    </div>

    <script>
        // Connect to WebSocket server
        const socket = io.connect('http://' + document.domain + ':' + location.port);
        const tag = '{{ tag }}';
        
        // Handle server response
        socket.on('response', function(data) {
            console.log('Received response:', data);
            const resultDiv = document.getElementById('result');
            
            if (data.status === 'success' && data.tag === tag) {
                if (data.result.error) {
                    resultDiv.textContent = 'Error: ' + data.result.error;
                    resultDiv.style.color = 'red';
                } else {
                    resultDiv.textContent = `${data.result.a} ${getOperator(data.result.operation)} ${data.result.b} = ${data.result.result}`;
                    resultDiv.style.color = 'green';
                }
            } else if (data.status === 'error') {
                resultDiv.textContent = 'Error: ' + data.message;
                resultDiv.style.color = 'red';
            }
        });
        
        // Calculation function
        function calculate() {
            const num1 = document.getElementById('num1').value;
            const num2 = document.getElementById('num2').value;
            const operation = document.getElementById('operation').value;
            
            if (!num1 || !num2) {
                alert('Please enter two numbers');
                return;
            }
            
            // Send data to server
            socket.emit('message', {
                tag: tag,
                operation: operation,
                a: parseFloat(num1),
                b: parseFloat(num2)
            });
        }
        
        // Helper function: Get operator symbol
        function getOperator(operation) {
            switch(operation) {
                case 'add': return '+';
                case 'subtract': return '-';
                case 'multiply': return '*';
                case 'divide': return '/';
                default: return '?';
            }
        }
    </script>
</body>
</html>
"""