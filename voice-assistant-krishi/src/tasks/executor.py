class TaskExecutor:
    def __init__(self):
        pass

    def execute_command(self, command):
        if command == "turn on the lights":
            self.turn_on_lights()
        elif command == "play music":
            self.play_music()
        elif command == "set a reminder":
            self.set_reminder()
        else:
            print("Command not recognized.")

    def turn_on_lights(self):
        print("Turning on the lights...")

    def play_music(self):
        print("Playing music...")

    def set_reminder(self):
        print("Setting a reminder...")