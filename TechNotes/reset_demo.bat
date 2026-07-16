@echo off
chcp 65001 >nul
echo ============================================
echo    TechNotes 演示仓库重置脚本
echo ============================================
echo.

cd /d "%~dp0"

echo [1/4] 切换到 master 分支...
git checkout master

echo [2/4] 重置工作区...
git reset --hard HEAD
git clean -fd

echo [3/4] 更新所有分支...
git checkout feature/git-enhance
git reset --hard origin/feature/git-enhance 2>nul || echo 本地分支已重置

git checkout feature/ai-integrate
git reset --hard origin/feature/ai-integrate 2>nul || echo 本地分支已重置

git checkout bugfix/fix-settings
git reset --hard origin/bugfix/fix-settings 2>nul || echo 本地分支已重置

git checkout master

echo [4/4] 重置完成！
echo.
echo 当前分支状态：
git branch -a

echo.
echo ============================================
echo    演示环境已准备就绪！
echo ============================================
pause
