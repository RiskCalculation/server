package controllers

import (
	"RiskCalculator/internal/api/helpers"
	"fmt"
	"net/http"
	"net/http/httptest"
	"strings"
	"testing"
)

var testPayload = `{"api":"balance","data":{"game_session_id":"16e2ea64-5725-40a4-99cc-c5c0deb8568d","currency":"BTC","denomination":0,"spin_meta":{},"bet_meta":{"bets":0},"notes":{"notes":""}}}`

// TestNewOpenApiGames tests the handler GameProcessor
func createTestPayloadSecret() string {
	helpers.Secret = "1234"
	fmt.Println(helpers.GenerateSignature(testPayload))
	return helpers.GenerateSignature(testPayload)

}

func TestGameProcessor(t *testing.T) {
	// Create a new instance of the handler
	h := NewOpenApiGames(nil)

	payload := createTestPayloadSecret()

	//convert payload to io.Reader
	payloadReader := strings.NewReader(testPayload)
	// Create a new request
	req := httptest.NewRequest("POST", "/api/v1/games-processor", payloadReader)
	req.Header.Set("Sign", payload)

	// Create a new response recorder
	rr := httptest.NewRecorder()

	// Call the handler
	h.GameProcessor(rr, req)

	fmt.Println(rr.Body.String())
	// Check the status code
	if rr.Code != http.StatusOK {
		t.Errorf("expected status code 200, got %d", rr.Code)
	}

}
