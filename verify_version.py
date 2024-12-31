import pkg_resources

BACKEND_REQUIREMENTS = "backend/requirements.txt"
TEST_REQUIREMENTS = "tests/requirements.txt"


def verify_versions(requirements_file):
    with open(requirements_file, 'r') as file:
        requirements = file.readlines()

    for req in requirements:
        try:
            pkg_resources.require(req.strip())
            print(f"{req.strip()} is installed and matches the specified version.")
        except pkg_resources.DistributionNotFound:
            print(f"{req.strip()} is not installed.")
        except pkg_resources.VersionConflict as e:
            print(f"{req.strip()} has a version conflict: {e}")


if __name__ == "__main__":
    print("Verifying backend dependencies:\n")
    verify_versions(BACKEND_REQUIREMENTS)
    print("\nVerifying test dependencies:\n")
    verify_versions(TEST_REQUIREMENTS)
