const body = document.getElementsByTagName("body")[0]
const input = document.getElementById("inputColor")
const inputcolor = input.value;

function setColor(name){
    body.style.backgroundColor = name
}

function randomColor(){
    const red = Math.round(Math.random()*255)
    const green = Math.round(Math.random()*255)
    const blue = Math.round(Math.random()*255)

    const color = `rgb(${red}, ${green}, ${blue})`
    body.style.backgroundColor = color
}

function setColorfromInput(){
    const inputcolor = input.value;
    setColor(inputcolor);
}

function addnewButton(){
    const newButton = document.createElement("button")
    const buttonscolor = body.style.backgroundColor
    newButton.style.backgroundColor = buttonscolor
    newButton.onclick = () => setColor(buttonscolor)
    body.appendChild(newButton)
}