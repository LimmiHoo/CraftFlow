# === Stage 86: Add sample command transcripts for the main CLI workflows ===
# Project: CraftFlow
import subprocess, sys, json, os
from pathlib import Path

def run_cli_demo():
    print("=== CraftFlow CLI Demo ===")
    try:
        # Initialize project if needed
        subprocess.run(["python", "-m", "craftflow.cli", "--init"], check=True)
        
        # Add a new material entry
        print("\n1. Adding Material (Wood):")
        subprocess.run([sys.executable, "-m", "craftflow.cli", "add-material", 
                        "--name", "Oak Wood", "--cost", "25.00", "--quantity", "10"], check=True)
        
        # Add a milestone
        print("\n2. Adding Milestone:")
        subprocess.run([sys.executable, "-m", "craftflow.cli", "add-milestone", 
                        "--title", "Prototype Complete", "--date", "2024-05-15"], check=True)
        
        # Add an inspiration note
        print("\n3. Adding Inspiration Note:")
        subprocess.run([sys.executable, "-m", "craftflow.cli", "add-note", 
                        "--category", "Design", "--text", "Minimalist aesthetic with natural textures."], check=True)
        
        # View summary
        print("\n4. Project Summary:")
        result = subprocess.run([sys.executable, "-m", "craftflow.cli", "summary"], capture_output=True, text=True)
        if result.returncode == 0:
            print(result.stdout.strip())
            
    except subprocess.CalledProcessError as e:
        print(f"Demo step failed at command: {e}")

if __name__ == "__main__":
    run_cli_demo()
