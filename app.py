from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return """
<html><head><meta name="viewport" content="width=device-width, initial-scale=1">
<style>
body{background:#0f0f0f;color:white;font-family:Arial;text-align:center;padding:20px;}
.sos{width:200px;height:200px;background:radial-gradient(#ff4444,#cc0000);border:5px solid white;border-radius:50%;font-size:40px;font-weight:bold;color:white;margin:30px auto;cursor:pointer;box-shadow:0 0 40px red;}
.card{background:white;color:black;padding:20px;margin:10px;border-radius:15px;width:38%;display:inline-block;font-weight:bold;font-size:18px;cursor:pointer;}
.contacts{background:white;color:black;padding:20px;border-radius:15px;margin-top:20px;}
</style></head>
<body>
<h1 style="color:#ff4444;">SHEild - Women Safety</h1>
<button class="sos" onclick="alert('SOS ALERT SENT! Police 100 Notified!')">SOS</button>
<p><b>TAP FOR EMERGENCY</b></p>
<div class="card" onclick="alert('Live Location Shared!')">Share Live Location</div>
<div class="card" onclick="alert('Recording Started!')">Start Recording</div>
<div class="card" onclick="alert('Fake Call Incoming...')">Fake Call</div>
<div class="card" onclick="alert('Siren ON!')">Siren Alarm</div>
<div class="contacts"><h3>Emergency Contacts</h3><p>Police: 100 | Women: 1091 | Ambulance: 108</p></div>
</body></html>
"""
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)