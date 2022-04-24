Array ...


findIndex: recebe uma função `fn`, retorna um int
fn: recebe um item do array e retorna um bool. Esse bool indica se o item do array é o item que procuramos.

Array.prototype.findIndex = (fn) => {
  for (let i = 0; i < this.length; i++) {
    if (fn(this[i])) {
        return i
    }
  }
  return -1
}
