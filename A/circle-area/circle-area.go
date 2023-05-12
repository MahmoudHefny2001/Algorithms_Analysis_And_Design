package main

import (
	"fmt"
)

func main() {
	fmt.Println(area(10))
	fmt.Println(area(20))

}

func area(r float32) float32 {
	var a float32 = 3.1415 * (r * r)
	return a
}
