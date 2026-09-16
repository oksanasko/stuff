const prompt = require("prompt-sync")()

function printInfo(){
    console.log("Contact Managment System")
    console.log("----------------------")
    console.log("1. Add a Contact")
    console.log("2. Delete a Contact")
    console.log("3. View Contacts")
    console.log("4. Search Contacts")
    console.log("5. Exit")
}

function addContact(){
    const name = prompt("Name: ")
    const email = prompt("Email: ")
    const contact = {
        name: name,
        email: email
    }
    contacts.push(contact)
    console.log("Added")
}

function deleteContact(){
    console.log("Contact IDs")
    for(let i =0; i < contacts.length; i++){
        const contact = contacts[i]
        console.log((i+1).toString()+":", contact.name)
    }
    const number = parseInt(prompt("Enter an ID: "))
    if(isNaN(number) || number > contact.length){
        console.log("invalid")
        return;
    }
    contacts.splice(number-1,1)
    console.log("Removed")
}

function searchContact(){
    const searchString = prompt("Search: ").toLowerCase()
    const results = [];

    for(const contact of contacts){
        if(contact.name.toLowerCase().includes(searchString)) results.push(contact)
    }
    listContact(results)
}

function listContact(contacts){
    for(let contact of contacts){
        console.log("######")
        console.log("Name:  ", contact.name)
        console.log("Email: ", contact.email)
    }
}

printInfo()

const contacts=[]

let keepGoing = true;
while(keepGoing){
const number = prompt("Enter an operation(1-5): ")
switch(number){
    case "1":
        addContact()
        break;
    case "2":
        deleteContact();
        break;
    case "3":
        listContact(contacts); // pass contacts
        break;
    case "4":
        searchContact();
        break;
    case "5":
        keepGoing=false;
        break;
    default:
        console.log("unknow");
}}



/* const arr = [1, 2, 3, 4] <- mutable(can be changed)
arr.push()
arr.pop()
arr.splice(index) or (from, howmuch)
arr[0] = 9 <- changes
console.log(arr)
const contacts ={ <- objects
    name: "Tim",
    email: "tim@gmail.com"
}
*/
          