import os


def write_file(working_directory, file_path, content):
    try:
        absolute_path = os.path.abspath(working_directory)
        full_path = os.path.normpath(
            os.path.join(absolute_path, file_path)
        )

        if os.path.commonpath([absolute_path, full_path]) != absolute_path:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

        if os.path.isdir(full_path):
            return f'Error: Cannot write to "{file_path}" as it is a directory'

        os.makedirs(os.path.dirname(full_path), exist_ok=True)

        with open(full_path, "w") as file:
            file.write(content)

        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        return f"Error: {e}"
