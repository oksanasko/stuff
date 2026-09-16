console.log("hello world")
const prompt = require("prompt-sync")()
const name = prompt("What is your name? ")
console.log("Hello,", name, "welcome to our game")

const shouldWePlay = prompt("Do you want to play? ")

//comment "7" == 7 -> true; "7" === 7 -> false;
// && -> and; || -> or; ! -> not;
//console.log(condition)

if (shouldWePlay.toLowerCase() === "yes") {
    console.log("okay, we will play!")
    //game logic
    const leftorright = prompt("You enter a maze, do you want to go left or right? ")
    if (leftorright === "left"){
        console.log("You go to left and see a bridge ")
        const cross = prompt("Do you want to cross the bridge? ").toLowerCase()
        if(cross === "yes" || "cross"){
            console.log("You cross but the bridge was weak and you fell")
        }else{
            console.log("good choice")
        }
    } else {
        console.log("You go right and fall off a cliff...")
    }




} else if(shouldWePlay.toLowerCase() === "no"){
    console.log("okay :(")
} else{
    console.log("invalid input")
}