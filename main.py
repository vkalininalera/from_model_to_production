import subprocess

if __name__ == '__main__':

    # List of scripts to run in order
    scripts = [
        "create_model.py",
        "app.py"
    ]

    # Run each script sequentially
    for script in scripts:
        print(f"\n--- Running {script} ---")
        try:
            subprocess.run(["python", script], check=True)
            print(f"✅ Finished {script}")
        except subprocess.CalledProcessError:
            print(f"❌ Error occurred in {script}, stopping pipeline.")
            break
