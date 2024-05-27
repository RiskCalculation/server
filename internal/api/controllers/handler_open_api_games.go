package controllers

import (
	"RiskCalculator/internal/api/dto"
	"RiskCalculator/internal/api/helpers"
	"RiskCalculator/internal/services"
	"fmt"
	"log"
	"net/http"
)

type RiskApiGames interface {
	Calculator(w http.ResponseWriter, r *http.Request)
}

type riskApiGames struct {
	caclService services.CaclService
	json        *helpers.JsonResponse
}

func NewRiskApiGames() RiskApiGames {
	return &riskApiGames{
		json:        &helpers.JsonResponse{},
		caclService: services.NewCalcService(),
	}
}

func (risk *riskApiGames) Calculator(w http.ResponseWriter, r *http.Request) {
	log.Println("GameProcessor")
	req := &dto.CalcRequest{}
	_, err := helpers.ReadJSON(w, r, req)

	if err != nil {
		log.Println(fmt.Sprintf("Error reading request: %s", err))
		_ = risk.json.WriteJSONError(w, fmt.Errorf("invalid request Paylod %v", err), http.StatusBadRequest)
		return
	}

	resp, err := risk.caclService.CalculateBattleResult(&req.AttackPlayer, &req.DefendPlayer)

	res := &helpers.JsonResponse{
		Error:   false,
		Message: "Processed Game Request",
		Data:    resp,
	}

	_ = res.WriteJSON(w, http.StatusOK, nil)
}
