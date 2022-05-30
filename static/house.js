function Onload () {
    let smoke = parseInt(localStorage.getItem("smoke"));

    if (smoke == null) {
        localStorage.setItem("smoke", parseInt(0));
    } else if (isNaN(smoke)) {
        localStorage.setItem("smoke", parseInt(1));
    }

    document.getElementById("meth_smoked").innerHTML = localStorage.getItem("smoke");
}

function Smoke () {
    localStorage.setItem("smoke", parseInt(localStorage.getItem("smoke"))+1);

    document.getElementById("meth_smoked").innerHTML = localStorage.getItem("smoke");

    var xhr = new XMLHttpRequest();
    xhr.open("SMOKE", '/api/v1/smoke', true);

    xhr.onreadystatechange = function() {
        if (this.readyState === XMLHttpRequest.DONE && this.status === 200) {
            console.log("e")
        }
    }
    xhr.send(null);
}