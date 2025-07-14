
async function recordAndSend() {
    const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
    const mediaRecorder = new MediaRecorder(stream);
    let chunks = [];

    mediaRecorder.ondataavailable = e => chunks.push(e.data);
    mediaRecorder.onstop = async () => {
        const blob = new Blob(chunks, { type: 'audio/wav' });
        const formData = new FormData();
        formData.append('audio', blob);

        const res = await fetch('http://127.0.0.1:5000/chat', {
            method: 'POST',
            body: formData
        });

        const data = await res.json();
        document.getElementById('response').innerText = data.response;

        const audioPlayer = document.getElementById('audioPlayer');
        const audioBlob = atob(data.audio);
        const buffer = new Uint8Array(audioBlob.length);
        for (let i = 0; i < audioBlob.length; i++) buffer[i] = audioBlob.charCodeAt(i);
        const audioURL = URL.createObjectURL(new Blob([buffer], { type: 'audio/mp3' }));
        audioPlayer.src = audioURL;
    };

    mediaRecorder.start();
    setTimeout(() => mediaRecorder.stop(), 5000);
}
