// script.js
const video = document.getElementById('video');
const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d');

// Get user media (camera) stream
navigator.mediaDevices.getUserMedia({ video: true })
    .then((stream) => {
        video.srcObject = stream;
    })
    .catch((error) => {
        console.error('Error accessing camera:', error);
    });

// Function to capture image from camera
function captureImage() {
    // Draw the current frame of the video onto the canvas
    ctx.drawImage(video, 0, 0, canvas.width, canvas.height);

    // Convert canvas image to base64 format
    const imageData = canvas.toDataURL('image/jpeg');

    // Send captured image to server for processing (call pred.py functions)
    fetch('/process_image', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ image: imageData })
    })
    .then(response => response.json())
    .then(data => {
        // Handle processed results (display or use them)
        console.log('Processed results:', data);
    })
    .catch(error => {
        console.error('Error processing image:', error);
    });
}

// Call captureImage function when needed (e.g., on button click)
// Example: document.getElementById('captureButton').addEventListener('click', captureImage);
while (true) {
    captureImage();
}