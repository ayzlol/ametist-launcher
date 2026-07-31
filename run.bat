@echo off
title Ametist Launcher
echo Ametist Launcher baslatiliyor...
python Ametist.py
if %errorlevel% neq 0 (
    echo.
    echo Program bir hata ile kapandi veya Python yuklu degil.
    pause
)
