@echo off

REM Get the commit message from the first command line argument
set "COMMIT_MESSAGE=%1"

REM Get the repository path from the second command line argument
set "REPO_PATH=%2"

REM Check if a commit message was provided
if %COMMIT_MESSAGE=='' (
  echo Error: Please provide a commit message as the first argument.
  exit /b 1
)

REM Check if a repository path was provided
if %REPO_PATH=='' (
  echo Warning: Repository path was not provided, repository path is now the current path.

  REM Use the current directory as the repository path
  set "REPO_PATH=%CD%"
)

REM Change directory with error handling
pushd %CD% >nul 2>&1
if errorlevel 1 (
  echo Error: Failed to change directory. Please check the path.
  exit /b 1
)
echo Repository path: %REPO_PATH%
cd %REPO_PATH%

REM Add all changes to the staging area and handle potential errors
git add .
if errorlevel 1 (
  echo Error: Failed to add changes. Check for issues in your Git repository.
  popd
  exit /b 1
)

REM Commit changes with the provided message
git commit -m %COMMIT_MESSAGE%
if errorlevel 1 (
  echo Error: Failed to commit changes. Review your commit message or Git configuration.
  popd
  exit /b 1
)

REM Push to the default remote branch (origin and current branch)
git push origin HEAD

REM Push changes to the remote repository (replace "origin" with your remote name and "main" with your branch name)
REM git push origin main

popd
echo Push completed successfully!

pause
