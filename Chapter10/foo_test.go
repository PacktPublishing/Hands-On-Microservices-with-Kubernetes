package main

import (
	"testing"
)

func TestExactResult(t *testing.T) {
	result, err := safeDivide(8, 4)
	if err != nil {
		t.Errorf("8 / 4 expected 2,  got error %v", err)
	}

	if result != 2 {
		t.Errorf("8 / 4 expected 2,  got %d", result)
	}
}

func TestIntDivision(t *testing.T) {
	result, err := safeDivide(14, 5)
	if err != nil {
		t.Errorf("14 / 5 expected 2,  got error %v", err)
	}

	if result != 2 {
		t.Errorf("14 / 5 expected 2,  got %d", result)
	}
}

func TestDivideByZero(t *testing.T) {
	result, err := safeDivide(77, 0)
	if err == nil {
		t.Errorf("77 / 0 expected 'division by zero' error,  got result %d", result)
	}

	if err.Error() != "division by zero" {
		t.Errorf("77 / 0 expected 'division by zero' error,  got this error instead %v", err)
	}
}
