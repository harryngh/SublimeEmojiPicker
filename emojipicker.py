import sublime
import sublime_plugin
import json
import os 


def load_emoji_data():
  dir_path = os.path.dirname(os.path.realpath(__file__))
  with open(os.path.join(dir_path,"emoji_data.json"),encoding='utf-8') as data_file:    
    data = json.load(data_file)
  return data




class EmojiPickerCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    window = self.view.window()
    data = load_emoji_data()["emoji_data"]
    items = [t['emoji_symbol']+' '+t['title'] for t in data]

    def callback(selection):          
        if selection >= 0:
            emoji = data[selection]['emoji_symbol']
            self.view.run_command("insert", {"characters": emoji})

    window.show_quick_panel(items, callback)
