import pathlib
import argparse
import venv

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="JAVEC",
        description="""Just another virtual environment creator."""
        )

    parser.add_argument(
        "-a",
        action="store_true",
        help="create activator in main folder"
        )

    parser.add_argument(
        "-g",
        "--gitignore",
        action="store_true",
        help="create .gitignore file in the root directory"
        )

    args = parser.parse_args()
    currentDirectory = pathlib.Path.cwd()
    virtualenvDirectory = pathlib.Path(
        currentDirectory,
        f".{currentDirectory.stem}"
        )

    if not virtualenvDirectory.exists():
        builder = venv.EnvBuilder(with_pip=True, system_site_packages=True)
        builder.create(virtualenvDirectory)
    else:
        print("Virtual environment already created at")

    if args.a:
        with open(".activator.sh", "w") as f:
            f.write(f"source {virtualenvDirectory}/bin/activate")
        print("Virtual environment activator created")

    if args.g:
        exampleGitignorePath = pathlib.Path(__file__).parent/"gitignore_example"
        gitignorePath = currentDirectory/".gitignore"
        with open(exampleGitignorePath, "r") as f:
            gitignoreToWrite = f.readlines()
        with open(gitignorePath, "w") as f:
            f.write("".join(gitignoreToWrite))
        print("Gitignore file created")
