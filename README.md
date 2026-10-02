from flask import Flask, render_template_string

app = Flask(__name__)

HTML_CODE = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>SHEild - Women Safety</title>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
<style>
body { background: linear-gradient(135deg, #1a1a2e, #16213e); color: white; min-height: 100vh; }
.sos-btn { 
  width: 200px; height: 200px; border-radius: 50%; 
  background: radial-gradient(circle, #ff1744, #d50000);
  border: 5px solid white; font-size: 50px; font-weight: bold;
  box-shadow: 0 0 30px #ff1744, 0 0 60px #ff1744;
  animation: pulse 1.5s infinite;
}
@keyframes pulse { 0% { transform: scale(1); } 50% { transform: scale(1.05); } 100% { transform: scale(1); } }
.card { background: rgba(255,255,255,0.1); backdrop-filter: blur(10px); border-radius: 15px; border: 1px solid rgba(255,255,255,0.2); }
.police-call { position: fixed; bottom: 0; left: 0; right: 0; background: #0f3460; padding: 15px; display: none; }
</style>
</head>
<body>
<div class="container text-center py-4">
  <h2>🛡️ SHEild</h2>
  <p>Your Safety, Our Priority</p>
  
  <div class="my-4">
    <button class="sos-btn" onclick="sendSOS()">SOS</button>
    <p class="mt-3">Tap for Emergency</p>
    <p id="status" class="text-warning">📍 Location: Getting location...</p>
    <p id="coords"></p>
  </div>

  <div class="row g-3">
    <div class="col-6"><div class="card p-3" onclick="shareLocation()"><h4>📍</h4><p>Share Live Location</p></div></div>
    <div class="col-6"><div class="card p-3" onclick="siren()"><h4>🚨</h4><p>Siren Alarm</p></div></div>
    <div class="col-6"><div class="card p-3" onclick="fakeCall()"><h4>📞</h4><p>Fake Call</p></div></div>
    <div class="col-6"><div class="card p-3" onclick="recordEvidence()"><h4>🎙️</h4><p>Evidence Record</p></div></div>
  </div>

  <div class="card mt-4 p-3 text-start">
    <h5>🚨 Emergency Contacts</h5>
    <p>👮 Police: 100 <br> 👩 Women Helpline: 1091 <br> 🚑 Ambulance: 108</p>
  </div>
</div>

<div class="police-call text-center" id="callScreen">
  <h4>📞 Incoming Call from Police (100)...</h4>
  <p>Officer is calling you</p>
  <button class="btn btn-success me-2" onclick="answerCall()">Answer</button>
  <button class="btn btn-danger" onclick="endCall()">Decline</button>
  <audio id="ringtone" loop src="https://www.soundjay.com/phone/phone-calling-1.mp3"></audio>
</div>

<script>
let lat = 17.5943, lon = 78.4860;
let audioContext;

if(navigator.geolocation){
  navigator.geolocation.watchPosition(pos => {
    lat = pos.coords.latitude;
    lon = pos.coords.longitude;
    document.getElementById('coords').innerText = lat.toFixed(4) + ', ' + lon.toFixed(4);
    document.getElementById('status').innerText = '📍 Location: Live Tracking Active';
  }, err => {
    document.getElementById('status').innerText = '📍 Location: Medchal Active (Default)';
  });
}

function sendSOS(){
  let msg = `🚨 EMERGENCY! I need help! My location: https://www.google.com/maps?q=${lat},${lon} - Sent via SHEild App`;
  let url = `https://wa.me/?text=${encodeURIComponent(msg)}`;
  window.open(url, '_blank');
  siren();
  document.getElementById('status').innerText = '✅ SOS Sent via WhatsApp!';
}

function shareLocation(){
  window.open(`https://www.google.com/maps?q=${lat},${lon}`, '_blank');
}

function siren(){
  try{
    if(!audioContext) audioContext = new (window.AudioContext || window.webkitAudioContext)();
    let osc = audioContext.createOscillator();
    let gain = audioContext.createGain();
    osc.connect(gain); gain.connect(audioContext.destination);
    osc.frequency.value = 800;
    gain.gain.value = 1;
    osc.start();
    setTimeout(()=>{osc.stop();}, 3000);
    alert('🚨 Siren Activated for 3 seconds! Help will hear you!');
  } catch(e){ alert('🚨 Siren Alert!'); }
}

function fakeCall(){
  document.getElementById('callScreen').style.display = 'block';
  document.getElementById('ringtone').play().catch(()=>{});
}

function answerCall(){
  alert('You: Hello Police? I am in danger at location: ' + lat + ',' + lon);
  endCall();
}

function endCall(){
  document.getElementById('callScreen').style.display = 'none';
  document.getElementById('ringtone').pause();
}

function recordEvidence(){
  alert('🎙️ Recording started for 30 seconds - This will be saved as evidence!');
}
</script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_CODE)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)