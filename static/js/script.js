function generatePrompt() {
    var btn = document.getElementById("generateButton");
    var concept = document.getElementById("inputConcept").value;
    if(concept !== "") {
        btn.disabled = true;
        btn.innerHTML = "Generate...";

        fetch('/generate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({concept: concept})
        })
        .then(response => response.json())
        .then(data => {
            btn.disabled = false;
            btn.innerHTML = "Generate prompt";
            document.getElementById("copyText").value = data;
        })
        .catch((error) => {
            btn.disabled = false;
            btn.innerHTML = "Generate prompt";
            console.error('Error:', error);
        });
    } else {
        alert("enter a concept please!");
    }
   /*
    var concept = document.getElementById("inputConcept").value;
    if(concept !== "") {
        document.getElementById("copyText").value = concept;
    } else {
        alert("请输入概念！");
    }
    */
}


function copyText() {
    var copyText = document.getElementById("copyText");
    copyText.select();
    document.execCommand("copy");
    /*alert("已复制: " + copyText.value);*/
}
