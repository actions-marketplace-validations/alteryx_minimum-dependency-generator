import argparse

from minimum_dependency_generator import generate_min_requirements

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="reads a requirements file and outputs the minimized requirements")
    parser.add_argument('--requirements_paths', nargs='+',
                        help='path for requirements to minimize', required=True)
    args = parser.parse_args()
    return generate_min_requirements(args.requirements_paths)