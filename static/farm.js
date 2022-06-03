function grow (drug) {
    var xhr = new XMLHttpRequest();
    xhr.open("GROW", `/api/v1/grow/${drug}`, true);

    xhr.onreadystatechange = function() {
        if (this.readyState === XMLHttpRequest.DONE && this.status === 200) {
            console.log(xhr.response)
        };
    };
    xhr.send(null);
}

function get_drugs () {
    var xhr = new XMLHttpRequest();
    xhr.open("HOWMANYNIGGASSMOKIN", '/api/v1/drugs', true);

    xhr.onload = function () {
        response = JSON.parse(xhr.response)
        document.getElementById("grownMeth").innerHTML = response['grown']['meth'];
        document.getElementById("grownCocaine").innerHTML = response['grown']['cocaine'];
        document.getElementById("totalMeth").innerHTML = response['totals']['meth'];
        document.getElementById("totalCocaine").innerHTML = response['totals']['cocaine'];
    };
}