package entities

type Player struct {
	Archers      int `json:"archers"`
	Cavalry      int `json:"cavalry"`
	Infantry     int `json:"infantry"`
	SiegeWeapons int `json:"siege"`
}
