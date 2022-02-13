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
  $("loading-spinner").style.display = "block";
  e.preventDefault();
  const data = new FormData();
  data.append("file", e.target.file.files[0]);
  data.append("ratio", e.target.ratio.value);
  await fetch(`${API}/upload`, { method: "POST", body: data })
    .then((r) => r.json())
    .then((data) => {
      $("loading-spinner").style.display = "none";
      $("transcript").textContent = "";
      Object.entries(data.main).forEach(([k, v]) => {
        $("transcript").innerHTML += `<b>${time}:</b> ${v}<br><br>`;
      });
      $("summary").textContent = "";
      Object.entries(data.summarized).forEach(([k, v]) => {
        $("summary").innerHTML += `<b>${time}:</b> ${v}<br><br>`;
      });
      console.log(data);
    })
    .catch((e) => {
      $("loading-spinner").style.display = "none";
      console.log(e);
    });
}
