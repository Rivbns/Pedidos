from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/', methods=['POST'])

def Chil_PiMen():
    button = request.form.get('button')
    contact = request.form.get('contact')
    button1 = request.form.get('button1')
    button2 = request.form.get('button2')
    button3 = request.form.get('button3')
    button4 = request.form.get('button4')
    button5 = request.form.get('button5')
    button6 = request.form.get('button6')
    button7 = request.form.get('button7')
    button8 = request.form.get('button8')


    if button:
        return redirect('index.html')
    elif contact:
        return redirect('https://ig.me/m/rivbns')
    elif button1:
        return render_template('Chil_Pi-Men.html', button1=button1)
    elif button2:
        return render_template('Chil_Mara.html', button2=button2)
    elif button6:
        return render_template('Hit_Piña-colada.html', button3=button3)
    elif button7:
        return render_template('Hit_Cuba-libre.html', button4=button4)
    elif button8:
        return render_template('Wild.html', button5=button5)
    elif button3:
        return render_template("Sour_Mara.html", button6=button6)
    elif button4:
        return render_template("Pisco_Acho.html", button7=button7)
    elif button5:
        return render_template("Especial.html", button8=button8)
    else:
        return redirect('index.html')

@app.route('/Chil_Pi-Men', methods=['POST'])
def process_form_CPM():
    button1 = request.form.get('button1')
    button2 = request.form.get('button2')
    
    if button1:
        return redirect('https://ig.me/m/rivbns')
    elif button2:
        return render_template('index.html', button2=button2)
    else:
        return redirect('/')

@app.route('/Chil_Mara', methods=['POST'])
def process_form_CMa():
    button1 = request.form.get('button1')
    button2 = request.form.get('button2')
    
    if button1:
        return redirect('https://ig.me/m/rivbns')
    elif button2:
        return render_template('index.html', button2=button2)
    else:
        return redirect('/')
    
@app.route('/Hit_Cuba-libre', methods=['POST'])
def process_form_HCu():
    button1 = request.form.get('button1')
    button2 = request.form.get('button2')
    
    if button1:
        return redirect('https://ig.me/m/rivbns')
    elif button2:
        return render_template('index.html', button2=button2)
    else:
        return redirect('/')
    
@app.route('/Hit_Piña-colada', methods=['POST'])
def process_form_HPCo():
    button1 = request.form.get('button1')
    button2 = request.form.get('button2')
    
    if button1:
        return redirect('https://ig.me/m/rivbns')
    elif button2:
        return render_template('index.html', button2=button2)
    else:
        return redirect('/')

@app.route('/Sour_Mara', methods=['POST'])
def process_form_WVNDG():
    button1 = request.form.get('button1')
    button2 = request.form.get('button2')
    
    if button1:
        return redirect('https://ig.me/m/rivbns')
    elif button2:
        return render_template('index.html', button2=button2)
    else:
        return redirect('/')

@app.route('/Pisco_Acho', methods=['POST'])
def process_form_WrG():
    button1 = request.form.get('button1')
    button2 = request.form.get('button2')
    
    if button1:
        return redirect('https://ig.me/m/rivbns')
    elif button2:
        return render_template('index.html', button2=button2)
    else:
        return redirect('/')

@app.route('/Wild', methods=['POST'])
def process_form_WVjG():
    button1 = request.form.get('button1')
    button2 = request.form.get('button2')
    
    if button1:
        return redirect('https://ig.me/m/rivbns')
    elif button2:
        return render_template('index.html', button2=button2)
    else:
        return redirect('/')
    
@app.route('/Especial', methods=['POST'])
def process_form_Es():
    button1 = request.form.get('button1')
    button2 = request.form.get('button2')
    
    if button1:
        return redirect('https://ig.me/m/rivbns')
    elif button2:
        return render_template('index.html', button2=button2)
    else:
        return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
    
