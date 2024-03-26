## Git Push Script (batch file)

This script automates the process of committing changes and pushing them to a Git repository.

**How to Use:**

1. Save the script as a file with a `.bat` extension (e.g., `push.bat`).

2. **(Optional) Add the script to your PATH environment variable for execution from any directory, look at "Adding Script to PATH" for more details.**
    
3. Open a Command Prompt window (CMD). 
    
4. Navigate to your Git repository directory using `cd` (Optional).
    
5. Run the script with the following arguments:
    
    - **First Argument:** The commit message for your changes.
    - **Second Argument (Optional):** The path to your Git repository (if different from the current directory).

**Usage Example:**

```
push.bat "Fixed a bug" "C:\Users\YourUser\MyRepo" // (commit message, path)
push.bat "Added new feature"                      // (commit message, current directory)
```

This will commit changes with the message "Fixed a bug" in the specified repository and push them to the remote branch.

**Example Output (Successful Push):**

```
Repository path: C:\Users\YourUser\MyRepo
Push completed successfully!
Press any key to continue . . .
```

**Example Output (Error: Missing Commit Message):**

```
Error: Please provide a commit message as the first argument.
```

**Features:**

- Checks for missing commit messages and provides informative error messages.
- Handles cases where the repository path is not provided, using the current directory.
- Includes error handling for Git commands (adding, committing, pushing) to provide feedback in case of issues.
- Pushes to the default remote branch ("origin" and "HEAD").
- (Commented-out section for pushing to a specific branch - replace "origin" and "main" with your actual remote and branch names if needed).

**Additional Notes:**

- Ensure you have Git installed and configured with a remote repository before using this script.
- Remember to replace "origin" and "HEAD" in the commented section with your desired remote name and branch name for pushing to a specific branch.
  <hr>
 **Optional: Adding Script to PATH**

For easier execution from any directory, you can add the script's location to your system's PATH environment variable. This allows you to run the script using its name (`push.bat`) instead of specifying the full path.

**Steps:**

1. **Save the Script:** Save the script in a directory that's already included in your PATH (like C:\Windows\System32) or a directory you want to add to your PATH.
2. **Edit Environment Variables** (Detailed instructions provided below)

**Detailed Instructions:**

* Right-click on "This PC" or "My Computer" and select "Properties".
* Navigate to "Advanced system settings" and click on "Environment Variables".
* Under "System variables", find the "Path" variable and click "Edit".
* Add a semicolon (;), followed by the full path to the directory where you saved the script, to the "Variable value" field. Click "OK" on all open dialog boxes.

**Restart Command Prompt:** Close and reopen Command Prompt for the changes to take effect.

**Additional Notes:**

* If you place the script in a directory that's not already in your PATH, remember to add that directory as described above.
* If you encounter issues, ensure you've added the path correctly and restarted Command Prompt.
<hr>

**Disclaimer:**

While this script offers error handling, it's recommended to review your changes and commit messages before pushing.
