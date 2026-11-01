// Run as a standalone tool: go run tools/check-format.go <maintained-path> [...].
// Choose paths explicitly; vendor/generated exclusions belong to the project's inventory.
package main

import (
	"fmt"
	"os"
	"os/exec"
)

func main() {
	if len(os.Args) < 2 {
		fmt.Fprintln(os.Stderr, "Supply at least one maintained Go file or directory")
		os.Exit(2)
	}
	command := exec.Command("gofmt", append([]string{"-l", "--"}, os.Args[1:]...)...)
	command.Stderr = os.Stderr
	output, err := command.Output()
	if err != nil {
		fmt.Fprintln(os.Stderr, err)
		os.Exit(2)
	}
	if len(output) > 0 {
		fmt.Fprintln(os.Stderr, "Run gofmt on these files:")
		fmt.Fprint(os.Stderr, string(output))
		os.Exit(1)
	}
}
