#!/bin/bash
set -euo pipefail

LOG_FILE="./server-info.log"

log() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') $1" | tee -a "$LOG_FILE"
}

print_system_info() {
    log "=== System Info ==="
    log "Hostname: $(hostname)"
    log "OS: $(uname -o)"
    log "Kernel: $(uname -r)"
    log "Uptime: $(uptime -p)"
}

print_resources() {
    log "=== Resources ==="
    log "CPU: $(nproc)"
    log "RAM: $(free -h | awk '/Mem:/ {print $3 "/" $2}')"
    log "Disk: $(df -h / | awk 'NR==2 {print $3 "/" $2}')"
}

docker_info() {
    if command -v docker >/dev/null; then
        log "=== Docker ==="
        docker ps --format "table {{.ID}}\t{{.Image}}\t{{.Status}}" | tee -a "$LOG_FILE"
    fi
}

check_services() {
    fail=0
    for url in "$@"; do
        code=$(curl -s -o /dev/null -w "%{http_code}" "$url" || echo 000)
        if [ "$code" == "200" ]; then
            log "[OK] $url ($code)"
        else
            log "[FAIL] $url ($code)"
            fail=1
        fi
    done
    return $fail
}

if [[ "${1:-}" == "--help" ]]; then
    echo "Usage: $0 [url1 url2 ...]"
    exit 0
fi

print_system_info
print_resources
docker_info

if [ "$#" -gt 0 ]; then
    check_services "$@" || exit 1
fi
