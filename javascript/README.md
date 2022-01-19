# Javascript

## global object

Every Javascript runtime has a global object.

You can have variables scoped to functions or blocks, and you can have "global" variables. Global variables are actually properties of the global object.

Example:
```js
myGlobalVar = 'hi'
// actually means
global.myGlobalVar = 'hi'
```

In the browser, the global object is called `window`. In NodeJS, it is called `global`.

Everything you can access in the global scope is a property of the global object. Examples in the browser: `document`, `alert()`, `parseInt()`.

## variable declaration

- (nothing): global. Do not use.
  ```js
  function a() {
    myName = 'Maris'
  }

  console.log(window.myName) // undefined
  a()
  // now `myName` is defined, even though it was defined inside of the function `a`, because it was a global declaration
  console.log(window.myName) // 'Maris'
  ```
- var: function scope (hoisting). Do not use.
  ```js
  function b() {
    console.log(nome) // this seems like an error of "nome is not defined", but it actually is defined (as `undefined`) because of hoisting

    if (1 > 0) {
      var nome = 'rafael'
    }

    console.log(nome)
  }
  ```

  The variable `nome` gets hoisted to the top of the enclosing function. There's no block scope, only function scope. This is equivalent to:
  ```js
  function b() {
    var nome
    console.log(nome)

    if (1 > 0) {
      nome = 'rafael'
    }

    console.log(nome)
  }
  ```

- let: variable with block scope
  ```js
  function b() {
    // `nome` doesn't exist here

    if (1 > 0) {
      let nome = 'rafael'
    }

    // `nome` doesn't exist here
  }
  ```

- const: constant with block scope. Once set, doesn't allow changing the value.

## truthy and falsy

In certain contexts, any value will be interpreted as a boolean value.

Example: as a condition in an `if` statement

```js
// this is valid in JS
if (1) {

}
```

So every value in JS can be interpreted as being either "truthy" or "falsy".

6 things are "falsy" (actually a couple more, but they are too weird and don't usually happen in practice):
- `false`
- `0`
- `''` (empty string, doesn't matter which quotes we use)
- `null`
- `undefined`
- `NaN`

All the other values are "truthy".

## implicit type coercion

A non-boolean value can be converted to its oposing boolean value by prepending a `!`. Example:
```js
var a = 0 // 0, so "falsy"
var b = !a // true (the actual boolean value)
var c = !b // false (the actual boolean value)
```

So to convert any value to its boolean representation, we can use `!!`:
```js
var a = 0 // 0, so "falsy"
var c = !!a // false
```

This is called: "bang-bang: you are boolean".

Another example of type coercions:
```js
var a = 1
var b = '2'
var c = a + b
console.log(c) // '12'
// it converts 1 to '1' and appends '2' to it
```

So, for instance, this converts an integer to a string:
```js
var a = 1234
var b = '' + a
console.log(b) // '1234'
```

All that said, avoid using these tricks when possible.

## === vs ==

`===` checks for strict equality. So:
- `1 === 1` is `true`
- `1 === '1'` is `false`

`==` checks for equality using a long and complex algorithm that performs several type coercions. So:
- `1 == 1` is `true`
- `1 == '1'` is also `true`

`===` is simple and does what you expect. Never use `==`.

## undefined, null

- `undefined` is the default value given by the language for something that was not previously initialized.
- `null` is never used by the language by default, so is a way for the programmer to explicitly set an empty value to something.

Examples:
```js
function a(paramA) {
  console.log('paramA:', paramA)
}

a('some value')
a() // passing nothing, the function gets `undefined` as parameter
const returnValue = a('checking the return value') // the function returns nothing, so implicitly returns `undefined`
console.log('return value', returnValue)
```

## sync vs async

Several of the most popular languages are primarily synchronous: C, Python, Java, Go.

Javascript is primarily asynchronous.

Example in pseudocode:

- synchronous: the numbers indicate the order of execution
  ```
  // 1. the execution waits on `makeNetworkCall` until the network call returns, even if it takes several seconds
  let result = makeNetworkCall(url)

  // 2. this only executes when the network call finished
  doSomething(result)

  // 3. other code that gets executed after `doSomething`
  ```

- asynchronous: the numbers indicate the order of execution
  ```
  // 1. The execution doesn't wait on `makeNetworkCall`. The network call is made
  makeNetworkCall(url, function(result) {
    // 3. This only executes when the network call finished. This is called a callback function.
    doSomething(result)
  })

  // 2. other code that gets executed after `makeNetworkCall`
  ```

Asynchronous code uses callbacks. Do something asynchronously and call me back with the result when you are finished.

Later, other mechanisms like Promises were introduced, but they follow the same principle.

Examples:
```
exemplo do garçom síncrono

- garçom pega o pedido da mesa 1, leva até a cozinha, espera o pedido ficar pronto
- entrega o pedido para a mesa 1
- garçom pega o pedido da mesa 2, leva até a cozinha, espera o pedido ficar pronto
- entrega o pedido para a mesa 2


let comida1 = pegaPedido(mesa1)
entregaComida(comida1)

let comida2 = pegaPedido(mesa2)
entregaComida(comida2)


exemplo do garçom assíncrono

- garçom pega o pedido da mesa 1, leva até a cozinha, pede para avisarem quando ficar pronto
- garçom pega o pedido da mesa 2, leva até a cozinha, pede para avisarem quando ficar pronto
- garçom espera
- entrega o pedido para a mesa 2
- entrega o pedido para a mesa 1


pegaPedido(mesa1, function(comida1) {
  entregaComida(comida1)
})

pegaPedido(mesa2, function(comida2) {
  entregaComida(comida2)
})
```

## undefined variable vs undefined object property

Trying to access an undefined variable is an error.

Trying to access an undefined property of an object results in `undefined`.

Example:
```js
console.log(someVar) // error is `someVar` was never defined

const myObject = {}
console.log(myObject.someProperty) // `undefined`
```
