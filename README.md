# Elements of Data Science Book Study


## Branches

### Main

This is the Main Branch where everything starts out and ends back in.


https://github.com/SteveN5QC/elements_of_data_science.git


        source Data_Science/bin/activate  # activate your virtual environment if needed


steve@2025HPLaptop:~/elements_of_data_science$ source Data_Science/bin/activate
(Data_Science) steve@2025HPLaptop:~/elements_of_data_science$








## ▶️ Usage
- Launch Jupyter from the command line:


        source Data_Science/bin/activate  # activate your virtual environment if needed
        jupyter notebook <notebook>.ipynb

- This will open the notebook directly in your browser.

- Alternatively, you can start JupyterLab:

        jupyter lab <notebook>.ipynb

Yet another alternative, run directly in WSL and open in Windows browser
If you’re working inside WSL but want to view the notebook in your Windows browser:

        # Activate your virtual environment
        source .venv/bin/activate

        # Launch Jupyter Notebook bound to all interfaces
        jupyter notebook --no-browser --ip=0.0.0.0 --port=8888

        - Copy the URL token printed in the terminal (it looks like http://127.0.0.1:8888/?token=...).
        - In Windows, open your browser and go to:

            - Copy the URL token printed in the terminal (it looks like http://127.0.0.1:8888/?token=...).
            - In Windows, open your browser and go to:

                http://localhost:8888/?token=YOUR_TOKEN

And still another alternative, run in WSL and connect from another device on the same network
If you want to use a browser on a different device (e.g., tablet or laptop on the same Wi‑Fi):

        # Activate your virtual environment
        source .venv/bin/activate

        # Launch Jupyter Notebook bound to your WSL host IP
        jupyter notebook --no-browser --ip=0.0.0.0 --port=8888

        - Find your Windows host IP address:

            ipconfig

        - Look for the IPv4 address under your active network adapter (e.g., 192.168.1.42).
        - On your other device’s browser, go to:

            http://192.168.1.42:8888/?token=YOUR_TOKEN

            - Replace 192.168.1.42 with your actual IP and paste the token from the WSL terminal.

Run JupyterLab (optional)For a more modern interface:

        jupyter lab --no-browser --ip=0.0.0.0 --port=8888

        This way, stakeholders can run the notebook whether they’re in WSL with a Windows browser or connecting from another device on the network.

🔒 Security NoteWhen exposing Jupyter to your local network:- Always use the token provided in the terminal, or set a password:

    jupyter notebook password

- Avoid running with --ip=0.0.0.0 unless you trust your network.
- Never disable authentication (--NotebookApp.token='') unless you’re in a secure, isolated environment.


