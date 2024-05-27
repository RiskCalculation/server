package main

import (
	"RiskCalculator/config"
	"RiskCalculator/internal/api"
)

type App struct {
	Routes *api.Routes
}

func NewApp(cfg *config.Repository) *App {
	return &App{
		Routes: api.NewRoutes(cfg),
	}
}
