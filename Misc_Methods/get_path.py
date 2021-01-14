import os
import platform
import getpass


class GetPath:
    @classmethod
    def get_directory_name(cls):
        cwd = os.getcwd()
        directory_name = os.path.basename(cwd)
        return directory_name

    @classmethod
    def get_driver(cls):
        os_name = platform.system()
        current_path = os.getcwd()
        selected_driver = None
        parent_directory = os.path.dirname(current_path)
        if os_name == "Windows":
            selected_driver = os.path.abspath(parent_directory +
                                              "//"+GetPath().get_directory_name()+"//Resources//Drivers//ChromeDriver"
                                              "//chromedriver.exe")
        elif os_name == "Linux":
            selected_driver = os.path.abspath(parent_directory +
                                              "/"+GetPath().get_directory_name()+"/Resources/Drivers/ChromeDriver"
                                              "/chromedriver_linux")
        return selected_driver

    @classmethod
    def get_config(cls, file_name):
        os_name = platform.system()
        current_path = os.getcwd()
        parent_directory = os.path.dirname(current_path)
        path = None
        if os_name == "Windows":
            path = os.path.abspath(parent_directory + "//" + GetPath().get_directory_name() + "//Resources//"
                                                                              "Config_Files//" + file_name)
        elif os_name == "Linux":
            path = os.path.abspath(parent_directory + "/" + GetPath().get_directory_name() + "/Resources"
                                                                             "/Config_Files/" + file_name)
        return path

    @classmethod
    def get_chrome_profile(cls):
        system_username = getpass.getuser()
        path = None
        os_name = platform.system()
        if os_name == "Linux":
            path = '/home/' + system_username + '/.config/google-chrome/Default'
        elif os_name == "Windows":
            path = 'C:/Users/' + system_username + '/Documents/ChromeProfile/User Data'
        return path

    @classmethod
    def save_screenshot(cls, file_name):
        os_name = platform.system()
        current_path = os.getcwd()
        parent_directory = os.path.dirname(current_path)
        path = None
        if os_name == "Windows":
            path = os.path.abspath(parent_directory + "//" + GetPath().get_directory_name() + "//Resources//"
                                                                              "Images//" + file_name)
        elif os_name == "Linux":
            path = os.path.abspath(parent_directory + "/" + GetPath().get_directory_name() + "/Resources"
                                                                             "/Images/" + file_name)
        return path
