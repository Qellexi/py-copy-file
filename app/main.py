def copy_file(command: str) -> None:
    c_files_list = (command.split("cp "))[1].split(" ")
    source_file = c_files_list[0]
    destination_file = c_files_list[1]
    if source_file != destination_file:
        with open(source_file, "r") as file_in, open(destination_file, "w") as file_out:
            file_out.write(file_in.read())

