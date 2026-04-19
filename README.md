# Fall Detection Server

A FastAPI-based backend service for a Raspberry Pi + MPU6050 fall detection system.  
This project receives fall events from a Raspberry Pi device, stores them in `data/events.json`, and provides a web dashboard for monitoring.

## Features

- Receive fall events from Raspberry Pi devices
- Store event records in JSON format
- Provide a simple dashboard page
- Support Docker / Docker Compose deployment
- Support configurable external port with `.env`

## Project Structure

```text
.
├── Dockerfile
├── app
│   ├── main.py
│   ├── schemas.py
│   ├── storage.py
│   └── routers
│       ├── events.py
│       └── pages.py
├── data
│   └── events.json
├── docker-compose.yml
├── down.sh
├── init.sh
├── requirements.txt
├── start.sh
├── static
│   └── styles.css
└── templates
    └── dashboard.html
```

## Requirements

- Python 3.11+
- Docker
- Docker Compose

## Local Development

### 1. Create virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the server

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

### 4. Open in browser

- Dashboard: `http://127.0.0.1:8000/dashboard`

## Docker Deployment

### 1. Create `.env`

Create a `.env` file in the project root:

```env
PORT=16777
```

You can change the external port by editing this file.

### 2. Build and start

```bash
docker-compose up -d --build
```

### 3. Stop the service

```bash
docker-compose down
```

## Helper Scripts

### Initialize

```bash
./init.sh
```

### Start service

```bash
./start.sh
```

### Stop service

```bash
./down.sh
```

## API Endpoints

### `POST /api/fall-event`

Receive a fall event from Raspberry Pi.

Example request:

```json
{
  "device_id": "raspberrypi-01",
  "event_type": "fall_detected",
  "acc_magnitude": 2.8,
  "gyro_magnitude": 190.5,
  "timestamp": "2026-04-19T17:00:00"
}
```

### `GET /dashboard`

Render the web dashboard.

## Data Storage

Fall event data is stored in:

```text
data/events.json
```

This file is ignored by Git and is intended for runtime data only.

## Environment Variables

Example `.env`:

```env
PORT=16777
```

Recommended practice:
- Keep `.env` in `.gitignore`
- Commit only `.env.example`

## Notes

- The container internally runs on port `8000`
- Docker maps `${PORT}:8000`
- For lab deployment, set `PORT=16777`

## License

For academic and project use only.