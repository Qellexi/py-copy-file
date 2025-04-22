def copy_file(command: str) -> None:
    c_files_list = (command.split("cp "))[1].split(" ")
    file = c_files_list[0]
    new_file = c_files_list[1]
    if file != new_file:
        with open(file, "r") as file_in, open(new_file, "w") as file_out:
            file_out.write(file_in.read())
