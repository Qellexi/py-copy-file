def copy_file(command: str) -> None:
    if not command.startswith("cp"):
        raise ValueError("Incorrect command format.")
    c_files_list = command.split()
    source_file, destination_file = c_files_list[1], c_files_list[2]
    if source_file != destination_file:
        try:
            with (open(source_file, "r") as file_in,
                  open(destination_file, "w") as file_out):
                file_out.write(file_in.read())
        except FileNotFoundError:
            print(f"File {source_file} was not found in the directory.")
