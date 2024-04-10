from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def test ():
    success = 'Adarsh Palm Retreat Bellandur Bangalore'
    return render_template ('maps.html', success=success)

if __name__ == '__main__' :
    app.run(debug=True)