# Create virtual environment in workspace
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Upgrade pip in virtual environment
pip install --upgrade pip

# Install required packages
pip install requests

# Run the Python script to check tickets
python /Users/abhinavvarmakalidindinagavenkata/.jenkins/workspace/check_tickets/check_tickets.py

# Check if the trigger file exists and run hello_world.py if it does
if [ -f "trigger_hello_world.txt" ]; then
    python /Users/abhinavvarmakalidindinagavenkata/.jenkins/workspace/check_tickets/hello_world.py
fi

# Deactivate and clean up virtual environment
deactivate
rm -rf venv

# Clean up trigger file
rm -f trigger_hello_world.txt
