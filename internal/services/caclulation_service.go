package services

import (
	"RiskCalculator/internal/entities"
	"bytes"
	"encoding/json"
	"fmt"
	"os/exec"
)

type BattleResult struct {
	AttackerWinRate float64 `json:"attacker_win_rate"`
	DefenderWinRate float64 `json:"defender_win_rate"`
	DrawRate        float64 `json:"draw_rate"`
}

type CaclService interface {
	CalculateBattleResult(attackPlayer, defendPlayer *entities.Player) (*BattleResult, error)
}

type calcService struct {
}

func NewCalcService() CaclService {
	return &calcService{}
}

func (c *calcService) CalculateBattleResult(attackPlayer, defendPlayer *entities.Player) (*BattleResult, error) {
	attackJSON, err := json.Marshal(attackPlayer)
	if err != nil {
		fmt.Println("Error marshalling attack:", err)
		return nil, err
	}

	defenderJSON, err := json.Marshal(defendPlayer)
	if err != nil {
		fmt.Println("Error marshalling defender:", err)
		return nil, err
	}

	// Execute the Python script
	cmd := exec.Command("python3", "analyse/battle_calculator.py", string(attackJSON), string(defenderJSON))
	var out bytes.Buffer
	cmd.Stdout = &out
	err = cmd.Run()
	if err != nil {
		fmt.Println("Error executing command:", err)
		return nil, err
	}

	var result BattleResult
	err = json.Unmarshal(out.Bytes(), &result)
	if err != nil {
		fmt.Println("Error unmarshalling result:", err)
		return nil, err
	}

	return &result, nil
}
