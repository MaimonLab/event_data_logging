from pathlib import Path


def validate_filename(filename):
    # File shouldn't exist, but if it does, add a number to the
    # end until the name is free.
    file_nth = 2
    file_path = Path(filename).resolve()

    file_stem = file_path.stem

    directory = file_path.parent
    # path does not exist, try to make
    if not directory.exists():
        try:
            Path.mkdir(directory, parents=True)
        except:
            raise PermissionError(f"failed to make {directory}")

    while file_path.exists():
        file_path = file_path.with_name(f"{file_stem}_{file_nth}").with_suffix(
            file_path.suffix
        )
        file_nth += 1

    return file_path
