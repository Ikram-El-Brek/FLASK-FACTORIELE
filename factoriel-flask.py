from flask import Flask, request, render_template_string

app = Flask(__name__)

html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Factorial Calculator</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
        }
        
        .container {
            width: 300px;
            margin: 50px auto;
            background-color: #fff;
            padding: 20px;
            border: 1px solid #ddd;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        
        .input-field {
            width: 95%;
            height: 40px;
            margin-bottom: 20px;
            padding: 10px;
            font-size: 16px;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
        
        .button {
            width: 100%;
            height: 40px;
            background-color: #4CAF50;
            color: #fff;
            padding: 10px;
            font-size: 16px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        
        .button:hover {
            background-color: #3e8e41;
        }
        
        .result {
            font-size: 24px;
            font-weight: bold;
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h2>Factorial Calculator</h2>
        <form action="/factorial" method="get">
            <input type="number" name="num" class="input-field" placeholder="Enter a number">
            <button class="button" type="submit">Calculate</button>
        </form>
        <p id="result" class="result">{% if result %}{{ result }}{% endif %}</p>
    </div>
</body>
</html>
"""

@app.route('/', methods=['GET'])
def index(): 
    return render_template_string(html_template)

@app.route('/factorial', methods=['GET'])
def factorial():
    print("Je suis dans la fonction factorial !")
    try:
        num = int(request.args.get('num'))
        print("Le nombre est :", num)
        if num < 0:
            raise ValueError("Le nombre doit être non négatif")
        elif num == 0:
            print("Le résultat est 1")
            return render_template_string(html_template, result=1)
        else:
            result = 1
            for i in range(1, num + 1):
                result *= i
            print("Le résultat est :", result)
            return render_template_string(html_template, result=result)
    except ValueError as e:
        print("Erreur :", str(e))
        return render_template_string(html_template, result=str(e))
    except Exception as e:
        print("Erreur inconnue :", str(e))
        return render_template_string(html_template, result="Erreur inconnue")

if __name__ == '__main__':
    print("L'application est en cours d'exécution !")
    app.run(debug=True)