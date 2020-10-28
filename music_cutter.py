first_section = ['Parov Stelar - Booty Swing.mp3',0,29000]
second_section = ['9 to 5.mp3',0,19000]

full_list = [first_section, second_section]

def musicSection(the_list):

  the_track = AudioSegment.empty()

  for element in the_list:
    this_sound = AudioSegment.from_mp3(element[0])
    this_section = this_sound[element[1]:element[2]]
    the_track = the_track + this_section
    
  the_track.export("function_track.mp3", format="mp3")