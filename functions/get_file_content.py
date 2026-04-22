import os


MAX_CHARS = 10000


def get_file_content(working_directory, file_path):
    try:
        absolute_path = os.path.abspath(working_directory)
        full_path = os.path.normpath(
            os.path.join(absolute_path, file_path)
        )

        if os.path.commonpath([absolute_path, full_path]) != absolute_path:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(full_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        with open(full_path, "r") as file:
            content = file.read(MAX_CHARS)
            if file.read(1):
                content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
            return content

    except Exception as e:
        return f"Error: {e}"
