def declare_classes()
    class Window_conf:
        def __init__(self, x_ul, y_ul, width, height):
            self.x_ul = x_ul
            self.y_ul = y_ul
            self.width = width
            self.height = height

def reload_config()
    # Delete old variable
    del Window

    # Parse from config-file
    config = configparser.configparser()
    config.readfp(open(r'config.txt'))