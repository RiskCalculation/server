package config

type Database struct {
	Host         string `json:"host"`
	Port         int    `json:"port"`
	User         string `json:"user"`
	Password     string `json:"password"`
	DBName       string `json:"dbname"`
	RestartCount int64  `json:"restart_count"`
}
type Repository struct {
	Env      string   `json:"env"`
	RESTPort int      `json:"rest_port"`
	DB       Database `json:"database"`
	Secret   string   `json:"secret"`
}

func Default() *Repository {
	return &Repository{
		Env:      "dev",
		RESTPort: 8080,
		DB: Database{
			Host:         "postgres",
			Port:         5432,
			User:         "postgres",
			Password:     "password",
			DBName:       "players",
			RestartCount: 10,
		},
		Secret: "1234",
	}
}

func New() *Repository {
	return Default()
}
