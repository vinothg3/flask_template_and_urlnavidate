from flask import Flask,render_template

fai=Flask(__name__)
@fai.route('/first')
def first():
    return render_template('first.html')
@fai.route('/context')
def context():
    return render_template('context.html',name='vinoth',age='23')

if __name__=='__main__':
    fai.run(debug=True)