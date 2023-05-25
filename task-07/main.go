package main

import (
	"syscall/js"
)

var counter int

func incfunc(this js.Value, args []js.Value) interface{} {
	counter++
	updateCounter()
	return nil
}

func decfunc(this js.Value, args []js.Value) interface{} {
	counter--
	updateCounter()
	return nil
}

func resetfunc(this js.Value, args []js.Value) interface{} {
	counter = 0
	updateCounter()
	return nil
}

func updateCounter() {
	js.Global().Get("document").Call("getElementById", "int").Set("innerHTML", counter)
}

func registerCallbacks() {
	js.Global().Set("incfunc", js.FuncOf(incfunc))
	js.Global().Set("decfunc", js.FuncOf(decfunc))
	js.Global().Set("resetfunc", js.FuncOf(resetfunc))
}

func main() {
	counter = 0
	registerCallbacks()
	select {}
}
