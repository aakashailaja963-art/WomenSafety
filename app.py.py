from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>SHEild - Women Safety Professional</title>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
<style>
body{background:#0f0f0f;color:white;font-family: 'Segoe UI'}
.sos-btn{width:200px;height:200px;border-radius:50%;background:radial-gradient(circle, #ff1a1a, #990000);border:8px solid #ff4d4d;box-shadow:0 0 40px red;font-size:32px;font-weight:bold;animation:pulse 1.5s infinite}
@keyframes pulse{0%{box-shadow:0 0 0 0 rgba(255,0,0,0.7)}70%{box-shadow:0 0 0 30px rgba(255,0,0,0)}}
.card{background:#1e1e1e;border:none;border-radius:15px}
</style>
</head>
<body>
<div class="container text-center py-4">
<h2>🛡️ SHEild - Professional</h2>
<p>Your Safety, Our Priority</p>

<div class="my-5">
<button class="sos-btn" onclick="sendSOS()">SOS</button>
<p class="mt-3">TAP FOR EMERGENCY</p>
</div>

<div class="row g-3">
<div class="col-6"><div class="card p-3" onclick="shareLocation()">📍<br>Share Live Location</div></div>
<div class="col-6"><div class="card p-3" onclick="startRecording()">🎙️<br>Start Recording</div></div>
<div class="col-6"><div class="card p-3" onclick="fakeCall()">📞<br>Fake Call</div></div>
<div class="col-6"><div class="card p-3" onclick="playSiren()">🚨<br>Siren Alarm</div></div>
</div>

<div class="card p-3 mt-4 text-start">
<h5>Emergency Contacts</h5>
<p>Police: 100 | Women Helpline: 1091 | Ambulance: 108</p>
<p id="location">Location: Fetching...</p>
<p id="status" class="text-success"></p>
</div>

<audio id="siren" src="https://www.soundjay.com/misc/sounds/bike-horn-01.mp3"></audio>
</div>

<script>
let lat, lon;
navigator.geolocation.watchPosition(pos => {
 lat = pos.coords.latitude; lon = pos.coords.longitude;
 document.getElementById('location').innerText = `Location: ${lat.toFixed(4)}, ${lon.toFixed(4)}`;
});

function sendSOS(){
 let msg = `🚨 EMERGENCY! I need help! My location: https://www.google.com/maps?q=${lat},${lon}`;
 document.getElementById('status').innerText = "SOS SENT! Location Shared!";
 window.open(`https://wa.me/?text=${encodeURIComponent(msg)}`, '_blank');
}

function shareLocation(){
 window.open(`https://www.google.com/maps?q=${lat},${lon}`, '_blank');
}

function fakeCall(){
 document.getElementById('status').innerText = "Incoming Call from Police (100)...";
 setTimeout(()=>{alert("Fake Call: Hello, Police is on the way! Stay strong.")},1000);
}

function playSiren(){
 document.getElementById('siren').play();
 document.getElementById('status').innerText = "🔊 LOUD SIREN ACTIVATED!";
}

function startRecording(){
 document.getElementById('status').innerText = "🎙️ Recording started for evidence (30 sec)...";
}
</script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)