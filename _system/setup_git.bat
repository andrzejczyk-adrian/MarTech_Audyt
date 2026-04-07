@echo off
echo ================================================
echo  MarTech Audyt — Git Setup
echo  Repo: andrzejczyk-adrian/MarTech_Audyt
echo ================================================
echo.

cd /d "C:\Users\adria\Documents\AI\AUDYT\MarTech"

REM Inicjalizuj git jeśli brak
if not exist ".git" (
    git init
    echo [OK] git init
) else (
    echo [OK] .git juz istnieje
)

REM Ustaw remote
git remote remove origin 2>nul
git remote add origin https://github.com/andrzejczyk-adrian/MarTech_Audyt.git
echo [OK] remote origin ustawiony

REM Ustaw branch main
git checkout -b main 2>nul || git checkout main

REM Pierwszy commit
git add .
git commit -m "init: system plikow MarTech Audyt"

REM Push
git push -u origin main

echo.
echo ================================================
echo  GOTOWE! Repo skonfigurowane.
echo  Kolejne zmiany: git add . && git commit -m "opis" && git push
echo ================================================
pause
