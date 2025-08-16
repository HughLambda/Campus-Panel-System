import json
from typing import Dict, Any
from task import Task
from page import Page
from app import SimpApp

def getApp() -> SimpApp:
    task = TextProcessorTask()
    page = Page(text_processor_html, "Text Processing Application")
    app = SimpApp("text-processor", task, page)
    return app
# Example application 2: Text processing application
class TextProcessorTask(Task):
    def invoke(self, data):
        text = data.get('text', '')
        operation = data.get('operation', 'uppercase')
        
        result = ""
        if operation == 'uppercase':
            result = text.upper()
        elif operation == 'lowercase':
            result = text.lower()
        elif operation == 'reverse':
            result = text[::-1]
        elif operation == 'length':
            result = len(text)
        else:
            return {'error': 'Unsupported operation'}
            
        return {
            'original': text,
            'operation': operation,
            'result': result
        }

text_processor_html = """
<!DOCTYPE html>
<html>
<head>
    <title>{{ title }}</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/socket.io/4.0.1/socket.io.js"></script>
    <style>
        body { font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }
        textarea { width: 100%; height: 100px; margin: 10px 0; padding: 10px; }
        .operations { margin: 10px 0; }
        button { margin: 0 5px; padding: 5px 10px; }
        .result { margin: 15px 0; padding: 10px; border: 1px solid #eee; border-radius: 3px; }
    </style>
</head>
<body>
    <h1>{{ title }}</h1>
    <div class="text-processor">
        <textarea id="text-input" placeholder="Please enter text to process..."></textarea>
        
        <div class="operations">
            <button onclick="processText('uppercase')">Convert to Uppercase</button>
            <button onclick="processText('lowercase')">Convert to Lowercase</button>
            <button onclick="processText('reverse')">Reverse Text</button>
            <button onclick="processText('length')">Calculate Length</button>
        </div>
        
        <div class="result" id="result">Processing result will be displayed here</div>
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
                    let operationText = '';
                    switch(data.result.operation) {
                        case 'uppercase': operationText = 'Convert to Uppercase'; break;
                        case 'lowercase': operationText = 'Convert to Lowercase'; break;
                        case 'reverse': operationText = 'Reverse Text'; break;
                        case 'length': operationText = 'Text Length'; break;
                        default: operationText = 'Processing';
                    }
                    
                    resultDiv.innerHTML = `
                        <strong>Original Text:</strong> ${data.result.original}<br>
                        <strong>${operationText} Result:</strong> ${data.result.result}
                    `;
                    resultDiv.style.color = 'green';
                }
            } else if (data.status === 'error') {
                resultDiv.textContent = 'Error: ' + data.message;
                resultDiv.style.color = 'red';
            }
        });
        
        // Text processing function
        function processText(operation) {
            const text = document.getElementById('text-input').value;
            
            if (!text.trim()) {
                alert('Please enter text to process');
                return;
            }
            
            // Send data to server
            socket.emit('message', {
                tag: tag,
                operation: operation,
                text: text
            });
        }
    </script>
</body>
</html>
"""