function Onload () {
    let meth = parseInt(localStorage.getItem("Meth"));
    let coke = parseInt(localStorage.getItem("Coke"));

    if (meth == null) {
        localStorage.setItem("Meth", parseInt(0));
    } else if (isNaN(meth)) {
        localStorage.setItem("Meth", parseInt(1));
    }

    if (coke == null) {
        localStorage.setItem("Coke", parseInt(0));
    } else if (isNaN(coke)) {
        localStorage.setItem("Coke", parseInt(1));
    }

    document.getElementById("meth_smoked").innerHTML = localStorage.getItem("Meth");
    document.getElementById("coke_smoked").innerHTML = localStorage.getItem("Coke");

    Get_Drugs();
}

function Smoke (drug) {
    var xhr = new XMLHttpRequest();
    xhr.open("SMOKE", `/api/v1/smoke/${drug}`, true);

    xhr.onreadystatechange = function() {
        if (this.readyState === XMLHttpRequest.DONE && this.status === 200) {
            console.log(xhr.response)
            if (drug == "cocaine") {
                localStorage.setItem("Coke", parseInt(localStorage.getItem("Coke"))+1);
            } else if (drug == "meth") {
                localStorage.setItem("Meth", parseInt(localStorage.getItem("Meth"))+1);
            }
        };
    };
    xhr.send(null);
    Get_Drugs();
}

function Get_Drugs () {
    var xhr = new XMLHttpRequest();
    xhr.open("HOWMANYNIGGASSMOKIN", '/api/v1/drugs', true);

    xhr.onload = function () {
        response = JSON.parse(xhr.response)
        document.getElementById("global_meth_smoked").innerHTML = response['meth'];
        document.getElementById("global_coke_smoked").innerHTML = response['cocaine'];
        document.getElementById("meth_smoked").innerHTML = localStorage.getItem("Meth");
        document.getElementById("coke_smoked").innerHTML = localStorage.getItem("Coke");
    };
    xhr.send(null);
}