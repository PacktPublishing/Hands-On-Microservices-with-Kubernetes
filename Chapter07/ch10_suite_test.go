package main_test

import (
	. "github.com/onsi/ginkgo"
	. "github.com/onsi/gomega"

	"testing"
)

func TestCh10(t *testing.T) {
	RegisterFailHandler(Fail)
	RunSpecs(t, "Ch10 Suite")
}
