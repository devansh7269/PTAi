let currentImageUrl = null;

async function uploadImage(endpoint) {
    const fileInput = document.getElementById("fileInput");
    if (!fileInput.files.length) {
        alert("Please select an image first!");
        return;
    }

    const formData = new FormData();
    formData.append("image", fileInput.files[0]);

    try {
        const response = await fetch(`http://127.0.0.1:5000/${endpoint}`, {
            method: "POST",
            body: formData
        });

        if (response.ok) {
            const blob = await response.blob();
            currentImageUrl = URL.createObjectURL(blob);

            document.getElementById("outputImage").src = currentImageUrl;
            document.getElementById("downloadBtn").style.display = "inline-block"; // show download button
        } else {
            const err = await response.text();
            alert("❌ Error: " + err);
        }
    } catch (error) {
        alert("⚠️ Failed to connect to server: " + error);
    }
}

function downloadImage() {
    if (!currentImageUrl) return;
    const a = document.createElement("a");
    a.href = currentImageUrl;
    a.download = "processed_image.png";
    a.click();
}
