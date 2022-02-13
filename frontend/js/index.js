const $ = (id) => document.getElementById(id);
const API = "http://127.0.0.1:4996";

function selectedvideo(self) {
  var file = self.files[0];
  var reader = new FileReader();

  reader.onload = function (e) {
    var src = e.target.result;
    var video = document.getElementById("videoplayer");
    var source = document.getElementById("source");

    source.setAttribute("src", src);
    video.load();
    video.play();
  };

  reader.readAsDataURL(file);
}

async function uploadVideo(e) {
  e.preventDefault();
  const data = new FormData();
  data.append("file", e.target.file.files[0]);
  await fetch(`${API}/upload`, { method: "POST", body: data })
    .then((r) => r.json())
    .catch((e) => {
      console.log(e);
    });
}