function uploadFile(){

let file = document.getElementById("fileInput").files[0];

let formData = new FormData();

formData.append("file", file);

fetch("/upload/",{

method:"POST",

body:formData

})

.then(response => response.json())

.then(data =>{

window.location = "/processing/" + data.id

})

}