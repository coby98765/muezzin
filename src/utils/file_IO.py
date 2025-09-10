from src.utils.logger import Logger
import os,json,re

# logger setup
logger = Logger.get_logger(index="utils_log",name="FileIO")


class FileIO:

    @staticmethod
    def import_json(path):
        try:
            with open(path, 'r') as file:
                data = json.load(file)

            logger.info(f'FileIO.import_json, imported JSON: {path}')
            return data

        except FileNotFoundError:
            msg = f"Error: file '{path}' not found."
            logger.error(f"FileIO.import_json, {msg}")
            raise Exception(msg)
        except json.JSONDecodeError:
            msg = f"Error: Canot decode JSON from {path}."
            logger.error(f"FileIO.import_json, {msg}")
            raise Exception(msg)
        except Exception as e:
            msg = f"error: {e}"
            logger.error(f"FileIO.import_json, {msg}")
            raise Exception(msg)

    @staticmethod
    def export_json(destination,name,data):
        path_and_name=""
        try:
            # validate filename
            name_valid,msg = FileIO.validate_filename(name)
            if not name_valid:
                raise Exception(msg)
            # validate path
            if not os.path.isdir(destination):
                os.mkdir(destination)

            path_and_name = f"{destination}/{name}.json"

            with open(path_and_name, 'w') as json_file:
                json.dump(data, json_file, indent=4)
            logger.info(f"FileIO.export_json, dumped JSON data to '{path_and_name}'")

        except IOError as e:
            msg = f"Error writing to file '{path_and_name}': {e}"
            logger.error(f"FileIO.export_json, {msg}")
            raise Exception(msg)
        except TypeError as e:
            msg = f"Error serializing data to JSON: {e}"
            logger.error(f"FileIO.export_json, {msg}")
            raise Exception(msg)
        except Exception as e:
            msg = f"An unexpected error occurred: {e}"
            logger.error(f"FileIO.export_json, {msg}")
            raise Exception(msg)

    @staticmethod
    def export_binary_file(destination,filename, data_bytes,file_type):
        path_and_name=""
        try:
            # validate filename
            name_valid, msg = FileIO.validate_filename(filename)
            if not name_valid:
                raise Exception(msg)
            # validate path
            if not os.path.isdir(destination):
                os.mkdir(destination)

            path_and_name = f"{destination}/{filename}.{file_type}"

            with open(path_and_name, 'wb') as f:
                f.write(data_bytes)
            logger.info(f"FileIO.write_binary_file, wrote data to '{path_and_name}'")
        except IOError as e:
            msg = f"Error writing to file '{filename}': {e}"
            logger.error(f"FileIO.write_binary_file, {msg}")
            raise Exception(msg)
        except Exception as e:
            msg = f"An unexpected error occurred: {e}"
            logger.error(f"FileIO.write_binary_file, {msg}")
            raise Exception(msg)

    @staticmethod
    def import_binary_file(path):
        try:
            with open(path, 'rb') as file:
                data = file.read()
            logger.info(f'FileIO.import_binary_file, imported data: {path}')
            return data
        except FileNotFoundError:
            msg = f"Error: file '{path}' not found."
            logger.error(f"FileIO.import_binary_file, {msg}")
            raise Exception(msg)
        except Exception as e:
            msg = f"error: {e}"
            logger.error(f"FileIO.import_binary_file, {msg}")
            raise Exception(msg)

    @staticmethod
    def validate_filename(filename):
        if re.search(r'[/\\:*?"<>|]', filename):
            return False, "Filename invalid char."
        if len(filename) > 255:
            return False, "Filename too long."
        if filename.startswith(' ') or filename.endswith(' '):
            return False, "Filename starts or ends with a space."
        return True, "Filename valid."
