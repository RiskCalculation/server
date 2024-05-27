package main

import (
	"RiskCalculator/config"
	"fmt"
	"log"
	"net/http"
)

func main() {
	cfg := config.New()

	app := NewApp(cfg)

	srv := &http.Server{
		Addr:    fmt.Sprintf(":%d", cfg.RESTPort),
		Handler: app.Routes.Routes(),
	}

	//start server
	err := srv.ListenAndServe()
	if err != nil {
		log.Fatal(err)
	}

}
