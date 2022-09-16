import subprocess
import argparse
import yaml
import shutil

parser = argparse.ArgumentParser(description="Which preset to use")
parser.add_argument("--config", type=str, help="Which config to use", default="default", required=False)
args = parser.parse_args()

# check if config exists, if not copy example config
try:
    f = open("sd-launcher-config.yaml")
except FileNotFoundError:
    shutil.copy("sd-launcher-config-example.yaml", "sd-launcher-config.yaml")
    print("File sd-launcher-config.yaml not found. Copying config_example.yaml")

# open config
with open("sd-launcher-config.yaml", "r") as f:
    config = yaml.safe_load(f)
    f.close()

default_params = config["default"]

# check if desired config exists, offer to use default if not
try:
    config_params = config[args.config]
except KeyError:
    print(f"Config {args.config} not found. Use default?")
    # ask if default should be used
    answer = input("y/n: ")
    if answer == "y":
        config_params = default_params
    else:
        exit()

# Create a list of params and add defaults needed for all configs to run this thing
launch_args = []
for key, value in config["environment"].items():
    launch_args.append(str(value))

# Go through default params and config params and add to launch_args
for key, value in {**default_params, **config_params}.items():
    if value is not None and key != "extra-params":
        launch_args.append(f"--{key}")
        launch_args.append(str(value))
    if key == "extra-params" and value is not None:
        for param in value:
            if param is not None:
                launch_args.append(param)
print(f"Launching {launch_args[1]} with args {launch_args[2:]}")

# Do the thing
subprocess.run(launch_args)
