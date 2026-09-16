const prompt =require("prompt-sync")()

function makemove(turn, board){
    while(true){
        let row = parseInt(prompt("Enter row: "))
        let col = parseInt(prompt("Enter col: "))

        if(isNaN(row)||row<1||row>3) console.log("invalid row")
        else if(isNaN(col)||col<1||col>3) console.log("invalid col")
        else if(board[row-1][col-1] !== " ") console.log("invalid position")
        else{
            board[row-1][col-1] = turn
            break}
    }
}

function printBoard(board){
    for(let i =0; i<board.length; i++){
        let row = board[i]
        let rowString = ""
        for(let j =0; j<row.length; j++){
            rowString += row[j]
            if(j !== row.length -1) rowString += " | "
        }
        console.log(rowString)
        if (i !== board.length-1) console.log("---------")
    }
}

let board = [
    [" "," "," "],
    [" "," "," "],
    [" "," "," "]
]

// makemove("X", board)
// console.log(board)
// makemove("O", board)
// console.log(board)

let turn ="X";
let turnCount =0;

printBoard(board)
console.log()
while(turnCount<9){
    makemove(turn, board)
    printBoard(board)

    if(turn === "X") turn ="O"
    else turn ="X"
    turnCount++;
}
