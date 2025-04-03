from flask import Flask, request, jsonify
import os
from somr import get_tax_tip
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    

            
            # Here you would add OCR processing to extract text from the receipt
            # For now, we'll mock the text extraction
        extracted_text = "Sample receipt text: Office supplies $200, Client dinner $150"
            
            tax_tip = get_tax_tip(extracted_text)
            return jsonify({
                "message": "Receipt analyzed successfully",
                "tax_tip": tax_tip
            })
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    
    return jsonify({"error": "Error processing file"}), 500

@app.route('/chat', methods=['POST'])
def chat():
    try:
        message = request.form.get('message')
        file = request.files.get('invoice')
        
        if not message and not file:
            return jsonify({"error": "No message or file provided"}), 400
        
        # Process the message and file here
        # For now, return a mock response
        return jsonify({
            "reply": "Based on your query, you may be eligible for home office deductions."
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)