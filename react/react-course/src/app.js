import {createRoot} from "react-dom/client"

// the root element is where ReactDOM will render the UI
const root = document.querySelector("root")

// this method receives a virtual representation of a React Element and makes it visible in the actual DOM
// createRoot(root).render(element)
createRoot(root).render(React.createElement("p", {}, "Hello World"))
