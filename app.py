from flask import Flask
import os
import time
import subprocess
import getpass

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h2>Welcome!</h2>
    <p>This is the home page. Visit <a href="/htop">/htop</a> to see system information.</p>
    '''

@app.route('/htop')
def htop():
    name = "Your Full Name Here"   # 🔁 Replace with your real name
    username = getpass.getuser()
    ist_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

    # Get system top output
    try:
        top_output = subprocess.check_output(['top', '-b', '-n', '1'], text=True)
    except Exception as e:
        top_output = f"Error fetching top output: {e}"

    return f"""
    <pre>
Name: {name}
Username: {username}
Server Time (IST): {ist_time}

TOP Output:
{top_output}
    </pre>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
