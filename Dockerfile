FROM golang:1.22.1-alpine AS builder

WORKDIR /app

COPY go.mod go.sum ./

COPY . .

RUN CGO_ENABLED=0 GOOS=linux go build  -o calculation-service ./cmd


FROM alpine:latest
WORKDIR /root/
COPY --from=builder /app/calculation-service .
CMD ["./calculation-service"]