document.addEventListener('DOMContentLoaded', function() {
    const videoElement = document.getElementById('videoElement');
    const startButton = document.getElementById('startButton');
    const stopButton = document.getElementById('stopButton');
    const statusDiv = document.getElementById('status');
    const permissionModal = new bootstrap.Modal(document.getElementById('permissionModal'), {
        keyboard: true,
        backdrop: true
    });


    async function startVideo() {
        try {
            const stream = await navigator.mediaDevices.getUserMedia({ video: true });
            videoElement.srcObject = stream;
            videoElement.style.display = 'block'; // Show video
            startButton.style.display = 'none'; // Hide start button
            stopButton.style.display = 'inline-block'; // Show stop button
            statusDiv.innerText = 'Detecting faces...';
            videoElement.play();
        } catch (error) {
            console.error('Error accessing the camera:', error);
            statusDiv.innerText = 'Failed to access the camera. Please ensure you have given the necessary permissions and that your device has a camera.';
        }
    }


    function stopVideo() {
        const stream = videoElement.srcObject;
        if (stream) {
            const tracks = stream.getTracks();
            tracks.forEach(track => track.stop());
        }
        videoElement.style.display = 'none'; // Hide video
        stopButton.style.display = 'none'; // Hide stop button
        startButton.style.display = 'inline-block'; // Show start button
        statusDiv.innerText = 'Camera stopped. Click "Start Camera" to begin again.';
    }


    startButton.addEventListener('click', function() {
        permissionModal.show();
    });


    document.getElementById('grantAccess').addEventListener('click', async () => {
        permissionModal.hide();
        await startVideo();
    });


    stopButton.addEventListener('click', stopVideo);
});



