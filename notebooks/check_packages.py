# check_packages.py

import importlib

# List of packages you expect in your environment
packages = [
    "IPython",
    "statsmodels",
    "matplotlib",
    "pandas",
    "numpy",
    "seaborn",
    "scipy",
    "sklearn",
    "h5py"
]

def check_packages(pkg_list):
    results = {}
    for pkg in pkg_list:
        try:
            importlib.import_module(pkg)
            results[pkg] = "✅ Installed"
        except ModuleNotFoundError:
            results[pkg] = "❌ Missing"
    return results

if __name__ == "__main__":
    results = check_packages(packages)
    print("Package check results:")
    for pkg, status in results.items():
        print(f"{pkg:12} : {status}")