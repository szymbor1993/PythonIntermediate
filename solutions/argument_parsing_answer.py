import argparse
import random
from dataclasses import dataclass
from typing import Dict, List


@dataclass
class MinMax:
    min_val: float
    max_val: float


DEFAULT_FILENAME_PREFIX: str = "tab_generated_"
DEFAULT_THRESHOLD_CONFIG: Dict[str, MinMax] = {
    "coord_x": MinMax(-10.0, 10.0),
    "coord_y": MinMax(-10.0, 10.0),
    "coord_z": MinMax(-10.0, 10.0),
    "mass": MinMax(1.0, 1.0)
}


def generate_single_body(config: Dict[str, MinMax]) -> str:
    body_mass = random.uniform(config["mass"].min_val, config["mass"].max_val)

    body_x = random.uniform(config["coord_x"].min_val, config["coord_x"].max_val)
    body_y = random.uniform(config["coord_y"].min_val, config["coord_y"].max_val)
    body_z = random.uniform(config["coord_z"].min_val, config["coord_z"].max_val)

    body_vx = random.uniform(config["coord_x"].min_val, config["coord_x"].max_val)
    body_vy = random.uniform(config["coord_y"].min_val, config["coord_y"].max_val)
    body_vz = random.uniform(config["coord_z"].min_val, config["coord_z"].max_val)

    return f"{body_mass:.5f} {body_x:.5f} {body_y:.5f} {body_z:.5f} {body_vx:.5f} {body_vy:.5f} {body_vz:.5f}"


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("bodies", help="Number of bodies to generate", type=int)
    parser.add_argument("-o", "--output", help="Name of the output file", required=False, default=None)
    args = parser.parse_args()

    dataset_content: List[str] = [str(args.bodies)]
    output_file = args.output if args.output is not None else f"{DEFAULT_FILENAME_PREFIX}{args.bodies}"
    threshold_config = DEFAULT_THRESHOLD_CONFIG

    random.seed()
    for i in range(args.bodies):
        dataset_content.append(generate_single_body(threshold_config))

    dataset_str: str = '\n'.join(dataset_content)
    with open(output_file, 'w+') as f_handler:
        f_handler.write(dataset_str)
