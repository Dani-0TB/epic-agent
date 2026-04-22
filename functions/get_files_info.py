import os


def get_files_info(working_directory, directory="."):
    try:
        absolute_path = os.path.abspath(working_directory)
        target_path = os.path.normpath(
            os.path.join(absolute_path, directory)
        )

        if os.path.commonpath([absolute_path, target_path]) != absolute_path:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        if not os.path.isdir(target_path):
            return f'Error: "{directory}" is not a directory'

        directory_listing = os.listdir(target_path)
        listing = []

        for name in directory_listing:
            item_path = os.path.join(target_path, name)
            is_dir = os.path.isdir(item_path)
            file_size = os.path.getsize(item_path)
            listing.append(
                f"- {name}: file_size={file_size} bytes, is_dir={is_dir}")

        return "\n".join(listing)

    except Exception as e:
        return f"Error: {e}"
