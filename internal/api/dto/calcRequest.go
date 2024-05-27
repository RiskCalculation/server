package dto

import "RiskCalculator/internal/entities"

type CalcRequest struct {
	AttackPlayer entities.Player `json:"attack_player"`
	DefendPlayer entities.Player `json:"defend_player"`
}
