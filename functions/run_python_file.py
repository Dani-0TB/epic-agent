import os
import subprocess
from google.genai import types

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a specified Python file and returns its output (stdout and stderr)",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The relative path to the Python file to execute",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(type=types.Type.STRING),
                description="Optional list of command-line arguments to pass to the Python script",
            ),
        },
        required=["file_path"],
    ),
)


def run_python_file(working_directory, file_path, args=None):
    try:
        absolute_path = os.path.abspath(working_directory)
        full_path = os.path.normpath(
            os.path.join(absolute_path, file_path)
        )

        if os.path.commonpath([absolute_path, full_path]) != absolute_path:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(full_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'

        if file_path.split(".")[-1] != "py":
            return f'Error: "{file_path}" is not a Python file'

        command = ["python", full_path]

        if args:
            command.extend(args)

        result = subprocess.run(
            command,
            cwd=absolute_path,
            capture_output=True,
            text=True,
            timeout=30,
        )

        output_list = []

        if result.returncode != 0:
            output_list.append(f"Process exited with code {result.returncode}")

        stderr_len = len(result.stderr)
        stdout_len = len(result.stdout)

        if stdout_len == 0 and stdout_len == 0:
            output_list.append("No output produced")

        if stdout_len > 0:
            output_list.append(f"STDOUT:\n{result.stdout}")

        if stderr_len > 0:
            output_list.append(f"STDERR:\n{result.stderr}")

        return "\n".join(output_list)

    except Exception as e:
        return f"Error: executing Python file: {e}"
