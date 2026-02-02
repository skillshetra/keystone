#!/usr/bin/env python3

"""
main.py

Entry point for the Keystone Data Science project.
This script runs the full analysis pipeline using the Key_Stone_Analysis function.
"""

# Import the main analysis pipeline #
from pipeline.run_analysis import Key_Stone_Analysis

# Ensure the script runs only when executed directly
if __name__ == "__main__":
    # Run the Keystone analysis pipeline
    # This function should handle:
    #   - Loading data from the database
    #   - Computing metrics
    #   - Performing statistical analysis
    #   - Persisting results
    Key_Stone_Analysis()
    # Print a success message #
    print("\n" + "="*60)
    print("*" * 5 + " ✅  Keystone Analysis Completed Successfully! ✅ " + "*" * 5)
    print("="*60 + "\n")