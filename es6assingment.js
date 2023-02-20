/*Refactor the following function into a one-liner:
const printName = (name) => {
                     return “Hi” + name;
           }*/
const printName = (name) => "hi "+name;

console.log(printName("VEDA"));
/*Rewrite the following code using template literals
const printBill = (name, bill) => {
                     return “Hi “ + name + “, please pay: “ + bill;
           }*/




const printBill = (name, bill) => `hi ${name} , please pay: ${bill}` ;

/*Modify the following code such that the object properties are destructured and logged.
const person = {
                      name: “Noam Chomsky”,
                      age: 92
            }
           
           let name = person.name;
           let age = person.age;
           console.log(name);
           console.log(age);*/

console.log(printBill("VEDA",100))

const person = {
                      name1: "Veda Priya",
                      age: 21
            }
            let {name1, age} = person;
           
           console.log(name1);
           console.log(age);