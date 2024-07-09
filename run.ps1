# Script PowerShell para gerenciar um projeto FastAPI

function Start-FastAPI {
    Write-Host "Starting FastAPI with uvicorn..."
    uvicorn workout_api.main:app --reload
}

function Create-Migration {
    param (
        [string]$Description
    )

    Write-Host "Creating migration with description: $Description"
    $env:PYTHONPATH="$env:PYTHONPATH;$(Get-Location)"; alembic revision --autogenerate -m "$Description"
}

function Run-Migrations {
    Write-Host "Running database migrations..."
    $env:PYTHONPATH="$env:PYTHONPATH;$(Get-Location)"; alembic upgrade head
}


Start-FastAPI
# Create-Migration -Description "init_db"
# Run-Migrations


