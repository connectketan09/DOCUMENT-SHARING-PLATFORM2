function uploadFile() {

    let file = document.getElementById("fileInput").files[0];

    if (!file) {
        alert("Please select a file first");
        return;
    }

    let formData = new FormData();
    formData.append("file", file);

    fetch("/upload/", {
        method: "POST",
        body: formData
    })
    .then(res => res.json())
    .then(data => {
        window.location.href = "/processing/" + data.vault_id + "/";
    });

}