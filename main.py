import pathlib
import argparse
import venv
import subprocess

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="JAVEC",
        description="""Just another virtual environment creator.""",
        )

    parser.add_argument(
        "-a",
        action="store_true",
        help="create activator in main folder",
        )

    parser.add_argument(
        "-g",
        "--gitignore",
        action="store_true",
        help="create .gitignore file in the root directory",
        )

    parser.add_argument(
        "--swap-gitignore",
        help="""Choose your own .gitignore file. This file will change the
        default .gitignore file used in JAVEC.""",
        default=None,
    )

    parser.add_argument(
        "-i",
        "--install",
        required=False,
        nargs="*",
        help="""Install given packages and put them in requirements_javec.txt"""
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
        print(f"Virtual environment already created at {virtualenvDirectory}")

    if args.a:
        with open(".activator.sh", "w") as f:
            f.write(f"source {virtualenvDirectory}/bin/activate")
        print("Virtual environment activator created")

    if args.swap_gitignore:
        newGitignoreExamplePath = pathlib.Path(args.swap_gitignore)
        exampleGitignorePath = pathlib.Path(__file__).parent/"gitignore_example"
        if newGitignoreExamplePath.exists():
            with open(newGitignoreExamplePath, "r") as f:
                newGitignoreToWrite = f.readlines()
            with open(exampleGitignorePath, "w") as f:
                f.write("".join(newGitignoreToWrite))
            print("Gitignore swapped")
        else:
            print("New .gitignore path does not exist.")

    if args.gitignore:
        exampleGitignorePath = pathlib.Path(__file__).parent/"gitignore_example"
        gitignorePath = currentDirectory/".gitignore"
        with open(exampleGitignorePath, "r") as f:
            gitignoreToWrite = f.readlines()
        with open(gitignorePath, "w") as f:
            f.write("".join(gitignoreToWrite))
        print("Gitignore file created")

    if args.install:
        if len(args.install) > 0:
            completed = subprocess.run(
                [f"{virtualenvDirectory}/bin/python3", "-m", "pip", "install", *args.install],
                capture_output=True,
            )
            print(completed.stdout.decode("utf-8"))
            if not completed.stderr:
                with open("requirements_javec.txt", "a") as f:
                    f.write("".join([f"{package}\n" for package in args.install]))
        else:
            print("Nothing to install.")
