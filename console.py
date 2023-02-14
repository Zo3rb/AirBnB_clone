#!/usr/bin/python3
"""
Entry point of the command interpreter
"""
import re
import cmd
import sys
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


# Contains all valid class names
CLASSES = [
    "BaseModel",
    "User",
    "State",
    "City",
    "Amenity",
    "Place",
    "Review"
]

# ============== Helper Functions ===============


def parser(line):
    """Parses arguments parsed to our HBNBCommands
    Returns an array of strings
    Args:
        line(str): String passed to cmd
    """

    # Regex gets all sub strings within quotation marks and
    # stores it an av_quoted array in order to treat is as a unit
    av_quoted = re.findall(r'["\']([^"\']+)["\']', line)

    # Each quoted sub string is replaced in line with
    # a place holder "quoted_str"
    line = re.sub(r'["\']([^"\']+)["\']', "quoted_str", line)

    # The regex returns a list of all space-demarcated substrings
    argv = re.findall(r"(\b[^\s]+\b)", line)

    quoted_str_index_counter = 0
    # The placeholder "quoted_str" is replaced with the original
    # quoted string
    for idx, arg in enumerate(argv):
        if arg == "quoted_str":
            argv[idx] = av_quoted[quoted_str_index_counter]
            quoted_str_index_counter += 1
    return argv


def verify_id(id, argv):
    """Verifies if given id exists and returns True when it does
    Args:
        id(str): id to be verified
        argv(list): list of commands passed to cmd
    """

    all_dict = storage.all()
    key = f"{argv[0]}.{argv[1]}"
    if all_dict.get(key):
        return True
    return False


class HBNBCommand(cmd.Cmd):
    """Command interpreter for AirBnB project"""

    prompt = "(hbnb) "

    def precmd(self, line):
        if '.' in line and '(' in line:
            # cls, comd = line.split('.')
            cls, comd = line.split('(')[0].split('.')
            # comd = comd.split('(')[0]

            # Gets the arg inside bracket
            cmd_args = line.split('(')[1]
            if '{' not in cmd_args:
                cmd_args = cmd_args.split(', ')
                for idx, arg in enumerate(cmd_args):
                    cmd_args[idx] = arg.strip(')')
                    if len(cmd_args) == 0:
                        line = f"{comd} {cls}"
                    elif len(cmd_args) >= 1:
                        id = cmd_args[0]
                        if len(cmd_args) == 1:
                            line = f"{comd} {cls} {id}"
                        elif len(cmd_args) == 2:
                            attr_name = cmd_args[1]
                            line = f'{comd} {cls} {id} {attr_name}'
                        elif len(cmd_args) == 3:
                            attr_name = cmd_args[1]
                            value = cmd_args[2]
                            line = f'{comd} {cls} {id} {attr_name} {value}'
            elif '{' in cmd_args:
                try:
                    cmd_args = list(re.findall(
                        r'(["\'].+["\']), (\{.*\})', cmd_args)[0])
                    dict_args = eval(cmd_args[1])
                    id = cmd_args[0]
                    line = f"{comd} {cls} {id} {dict_args}"
                except Exception:
                    print("Invalid input")
                    sys.exit(1)
        return cmd.Cmd.precmd(self, line)

    def do_EOF(self, line):
        """Implements EOF for the command interpreter
        """
        print("")
        return True

    def do_quit(self, line):
        """Quit command to exit the program
        """
        sys.exit()

    def emptyline(self):
        """Ensures that empty line + <ENTER> shouldn't execute anything
        """
        pass

    def do_create(self, line):
        """Creates a new instance of a class
        Saves it to the JSON file and prints the id
        """
        # argv is a vector containing parsed input string
        # Input string involves only args passed to function
        argv = parser(line)
        if len(argv) == 0:
            print("** class name missing **")
        elif argv[0] not in CLASSES:
            print("** class doesn't exist **")
        else:
            model = eval(argv[0])()
            print(model.id)
            storage.save()

    def do_show(self, line):
        """Prints str repr of an instance based on the class name and id
        """
        argv = parser(line)
        if len(argv) == 0:
            print("** class name is missing **")
        elif argv[0] not in CLASSES:
            print("** class doesn't exist **")
        elif len(argv) == 1:
            print("** instance id missing **")
        else:
            all_dict = storage.all()
            key = f"{argv[0]}.{argv[1]}"

            # checks if key is valid
            if all_dict.get(key):
                print(str(all_dict[key]))
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name & id and save the change
        """
        argv = parser(line)
        if len(argv) == 0:
            print("** class name missing **")
        elif argv[0] not in CLASSES:
            print("** class doesn't exist **")
        elif len(argv) == 1:
            print("** instance id missing **")
        else:
            all_dict = storage.all()
            key = f"{argv[0]}.{argv[1]}"

            # checks if key is valid
            if all_dict.get(key):
                del all_dict[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, line):
        """Prints all str representation of all instances
        """

        argv = parser(line)
        all_dicts = storage.all()
        all_objects = []
        class_objects = []  # contains obj when class name is called
        # Stores str(obj) in list if class name is valid
        for k, v in all_dicts.items():
            all_objects.append(str(v))
            if len(argv) != 0:
                cls = v.__class__.__name__
                if argv[0] == cls:
                    class_objects.append(str(v))
        # No class given
        if len(argv) == 0:
            print(all_objects)
        # Class name given and is a valid class
        elif len(argv) == 1:
            if argv[0] in CLASSES:
                print(class_objects)
        # Class name not a valid class
            else:
                print("** class doesn't exist **")

    def do_update(self, line):
        """Updates an instance based on the class and id by adding attribute
        """
        # A list of all lines to be updated
        all_lines = []

        if '{' in line:
            dict_args = re.findall(r'(\{.*\})', line)[0]
            line = re.sub(r'(\{.*\})', "dict", line)
            dict_args = eval(dict_args)
            argv = parser(line)
            for k, v in dict_args.items():
                line = f'{argv[0]} "{argv[1]}" "{k}" "{v}"'
                all_lines.append(line)
        else:
            all_lines.append(line)

        # A loop to update every line in all_lines
        for line in all_lines:
            argv = parser(line)
            if len(argv) == 0:
                print("** class name missing **")
            elif argv[0] not in CLASSES:
                print("** class doesn't exist **")
            elif len(argv) == 1:
                print("** instance id missing **")
            elif len(argv) == 2:
                if verify_id(argv[1], argv) is False:
                    print("** no instance found **")
                else:
                    print("** attribute name missing **")

            elif len(argv) == 3:
                if verify_id(argv[1], argv) is False:
                    print("** no instance found **")
                else:
                    print("** value missing **")
            else:
                if verify_id(argv[1], argv) is False:
                    print("** no instance found **")
                else:
                    all_dict = storage.all()
                    key = f"{argv[0]}.{argv[1]}"
                    obj = all_dict.get(key)

                    # if attribute name already exist, verify its type
                    # and cast new value to the existing type
                    if argv[2] in type(obj).__dict__:
                        attr_type = type(obj.__class__.__dict__[argv[2]])
                        setattr(obj, argv[2], attr_type(argv[3]))
                    else:
                        # if attribute does not exist, just assign to value
                        setattr(obj, argv[2], argv[3])

                    # save the updated objects
            storage.save()

    def do_count(self, line):
        """Retrieves the count of instances of a class
        """
        argv = parser(line)
        count_class = 0
        count_all = 0
        all_dict = storage.all()
        for k, v in all_dict.items():
            if len(argv) != 0 and argv[0] in CLASSES:
                if argv[0] == v.__class__.__name__:
                    count_class += 1
            if len(argv) == 0:
                count_all += 1
        if len(argv) == 0:
            print(count_all)
        elif len(argv) == 1:
            if argv[0] in CLASSES:
                print(count_class)
            else:
                print("** class doesn't exist **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
