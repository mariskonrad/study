// named function, called `myFunction`
function myFunction() {

}

// annonymous function attributed to `myFunction` constant.
// `myFunction` is not the name of the function, just the constant (or variable) that points to it.
const myFunction = function() {

}

// function called `myFunction2` set to a constant called `myFunction1`
const myFunction1 = function myFunction2() {

}

// arrow functions are always anonymous
const myFunction1 = () => {}
const myFunction1 = (a) => {}
const myFunction1 = a => {}
const myFunction1 = (a, b) => {}
const myFunction1 = (a) => {
  a + 1
  // no explicit return, returns undefined implicitly
}

const myFunction1 = (a) => {
  return a + 1
}
// same as:
const myFunction1 = (a) => a + 1
