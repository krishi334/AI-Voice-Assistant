class TaskAutomation:
    def automate_task(self, intent):
        if intent == "turn_on_light":
            self.turn_on_light()
        elif intent == "turn_off_light":
            self.turn_off_light()
        elif intent == "play_music":
            self.play_music()
        else:
            print("Intent not recognized.")

    def turn_on_light(self):
        print("Turning on the light.")

    def turn_off_light(self):
        print("Turning off the light.")

    def play_music(self):
        print("Playing music.")